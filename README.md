# Crop Yield Prediction Project

## Overview
This repository contains the implementation of a **Crop Yield Prediction System**, which leverages **machine learning** to predict crop yield (in tons per hectare) based on various environmental and cultivation factors. The project consists of three main phases:

1. **Machine Learning Model Development & Validation**  
   - Utilizes **Python** and popular data science libraries for model training and evaluation.
   
2. **Apache Spark Implementation**  
   - Enhances scalability by leveraging **Apache Spark** for handling large datasets.

3. **Flask Web Application**  
   - Provides an interactive web interface for users to input data and receive crop yield predictions.

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-MLlib-orange)
![Flask](https://img.shields.io/badge/Flask-WebApp-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

### Dataset  
The dataset used in this project can be accessed at:  
[📂 Kaggle Dataset - Agriculture Crop Yield](https://www.kaggle.com/datasets/samuelotiattakorah/agriculture-crop-yield)

---

## 📂 Project Files  

| File Name                | Description  |
|-------------------------|-------------|
| `code_using_ml.ipynb`  | Machine learning implementation using Pandas, Scikit-learn, and Matplotlib for data visualization and model training. |
| `code_using_spark.ipynb`  | Apache Spark implementation for handling large datasets efficiently. |
| `app.py`  | Flask web application that serves a user-friendly interface for crop yield prediction. |
| `home.html` & `styles.css`  | Frontend files for the web application. |

---

## 🔹 Phase 1 & 2: Machine Learning Implementation

### **Description**
These phases focus on:
- **Data Preprocessing**: Cleaning and preparing data for model training.
- **Exploratory Data Analysis (EDA)**: Understanding the dataset through visualizations.
- **Model Training & Evaluation**: Implemented and compared **Linear Regression, K-Nearest Neighbors (KNN), Naive Bayes, Decision Tree, Random Forest, ElasticNet, and XGBoost** for crop yield prediction.

### **Technologies Used**
- **Python**
- **Pandas** – Data manipulation
- **Matplotlib & Seaborn** – Data visualization
- **Scikit-learn** – Machine learning model development

---

## 🔹 Phase 3: Apache Spark Implementation

### **Description**
This phase enhances data processing efficiency using **Apache Spark** to:
- Handle large datasets efficiently.
- Use **Spark SQL & DataFrame API** for transformations and aggregations.
- Implement **machine learning pipelines** in a distributed computing environment.

### **Technologies Used**
- **Apache Spark**
- **PySpark** (Python API for Spark)

---

## 🌐 Flask Web Application  

### **Description**
The **Flask app** provides an interactive web interface where users can input parameters (e.g., **rainfall, temperature, crop type, soil type**) to get a **crop yield prediction**.

### **Setup & Execution**
1. Install Flask:
   ``` cmd
   pip install flask
   ```
2. Run the Flask app:
   ``` cmd
   python app.py
   ```
3. Open a web browser and visit:
   ``` url
   http://127.0.0.1:5000/
   ```

### **Technologies Used**
- **Flask** – Web framework
- **HTML/CSS** – Frontend UI

---

## 🚀 Getting Started  

### **Prerequisites**
Ensure **Python** is installed on your system.

### **Installation**
Install required dependencies:
``` cmd
pip install pandas matplotlib seaborn scikit-learn pyspark flask
```

### **Running the Project**
1. Train the machine learning model using `code_using_ml.ipynb`.
2. (Optional) Use `code_using_spark.ipynb` for large-scale data processing.
3. Download the trained model from the link below and place it in the project directory:
   ``` url
   https://drive.google.com/drive/folders/1Fxqluo2iR2CVvoqogZqUTfcZmMlomgwW
   ```
4. Unzip the folder and place the unzipped file at the root folder.
5. Run `app.py` to start the **Flask web application**.

---

## 🤝 Contribution  
Contributions are welcome!  
- If you'd like to improve this project, please **open an issue** first to discuss changes.
- Fork the repository and create a **pull request** with your changes.

---

## 📜 License  
Distributed under the **MIT License**. See the `LICENSE` file for more details.

---

This **README** provides a structured overview of the **Crop Yield Prediction Project**, including its features, setup, and usage instructions. 🚀 Happy coding!
