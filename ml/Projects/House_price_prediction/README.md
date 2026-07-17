# 🏠 House Price Prediction

# live: 
https://qspider-h899gsjyaqs6sl49icfzbv.streamlit.app/

A Machine Learning web application built with **Streamlit** that predicts Bangalore house prices based on user inputs like location, total square feet, number of bathrooms, and BHK.

## 🚀 Features

* Predicts house prices using a trained Machine Learning model
* User-friendly Streamlit interface
* Location-based price prediction
* Real-time predictions

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* Scikit-learn
* Joblib

## 📂 Project Structure

```
House_price_prediction/
│
├── app.py
├── notebook/
│   └── rf_model.joblib
├── dataset/
│   └── Cleaned_bangloreHousePrice_df.csv
└── House_logo.png
```

## ▶️ Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## 📌 Input Features

* Location
* Total Square Feet
* Number of Bathrooms
* Number of Bedrooms (BHK)

## 📈 Output

The application displays the estimated house price based on the entered details.
