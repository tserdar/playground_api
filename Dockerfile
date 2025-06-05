FROM python:3.12.9

# System dependencies (including libGL)
RUN apt-get update && apt-get install -y libgl1 && apt-get clean

RUN pip install uv 

WORKDIR /app

# Start this layer separately here to optimize building speed.
COPY pyproject.toml /app
COPY install_deps.py /app
RUN uv venv && uv run -m install_deps

COPY . /app  


EXPOSE 8000

CMD ["uv", "run", "uvicorn", "run:app", "--host", "0.0.0.0", "--port", "8000"]