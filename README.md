# 🧠 Playground API

> A production-grade FastAPI project that demonstrates AI inference through OCR, face detection, and chatbot capabilities — fully containerized and CI/CD-ready.

![CI Checks](https://github.com/tserdar/playground_api/actions/workflows/basic_ci_flow.yaml/badge.svg)
![CD Checks](https://github.com/tserdar/playground_api/actions/workflows/basic_cd_flow.yaml/badge.svg)

---

## 💸 Cost & Infrastructure

__🟢 This project is intentionally built to cost virtually 0$ and run on FREE tiers only.__  
__The focus: Live demo with zero-cost operation:__

- 🐳 **Docker** (local or VM)
- 🆓 **GitHub Actions** (CI/CD on free tier)
- ☁️ **GCP VM (e2-micro)** — free-tier eligible
- 💡 **Open-source models** (Qwen2, EasyOCR, RetinaFace)
- 🔑 **No paid APIs or services required**

The only cost for the whole project is the domain name.
---

## 🧱 Tech Stack

### ⚙️ Backend
- **Python 3.12.9**
- **FastAPI** for async REST APIs
- **uvicorn** & **gunicorn** for ASGI serving
- **WebSockets** for live chat
- **uv** for fast dependency & virtualenv management

### 🤖 AI & Deep Learning
- `easyocr` for OCR
- `retina-face` for face detection
- `transformers`, `torch`, `accelerate` for chatbot (Qwen2)
- OpenCV for visualization

### 🐋 DevOps & Runtime
- **Dockerized** with `uv`-based build layers
- CI with **Ruff** linter & `pytest`
- CD via **SSH deploy to GCP VM**

---

## 🚀 Features

| Feature        | Description                              |
|----------------|------------------------------------------|
| `/ocr`         | Extracts text from images (EasyOCR)      |
| `/face`        | Detects faces & landmarks (RetinaFace)   |
| `/chat` (WS)   | Real-time chatbot via WebSocket (Qwen2)  |
| `/`            | Healthcheck endpoint                     |
| **Visualize**  | Optional annotated image responses       |

---

## 🔁 CI/CD

- **CI**: Linting (Ruff) + Unit Tests (Pytest)
- **CD**: Tag-based SSH deployment to GCP VM
- Configured via `.github/workflows/*.yaml`
- Secrets:
  - `GCP_VM_SSH_KEY`
  - `GCP_VM_IP`
  - `GCP_VM_USER`

---

## ✅ Testing

- FastAPI `TestClient` used for route validation
- Mocked model inference for OCR & face detection
- Tested:
  - `GET /`
  - `POST /ocr`
  - `POST /face`

---

## 📌 Summary

This repo demonstrates:
- ✅ Modular AI inference API
- ✅ Docker-first development
- ✅ Fast and type-safe backend with FastAPI
- ✅ Reproducible builds using `uv`
- ✅ Fully automated CI/CD pipeline
- ✅ __Virtually $0 to run — every component can be hosted for FREE__
