
# 🛃 Customer Segmentation using K-Means Clustering

## live
https://qspider-39nejqpy3rzpsy8ysdivqq.streamlit.app/

A Machine Learning web application built with **Streamlit** that performs customer segmentation using the **K-Means Clustering algorithm**. The application groups customers based on selected features and helps identify different customer segments.

## 🚀 Features

* Upload customer dataset in CSV format
* Select features for clustering
* Automatic data preprocessing
* Finds optimal number of clusters using the **Elbow Method**
* Performs K-Means clustering
* Visualizes customer segments using scatter plots

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* Scikit-learn
* K-Means Clustering
* Kneed

## 📂 Project Structure

```text
Customer_Segmentation/
│
├── app.py
├── requirements.txt
└── README.md
```

## ▶️ Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## 📌 How It Works

1. Upload a customer dataset (`.csv`)
2. Select the features required for clustering
3. The application preprocesses categorical data
4. The Elbow Method determines the optimal cluster count
5. K-Means algorithm assigns customers into clusters
6. Customer groups are visualized on a scatter chart

## 📊 Example Features

Common customer segmentation features:

* Annual Income
* Spending Score
* Age
* Other customer attributes

## 📈 Output

The application provides:

* Elbow curve for selecting optimal clusters
* Cluster labels for customers
* Interactive visualization of customer segments


