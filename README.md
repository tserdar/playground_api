![CI Checks](https://github.com/tserdar/playground_api/actions/workflows/basic_ci_flow.yaml/badge.svg)![CD Checks](https://github.com/tserdar/playground_api/actions/workflows/basic_cd_flow.yaml/badge.svg)

🧠 Playground API
A production-grade project which costs virtually 0$, demonstrating AI inference using OCR, face detection, and chatbot capabilities, fully containerized and deployable via CI/CD pipelines.

🧱 Tech Stack
⚙️ Backend
Python 3.12.9

FastAPI for high-performance, async REST APIs

WebSocket support for real-time chatbot

uvicorn & gunicorn for serving

uv for fast dependency resolution and virtual environment management

🤖 AI & Deep Learning
Computer Vision:

opencv-python

retina-face for face detection

easyocr for OCR

NLP:

transformers (Qwen2-0.5B-Instruct model)

accelerate, torch

Token-aware chatbot logic for memory-efficient conversation

🐋 Containerization
Docker-based with layer caching

Fast builds using uv (replaces pip + venv)

Configured for GPU readiness (torch_dtype="auto", device_map)

🚀 CI/CD Workflow
✅ Continuous Integration
GitHub Actions: .github/workflows/basic_ci_flow.yaml

Linting: Ruff

Testing:

pytest tests for /ocr, /face, /

Runs in isolated virtualenv via uv

Smart caching: ~/.cache/uv and .venv

🚢 Continuous Deployment
GitHub Actions: .github/workflows/basic_cd_flow.yaml

Triggered on: Git tag push

SSH deploys to GCP VM

Pulls latest code, resets state, runs deploy.sh

📦 Features
Feature	Description
OCR	Extracts text from uploaded images via EasyOCR
Face Detection	Detects faces and landmarks with RetinaFace and returns bounding boxes
Chatbot	Real-time Qwen2-based AI chat via WebSocket
Web Visualization	Optionally returns annotated images via /face and /ocr APIs
Test Coverage	Unit-tested FastAPI routes with mocking and image stubs

🔧 Project Structure
bash
Copy
Edit
.
├── api/
│   ├── modules/          # Face, OCR, Chat logic
│   ├── routes/           # FastAPI endpoints
│   └── utils/            # Shared utility functions
├── tests/                # pytest test suite
├── run.py                # FastAPI app entrypoint
├── Dockerfile            # Container definition
├── pyproject.toml        # Dependencies and settings
├── .github/workflows/    # CI/CD pipelines
└── README.md
📡 API Endpoints
Endpoint	Method	Description
/	GET	Root endpoint (welcome message)
/ocr	POST	OCR on uploaded image
/face	POST	Face detection + optional visualization
/chat	WS	WebSocket endpoint for real-time chat

🔐 Security
GitHub Secrets:

GCP_VM_SSH_KEY

GCP_VM_IP

GCP_VM_USER

Deployment uses SSH with limited permissions for safe, controlled updates

🧪 Testing Highlights
tests/test_ocr.py, test_face.py, test_run.py

Uses FastAPI’s TestClient

Extensive use of mocking to simulate image input and bypass real inference

📌 Summary
This repo showcases:

Clean FastAPI architecture

AI/ML integration (OCR, face detection, chat)

Dockerized, production-capable code

Modern CI/CD pipelines with test + deploy automation

Real-time communication via WebSockets
