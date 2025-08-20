# Cloud-Native AI Model Deployment: Sentiment Analysis API

This project demonstrates the end-to-end process of training a machine learning model, wrapping it in a web API, containerizing it with Docker, and deploying it to a live cloud server on AWS EC2.

The application is a sentiment analysis service that classifies movie reviews as either positive or negative.

---

## 🚀 Live Demo

The API is running live on an AWS EC2 instance and is publicly accessible.

* **Public URL**: http://13.60.69.48
* **Interactive Docs (Swagger UI)**: http://13.60.69.48/docs

---

## 🛠️ Technology Stack

* **Machine Learning**: Scikit-learn, Pandas
* **Web Framework**: FastAPI
* **Containerization**: Docker
* **Cloud Platform**: AWS EC2 (Ubuntu)

---

## Usage

You can interact with the API using the interactive docs page or by sending a `POST` request to the `/predict/` endpoint.

#### Example using `curl`

```bash
curl -X 'POST' \
  '[http://13.60.69.48/predict/](http://13.60.69.48/predict/)' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "text": "This movie was absolutely fantastic and the acting was superb!"
  }'
  ```



## Expected Response
```bash

{
  "sentiment": "positive"
}
  ```
---

## ⚙️ Local Setup and Deployment

Instructions for setting up and running this project locally or deploying it yourself.

### 1. Prerequisites

* Python 3.8+
* Docker
* An AWS Account

### 2. Clone the Repository

```bash
git clone [https://github.com/YOUR_USERNAME/sentiment-api.git](https://github.com/YOUR_USERNAME/sentiment-api.git)
cd sentiment-api
```


### 3. Get the Data

This model was trained on the IMDb Movie Reviews Dataset from Kaggle.

Download the data here: https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews

After downloading, place the IMDB Dataset.csv file in the root of the project directory.

### 4. Build and Run with Docker (Recommended)
This is the easiest way to run the application, as it works exactly the same as the production deployment.

```bash
# Build the Docker image
docker build -t sentiment-api .

# Run the container
docker run -p 8080:80 sentiment-api
```

# Build the Docker image

```bash
docker build -t sentiment-api .
```

# Run the container

```bash
docker run -p 8080:80 sentiment-api
```
The application will be available at http://localhost:8080.