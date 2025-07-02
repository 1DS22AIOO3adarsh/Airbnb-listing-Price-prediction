
# Airbnb Listing Price Prediction

## Overview

This project predicts Airbnb listing prices using advanced machine learning techniques. It helps hosts determine competitive prices for their properties based on listing attributes and activity data.

---

## Dataset

* **Source:** Airbnb listings dataset
* **Final size after cleaning:** 447 rows, 16 columns
* **Target variable:** `price` (log-transformed)

---

## Exploratory Data Analysis (EDA)

We performed a thorough EDA to understand data characteristics and guide feature engineering.

### Missing value treatment

* Handled missing values in `price`, `last_review`, `reviews_per_month`.

### Distribution analysis and outlier handling

* Applied log transformation on `price` to reduce skewness.
* Removed listings with `minimum_nights` > 30 to exclude extreme cases.

### Correlation analysis

* No strong linear correlation with `log_price`.
* Strong correlations among review-related metrics (`number_of_reviews`, `reviews_per_month`, `number_of_reviews_ltm`).

---

## Feature Engineering

New features were created to improve prediction performance:

* `log_price`: Log-transformed price for variance stabilization.
* `reviews_density`: Reviews per month normalized by availability.
* `price_per_min_night`: Price divided by minimum nights.
* `is_professional_host`: Flag indicating if a host manages more than 3 listings.
* `days_since_last_review`: Number of days since the most recent review.
* `popularity_score`: Composite score combining activity and recency.

---

## Modeling

Multiple regression models were evaluated:

| Model             | RMSE | R²   |
| ----------------- | ---- | ---- |
| Linear Regression | 0.33 | 0.43 |
| Decision Tree     | 0.32 | 0.47 |
| Random Forest     | 0.23 | 0.73 |
| Gradient Boosting | 0.17 | 0.85 |

### Final Model

* **Chosen model:** Gradient Boosting Regressor
* **Tuned using:** GridSearchCV
* **Best Test RMSE:** 0.15
* **Best Test R²:** 0.89

---

Deployment
Export
Complete preprocessing pipeline (including scaler, encoder, and engineered features) saved together with the model using joblib.

API
Built using FastAPI.

Accepts JSON payload and returns a predicted price.

Web App
Developed using Streamlit.

Interactive UI to input listing details and receive predicted prices.

Containerization
Full application containerized using Docker.

Streamlit app and FastAPI run inside the same container for seamless deployment.

Running Locally
bash
Copy
Edit
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run API
python main.py

# Run Streamlit app
streamlit run streamlit_app.py
Docker Usage
bash
Copy
Edit
docker pull batman21/airbnb-app:latest
docker run -p 8501:8501 batman21/airbnb-app
Then visit:

Streamlit app: http://localhost:8501

Deployment on Railway
The application is also deployed using Railway's Docker container service.

Running at: airbnb-app-production-5063.up.railway.app

Monitoring
Prometheus used to scrape metrics from the app endpoints.

Grafana configured to visualize real-time metrics (e.g., API response times, scrape duration, request errors).

Dockerized setup for Prometheus and Grafana to keep them portable and reproducible.

Docker Image
Docker Hub — batman21/airbnb-app

Author
Adarsh

