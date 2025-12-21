# 🏠 South Jakarta House Predictor

This repository contains a Machine Learning-based web application designed to predict house prices in the South Jakarta area. Built using Flask, the application integrates a trained Voting Regressor model to provide accurate price estimations based on property specifications and location.

---

## 🧠 Features

- House Price Prediction: Utilizes a Voting Regressor model combining Random Forest, Gradient Boosting, and XGBoost for accurate predictions.
- Easy-to-Use Interface: Simple web interface for users to input property details and receive price estimates.
- Data Preprocessing: Handles text and numerical data effectively to ensure model accuracy.
- Model Training: Includes Jupyter notebooks for data exploration, preprocessing, model training, and evaluation.
- Responsive Design: Built with Bootstrap for a clean and user-friendly experience.

---

## 🛠️ Tech Stack
- **Python**
- **Flask**
- **scikit-learn**
- **Pandas**
- **NumPy**
- **Bootstrap 5**
- **Jupyter Notebooks**
- **JavaScript**

---

## 📁 Project Structure

```
south-jakarta-house-prediction-webapp/
│
├── artifacts/              # Trained ML models and preprocessors
│   ├── scaler.pkl          # Scaler object for normalization
│   ├── vectorizer.pkl      # Vectorizer for text features
│   └── voting_regressor.pkl # The main trained model
│
├── data/
│   └── DATA RUMAH.xlsx     # Raw dataset source
│
├── notebooks/              # Data Science workspace
│   ├── eda.ipynb           # Exploratory Data Analysis notebook
│   └── model.ipynb         # Model training and evaluation notebook
│
├── services/               # Backend logic modules
│   ├── __init__.py
│   ├── predictor.py        # Logic to load model and predict
│   └── preprocessing.py    # Logic to clean and prepare user input
│
├── static/                 # Static assets
│   ├── css/
│   │   └── style.css       # Custom styling (Glassmorphism, etc.)
│   └── js/
│       └── script.js       # Frontend logic (Sliders, API calls)
│
├── templates/              # HTML Templates (Jinja2)
│   ├── base.html           # Base layout
│   ├── index.html          # Landing page
│   ├── predict.html        # Prediction form
│   └── result.html         # Prediction result page
│
├── app.py                  # Main application entry point
├── requirements.txt        # Python dependencies list
├── .gitignore
└── README.md
```

---

## 🔁 Machine Learning Workflow
1. **Data Collection**: The dataset "DATA RUMAH.xlsx" contains various features of houses in South Jakarta.
2. **Exploratory Data Analysis (EDA)**: Conducted in `eda.ipynb` to understand data distributions and relationships.
3. **Data Preprocessing**: Handled in `eda.ipynb` and `preprocessing.py` to clean and transform data for modeling.
4. **Model Training**: Experiments with different algorithms in `model.ipynb`, leading to the selection of a Voting Regressor.
5. **Model Evaluation**: Performance metrics such as MAE, RMSE, and R² are calculated to assess model accuracy.
6. **Model Deployment**: The trained model and preprocessors are saved in the `artifacts/` directory and integrated into the Flask app for real-time predictions.

---

## 📂 Dataset & Credits

The dataset used in this project was sourced from Kaggle.  
You can access the original dataset and description through the link below:

🔗[Daftar Harga Rumah](https://www.kaggle.com/datasets/wisnuanggara/daftar-harga-rumah/data)

We would like to acknowledge and thank the dataset creator for making this resource publicly available for research and educational use.

---

## 🚀 How to Run

To run this project on your local machine, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/abidalfrz/south-jakarta-house-prediction-webapp.git

```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # On Linux/macOS
venv\Scripts\activate.bat     # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
# Run the Flask application
python app.py

# The API will be accessible at http://localhost:5000
```

### 5. Access the Application
Open your web browser and navigate to `http://localhost:5000` to access the Smart Expense Tracker application.

1. Click on "Start Prediction".
2. Fill in the property details in the form.
3. Click "Calculate" to get the predicted house price!

---
