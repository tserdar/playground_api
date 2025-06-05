FROM python:3.12.9

# System dependencies (including libGL)
RUN apt-get update && apt-get install -y libgl1 && apt-get clean

RUN pip install uv 

WORKDIR /app

# Start this layer separately here to optimize building speed.
COPY pyproject.toml /app
COPY . /app  

RUN uv venv && uv run -m install_deps

EXPOSE 8000

CMD ["uv", "run", "gunicorn", "-k", "uvicorn.workers.UvicornWorker", "run:app", "--bind", "0.0.0.0:8000", "--workers", "4", "--preload"]