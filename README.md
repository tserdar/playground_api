# 🧠 Playground API

> A containerized AI-powered FastAPI backend with real-time chat, face detection, and OCR — built using PyTorch, Hugging Face Transformers, and OpenCV. Deployed via CI/CD on a zero-cost cloud setup.

![CI Checks](https://github.com/tserdar/playground_api/actions/workflows/basic_ci_flow.yaml/badge.svg)
![CD Checks](https://github.com/tserdar/playground_api/actions/workflows/basic_cd_flow.yaml/badge.svg)

---

## 📌 Highlights

- ✅ FastAPI + WebSocket + REST — real-time API stack
- ✅ Deep Learning: **PyTorch**, **Transformers**
- ✅ Docker-first architecture with optimized layers
- ✅ Deployed on **free-tier cloud** with secure GitHub-based CD
- ✅ Uses **only open-source models** — no paid SaaS or API gateways
- ✅ Built with **cost-awareness** in mind: __zero dollar infra__

---

## 💸 Zero-Cost Architecture

__🟢 This project is designed to be FREE to run.__  
All components run on free-tier infrastructure with open-source tooling:

- 🐳 Dockerized deployment
- ☁️ GCP e2-micro VM (always-free tier)
- 🧪 GitHub Actions for CI/CD (free-tier)
- 🧠 Inference using local models — no paid APIs or usage limits
- 🔐 Deployment via secure SSH (no orchestration overhead)

---

## 🧱 Tech Stack

### 🔙 Backend
- **Python 3.12**
- **FastAPI** (high-performance async API)
- **Uvicorn** + **Gunicorn** for ASGI serving
- **WebSockets** (for real-time chat)
- **uv** (lightweight virtualenv + dependency manager)

### 🤖 Machine Learning & Inference
- **PyTorch** — core runtime for all deep learning models
- **Hugging Face Transformers** — `Qwen2-0.5B-Instruct` for chat
- **EasyOCR** — OCR from images (Torch-based)
- **RetinaFace** — Face detection with facial landmarks
- **OpenCV** — Image manipulation & annotation
- **Accelerate** — Lightweight GPU utilization

---

## 📦 Features

| Feature        | Description                                            |
|----------------|--------------------------------------------------------|
| `/ocr`         | OCR on images via EasyOCR                              |
| `/face`        | Face detection & landmark visualization via RetinaFace |
| `/chat` (WS)   | Real-time AI chatbot (Qwen2) over WebSocket            |
| `/`            | Root health endpoint                                   |
| `visualize`    | Returns annotated images on demand (bounding boxes, etc.) |

---

## 🔁 CI/CD Pipeline

- **CI**: Linting (Ruff) + Tests (Pytest)
- **CD**: Auto-deploy on Git tag push to GCP VM
- Managed via GitHub Actions:
  - `.github/workflows/basic_ci_flow.yaml`
  - `.github/workflows/basic_cd_flow.yaml`
- **Secrets Managed**:
  - `GCP_VM_SSH_KEY`
  - `GCP_VM_USER`
  - `GCP_VM_IP`

---

## ✅ Testing

- `pytest` + FastAPI’s `TestClient`
- Mocked inference for OCR/Face detection
- Coverage:
  - `GET /`
  - `POST /ocr`
  - `POST /face`
  - Optional `visualize=true` rendering

---
