"""Script that contains base and wrapper classes for chatbots."""

from abc import ABC, abstractmethod

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


class TokenLimitedChatbot(ABC):
    """Abstract base class for chatbots with limited token budget."""

    def __init__(self, max_memory_tokens: int = 512) -> None:
        """Initialize the chatbot with a memory limit.

        Args:
            max_memory_tokens (int): Maximum number of tokens to keep in memory.

        """
        self.max_memory_tokens = max_memory_tokens
        self.history: list[dict[str, str]] = []

    @abstractmethod
    def generate_response(self, messages: list[dict[str, str]], max_new_tokens: int = 128) -> str:
        """Generate a model response from message history.

        Args:
            messages (list[dict[str, str]]): Chat history.
            max_new_tokens (int): Max tokens to generate.

        Returns:
            str: Model-generated response.

        """
        pass  # noqa: PIE790

    @abstractmethod
    def num_tokens(self, messages: list[dict[str, str]]) -> int:
        """Compute number of tokens in the given message list.

        Args:
            messages (list[dict[str, str]]): Chat history.

        Returns:
            int: Number of tokens.

        """
        pass  # noqa: PIE790

    def _truncate_history(self, user_message: str) -> list[dict[str, str]]:
        """Truncate the conversation history to fit within the token budget.

        Args:
            user_message (str): The next user input.

        Returns:
            list[dict[str, str]]: Trimmed message history.

        """
        temp_history = [*self.history, {"role": "user", "content": user_message}]
        while self.num_tokens(temp_history) > self.max_memory_tokens and len(self.history) > 1:
            self.history.pop(1)  # Preserve system prompt
            temp_history = [*self.history, {"role": "user", "content": user_message}]
        return temp_history

    def chat(self, user_message: str) -> str:
        """Process a user message and return the chatbot's response.

        Args:
            user_message (str): User input.

        Returns:
            str: Chatbot response.

        """
        trimmed_history = self._truncate_history(user_message)
        trimmed_history.append({"role": "user", "content": user_message})
        response = self.generate_response(trimmed_history)
        self.history = [*trimmed_history, {"role": "assistant", "content": response}]
        return response


class Qwen2Chatbot(TokenLimitedChatbot):
    """Wrapper class for Qwen2 model to fit TokenLimitedChatbot interface."""

    def __init__(
        self,
        model_name: str = "Qwen/Qwen2-0.5B-Instruct",
        device: str = "cpu",
        max_memory_tokens: int = 512,
    ) -> None:
        """Initialize the Qwen2 model and tokenizer.

        Args:
            model_name (str): HuggingFace model ID.
            device (str): Device to run model on.
            max_memory_tokens (int): Max history tokens.

        """
        super().__init__(max_memory_tokens=max_memory_tokens)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype="auto", device_map=device)
        self.device = device

        system_prompt = {
            "role": "system",
            "content": "You are a concise AI assistant. Limit responses to 1-2 sentences.",
        }
        # Initial system prompt
        self.history.append(system_prompt)

    def num_tokens(self, messages: list[dict[str, str]]) -> int:
        """Count tokens in a message list.

        Args:
            messages (list[dict[str, str]]): Chat history.

        Returns:
            int: Token count.

        """
        prompt = self.tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True)
        return len(prompt)

    def generate_response(self, messages: list[dict[str, str]], max_new_tokens: int = 128) -> str:
        """Generate response using Qwen2 model.

        Args:
            messages (list[dict[str, str]]): Chat history.
            max_new_tokens (int): Max tokens to generate.

        Returns:
            str: Model output.

        """
        prompt_text = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = self.tokenizer([prompt_text], return_tensors="pt").to(self.device)

        with torch.no_grad():
            outputs = self.model.generate(inputs.input_ids, max_new_tokens=max_new_tokens)

        new_tokens = [output[len(input_ids) :] for input_ids, output in zip(inputs.input_ids, outputs, strict=False)]
        return self.tokenizer.batch_decode(new_tokens, skip_special_tokens=True)[0]


def main() -> None:
    """Test chatbot."""
    print("Welcome to Qwen2 Chatbot! Type 'exit' or 'quit' to end the session.\n")  # noqa: T201
    chatbot = Qwen2Chatbot()

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")  # noqa: T201
            break

        reply = chatbot.chat(user_input)
        print(f"Bot: {reply}\n")  # noqa: T201


if __name__ == "__main__":
    main()
