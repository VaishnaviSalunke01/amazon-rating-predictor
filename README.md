# amazon-rating-predictor

# Amazon Saree Rating Predictor 🧵⭐

A Full-Stack Machine Learning application that predicts the expected customer rating of a saree based on its price and material type. 

**Live Demo:** https://amazon-saree-rating-predictor.netlify.app

## 🚀 Overview
This project demonstrates the end-to-end lifecycle of a Data Science product:
1. **Data Collection:** Scraped product data from Amazon using BeautifulSoup.
2. **Machine Learning:** Processed data and trained a Random Forest Regressor using Scikit-Learn.
3. **API Development:** Created a high-performance backend using FastAPI.
4. **Cloud Deployment:** Hosted the backend on Render and the frontend on Netlify.

## 🛠️ Tech Stack
- **Language:** Python 3.12
- **ML Libraries:** Pandas, Scikit-Learn, Joblib
- **Backend:** FastAPI, Uvicorn
- **Frontend:** HTML5, CSS3, JavaScript (Fetch API)
- **DevOps:** GitHub, Render (API), Netlify (Web)

## 📊 How it Works
The model was trained on a dataset of sarees, extracting key features from product titles:
- **Numerical Features:** Price (₹)
- **Categorical Features (One-Hot Encoded):** Cotton, Silk, Chiffon, Linen, Ready-to-Wear.

When a user enters a price and selects a material, the frontend sends a POST request to the FastAPI server. The server loads the `rating_predictor.pkl` model, processes the input, and returns a predicted rating out of 5.

## 📥 Installation & Local Setup

Follow these steps to run the project on your local machine for testing or development.

### **Step 1: Clone the Repository**
```bash
git clone [https://github.com/VaishnaviSalunke01/amazon-rating-predictor.git](https://github.com/VaishnaviSalunke01/amazon-rating-predictor.git)

### **Step 2: Create a Virtual Environment (venv)**
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

### **Step 3: Install Dependencies**
pip install -r requirements.txt

### **Step 4: Start the Backend Server**
uvicorn main:app --reload
