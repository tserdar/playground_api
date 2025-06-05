"""API route for chatbot via WebSocket."""

import logging

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from api.modules.chat.models import Qwen2Chatbot

router = APIRouter()
logger = logging.getLogger(__name__)


@router.websocket("/chat")
async def chat_with_chatbot(websocket: WebSocket) -> None:
    """WebSocket endpoint for real-time chat with the chatbot."""
    await websocket.accept()
    chatbot = Qwen2Chatbot()

    try:
        while True:
            user_input = await websocket.receive_text()
            if user_input.lower() in {"exit", "quit"}:
                await websocket.send_text("Goodbye!")
                await websocket.close()
                break

            if hasattr(chatbot, "stream_response"):
                history = chatbot.prepare_history(user_input)
                response_text = ""
                for chunk in chatbot.stream_response(history):
                    await websocket.send_text(chunk)
                    response_text += chunk
                chatbot.history = [*history, {"role": "assistant", "content": response_text}]
            else:
                response = chatbot.chat(user_input)
                await websocket.send_text(response)

    except WebSocketDisconnect:
        logger.info("WebSocket disconnected")
    except Exception:
        logger.exception("WebSocket error.")
        await websocket.close(code=1011)
