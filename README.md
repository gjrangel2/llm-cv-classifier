🗂️ Estructura del repositorio

llm-cv-classifier/
├── app/
│   └── main.py
├── model/
│   └── trainer.py
├── data/
│   └── train.csv
├── requirements.txt
├── Dockerfile
└── README.md

# 🧠 LLM CV Classifier API

Este proyecto despliega una API REST con FastAPI que utiliza un modelo LLM (BERT multilingüe) para clasificar currículums por perfil profesional. El modelo fue entrenado y desplegado en una instancia EC2 de AWS usando Docker.

## 🚀 Tecnologías
- FastAPI
- Hugging Face Transformers
- Docker
- AWS EC2 (capa gratuita)
- Python 3.10

## 📦 Instalación local

```bash
git clone https://github.com/tuusuario/llm-cv-classifier.git
cd llm-cv-classifier
pip install -r requirements.txt
uvicorn app.main:app --reload


🐳 Docker

<img width="699" height="132" alt="image" src="https://github.com/user-attachments/assets/0c84c861-ef7f-4814-b523-6354152fdf83" />

docker build -t llm-api .
docker run -d -p 8000:8000 llm-api

🌐 Endpoint
POST /predict: Recibe un texto y devuelve el perfil estimado y la confianza.
<img width="691" height="154" alt="image" src="https://github.com/user-attachments/assets/aeff9a20-a87a-41f1-853b-d72001420d9d" />

{
  "text": "Desarrollador con experiencia en Spring Boot y MySQL"
}

☁️ Despliegue en AWS
EC2 Ubuntu 22.04 (t2.micro)

Docker instalado

Proyecto clonado y contenedor ejecutado

Acceso público por IP: http://<IP>:8000/docs

📊 Monitoreo y seguridad
Logging con logging

Umbral de confianza para revisión manual

Autenticación básica con JWT (opcional)


CREDITOS

Geyson Rangel

