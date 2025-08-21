# 🤖 Cloud-Native AI Sentiment Analysis API

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Available-brightgreen)](http://13.60.69.48)
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue)](./Dockerfile)
[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-Modern%20API-009688)](https://fastapi.tiangolo.com)
[![AWS](https://img.shields.io/badge/AWS-EC2%20Deployed-orange)](https://aws.amazon.com/ec2/)

> **A production-ready sentiment analysis service demonstrating end-to-end ML deployment on AWS**

This project showcases the complete machine learning lifecycle: from model training and API development to containerization and cloud deployment. Built with modern MLOps practices, it serves as a foundation for scalable AI applications.

## 🎯 Project Highlights

- **87.6% Model Accuracy** on IMDb movie review classification
- **Production Deployment** on AWS EC2 with Docker containerization  
- **RESTful API** with automatic interactive documentation
- **Scalable Architecture** ready for enterprise integration
- **Complete Documentation** including technical deep-dive

---

## 🚀 Live Demo & Quick Start

### 🌐 Try the Live API
- **Base URL**: http://13.60.69.48
- **Interactive Docs**: http://13.60.69.48/docs
- **Health Check**: http://13.60.69.48

### 📝 Quick API Test
```bash
curl -X POST "http://13.60.69.48/predict/" \
  -H "Content-Type: application/json" \
  -d '{"text": "This movie was absolutely fantastic!"}'
```

**Response:**
```json
{
  "sentiment": "positive"
}
```

---

## 🏗️ Architecture Overview

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Client Apps   │───▶│   FastAPI       │───▶│  ML Pipeline    │
│                 │    │   Web Server    │    │                 │
│ • Web Apps      │    │                 │    │ • TF-IDF        │
│ • Mobile Apps   │    │ • Input Valid.  │    │ • Logistic Reg. │
│ • curl/Postman  │    │ • Auto Docs     │    │ • Predictions   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                ▲
                                │
                    ┌─────────────────┐
                    │   Docker        │
                    │   Container     │
                    │                 │
                    │ • Isolated Env  │
                    │ • Port Mapping  │
                    │ • Dependencies  │
                    └─────────────────┘
                                ▲
                                │
                    ┌─────────────────┐
                    │   AWS EC2       │
                    │   Ubuntu Server │
                    │                 │
                    │ • Public IP     │
                    │ • Security Grp  │
                    │ • Auto-scaling  │
                    └─────────────────┘
```

---

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **ML Framework** | scikit-learn | Model training & inference |
| **Text Processing** | TF-IDF Vectorizer | Feature extraction from text |
| **Web Framework** | FastAPI | RESTful API development |
| **Server** | Uvicorn | ASGI web server |
| **Containerization** | Docker | Application packaging |
| **Cloud Platform** | AWS EC2 | Production hosting |
| **Data Processing** | Pandas | Data manipulation |
| **Model Persistence** | joblib | Model serialization |

---

## 📖 API Usage

### 🔗 Available Endpoints

| Endpoint | Method | Description | Parameters |
|----------|---------|-------------|------------|
| `/` | GET | Health check and welcome message | None |
| `/predict/` | POST | Predict sentiment of text | `{"text": "string"}` |
| `/docs` | GET | Interactive API documentation | None |

### 💻 Usage Examples

#### Using cURL
```bash
# Positive sentiment example
curl -X POST "http://13.60.69.48/predict/" \
  -H "Content-Type: application/json" \
  -d '{"text": "This movie was absolutely fantastic!"}'

# Negative sentiment example  
curl -X POST "http://13.60.69.48/predict/" \
  -H "Content-Type: application/json" \
  -d '{"text": "Terrible plot and bad acting."}'
```

#### Using Python
```python
import requests

# API endpoint
url = "http://13.60.69.48/predict/"

# Test positive sentiment
response = requests.post(url, json={"text": "Amazing cinematography!"})
print(response.json())  # {'sentiment': 'positive'}

# Test negative sentiment
response = requests.post(url, json={"text": "Boring and predictable."})
print(response.json())  # {'sentiment': 'negative'}
```

#### Using JavaScript
```javascript
// Fetch API example
const predictSentiment = async (text) => {
  const response = await fetch('http://13.60.69.48/predict/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text })
  });
  return await response.json();
};

// Usage
predictSentiment("Great movie!").then(console.log);
```

---

## 🛠️ Local Development Setup

### 📋 Prerequisites
- **Python 3.10+** (recommended)
- **Docker** (for containerization)
- **Git** (for version control)

### 🚀 Quick Start

#### Option 1: Docker (Recommended)
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/sentiment-api.git
cd sentiment-api

# Download the dataset (see Dataset section below)
# Place IMDB Dataset.csv in the root directory

# Build and run with Docker
docker build -t sentiment-api .
docker run -p 8080:80 sentiment-api

# Access the application
open http://localhost:8080
```

#### Option 2: Local Python Environment
```bash
# Clone and navigate
git clone https://github.com/YOUR_USERNAME/sentiment-api.git
cd sentiment-api

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download dataset (see below) and train model
python train_model.py

# Run the application
uvicorn app.main:app --host 0.0.0.0 --port 8080

# Access the application
open http://localhost:8080
```

### 📊 Dataset Setup

The model requires the IMDb Movie Reviews Dataset:

1. **Download**: [IMDb Dataset on Kaggle](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
2. **Extract**: Place `IMDB Dataset.csv` in the project root
3. **Train**: Run `python train_model.py` to generate model files

**Note**: The dataset is excluded from Git due to size (63MB). Training creates two files:
- `models/sentiment_model.joblib` (trained classifier)
- `models/sentiment_vectorizer.joblib` (TF-IDF vectorizer)

---

## 🧠 Model Performance

### 📊 Training Results
- **Dataset**: IMDb Movie Reviews (10,000 samples)
- **Algorithm**: Logistic Regression with TF-IDF features
- **Accuracy**: **87.6%** on test set (2,000 samples)
- **Features**: 5,000 most frequent words
- **Training Time**: ~30 seconds on standard laptop

### 🎯 Model Details
| Metric | Value |
|--------|-------|
| **Model Type** | Logistic Regression |
| **Vectorization** | TF-IDF (max 5,000 features) |
| **Train/Test Split** | 80/20 |
| **Random State** | 42 (reproducible) |
| **Test Accuracy** | 87.6% |

### 🔍 Sample Predictions
```python
# High confidence predictions
"Amazing movie!" → positive (confident)
"Terrible acting" → negative (confident)
"It was okay"    → mixed results (lower confidence)
```

---

## 🚀 Deployment Architecture

### 🏗️ Infrastructure
- **Platform**: AWS EC2 (t2.micro)
- **OS**: Ubuntu 20.04 LTS
- **Container**: Docker with Python 3.10-slim
- **Web Server**: Uvicorn (ASGI)
- **Port**: 80 (HTTP)

### 🔒 Security & Networking
- **Security Group**: HTTP (80) open to 0.0.0.0/0
- **SSH Access**: Key-pair authentication only
- **Container Isolation**: Docker containerization
- **Input Validation**: Pydantic schema validation

### 📈 Scalability Considerations
- **Horizontal Scaling**: Load balancer + multiple EC2 instances
- **Vertical Scaling**: Larger EC2 instance types
- **Container Orchestration**: Kubernetes/ECS for production
- **Database**: Add persistent storage for logs/analytics

---

## 🔧 Development & Contributing

### 🧪 Testing
```bash
# Test the API locally
curl -X POST "http://localhost:8080/predict/" \
  -H "Content-Type: application/json" \
  -d '{"text": "Test message"}'

# Check health endpoint
curl http://localhost:8080/
```

### 📁 Project Structure
```
sentiment-api/
├── app/
│   └── main.py              # FastAPI application
├── models/
│   ├── sentiment_model.joblib     # Trained model
│   └── sentiment_vectorizer.joblib # TF-IDF vectorizer
├── train_model.py           # Model training script
├── requirements.txt         # Python dependencies
├── Dockerfile              # Container configuration
├── README.md               # This file
└── PROJECT_REPORT.md       # Detailed technical report
```

### 🔄 Future Enhancements
- [ ] **Model Improvements**: BERT/transformer models
- [ ] **MLOps Pipeline**: MLflow for experiment tracking
- [ ] **Monitoring**: Prometheus + Grafana dashboards
- [ ] **CI/CD**: GitHub Actions for automated deployment
- [ ] **Database**: PostgreSQL for request logging
- [ ] **Caching**: Redis for improved response times
- [ ] **Authentication**: JWT-based API security
- [ ] **Rate Limiting**: Prevent API abuse

---

## 📚 Learn More

### 📖 Documentation
- **[PROJECT_OVERVIEW.md](./PROJECT_OVERVIEW.md)**: 🌟 **Start here** - Complete project navigation and summary
- **[PROJECT_REPORT.md](./PROJECT_REPORT.md)**: Comprehensive technical project report with implementation details
- **[API_DOCUMENTATION.md](./API_DOCUMENTATION.md)**: Complete API reference guide with code examples
- **[PERFORMANCE_METRICS.md](./PERFORMANCE_METRICS.md)**: Benchmarking, optimization, and performance analysis
- **[Live API Docs](http://13.60.69.48/docs)**: Interactive Swagger UI documentation for hands-on testing

### 🎓 Technologies Used
- **[scikit-learn](https://scikit-learn.org/)**: Machine learning library
- **[FastAPI](https://fastapi.tiangolo.com/)**: Modern Python web framework
- **[Docker](https://www.docker.com/)**: Containerization platform
- **[AWS EC2](https://aws.amazon.com/ec2/)**: Cloud computing service

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Sahar**
- 🎓 AI Master's Student (3rd Semester)
- 💼 Seeking Werkstudent opportunities in AI/ML
- 🌟 Passionate about cloud-native AI solutions

---

<div align="center">

**⭐ If this project helped you, please give it a star! ⭐**

</div>