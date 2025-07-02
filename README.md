
# Airbnb Listing Price Prediction

## Overview

This project aims to predict the listing price of Airbnb properties using advanced machine learning techniques. The solution helps hosts estimate competitive prices for their listings based on property details and activity data.

---

## Dataset

* **Source:** Airbnb listings dataset
* **Size:** 447 rows, 16 columns after cleaning
* **Target variable:** `price` (transformed using log)

---

## Exploratory Data Analysis (EDA)

We performed a thorough EDA to understand data distribution and relationships:

* **Missing value treatment:**

  * Handled missing `price`, `last_review`, `reviews_per_month`
* **Feature distributions & outlier handling:**

  * Log transformation and capping on `price`
  * Filtered extreme `minimum_nights` (>30 nights)
* **Correlation analysis:**

  * No strong correlation with price; review metrics highly correlated among themselves
* **Feature engineering:**

  * `log_price`
  * `reviews_density` = reviews per month / availability
  * `price_per_min_night` = price / minimum nights
  * `is_professional_host` (binary)
  * `days_since_last_review`
  * `popularity_score`

---

## Feature Engineering

We engineered new features to capture useful patterns:

* **Log-transformed price** for stable modeling
* **Price per minimum night** as a relative cost indicator
* **Host professional flag** to separate large hosts
* **Review recency metrics**

---

## Modeling

We evaluated multiple regression models:

| Model             | RMSE     | R²       |
| ----------------- | -------- | -------- |
| Linear Regression | 0.33     | 0.43     |
| Decision Tree     | 0.32     | 0.47     |
| Random Forest     | 0.23     | 0.73     |
| Gradient Boosting | **0.17** | **0.85** |

We finally selected **Gradient Boosting Regressor** and fine-tuned using GridSearchCV, achieving:

* **Best Test RMSE:** 0.15
* **Best Test R²:** 0.89

---

## Deployment

The final model is exported along with its full preprocessing pipeline (including scaler and encoder).

### API

* Implemented using **FastAPI** to serve predictions.
* Supports JSON input and returns price prediction.

### Web App

* Built using **Streamlit**.
* Simple and interactive UI to input listing details and get predicted price.

---

## Containerization

* Entire app containerized using Docker.
* Streamlit app and API run in the same container for seamless deployment.

---

## Running Locally

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run FastAPI and Streamlit (entrypoint script)
python main.py
streamlit run streamlit_app.py
```

---

## Docker

Pull and run from Docker Hub:

```bash
docker pull batman21/airbnb-app:latest
docker run -p 8501:8501 batman21/airbnb-app
```

Then, visit:

* Streamlit app: [http://localhost:8501](http://localhost:8501)

---

## 🚀 Docker Image

[**Docker Hub Link**](https://hub.docker.com/r/batman21/airbnb-app)

---

## Author

Adarsh

---
