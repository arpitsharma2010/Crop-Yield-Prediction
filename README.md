Crop Yield Prediction Project
Overview
This repository contains two phases of a crop yield prediction project, aimed at predicting the yield of crops in tons per hectare based on various environmental and cultivation factors. The project utilizes both traditional machine learning models and big data processing with Apache Spark to address scalability and performance optimization.
Here is the link to the dataset used for this project :-
https://www.kaggle.com/datasets/samuelotiattakorah/agriculture-crop-yield

Files
phase1and2.ipynb: Implements the preprocessing and machine learning models using Python libraries such as Pandas, Scikit-learn, and Matplotlib for data visualization.
phase3.ipynb: Implements the data processing and analytics using Apache Spark, enhancing the capability to handle large datasets efficiently.
Phase 1 and 2: Machine Learning Implementation
Description
In the initial phases, the project focuses on:

Data cleaning and preprocessing to prepare the dataset for model training.
Exploratory data analysis (EDA) to understand the dataset's characteristics.
Training machine learning models including Linear Regression, K-Nearest Neighbors, and Naive Bayes to predict crop yields.
Technologies Used
Python
Pandas for data manipulation
Matplotlib and Seaborn for data visualization
Scikit-learn for implementing machine learning models
Phase 3: Apache Spark Implementation
Description
To handle larger datasets and improve computational efficiency, the project scales up using Apache Spark:

Utilizes Spark SQL for data ingestion and preprocessing.
Employs Spark's DataFrame API to perform data transformations and aggregations efficiently.
Implements feature engineering and machine learning within the Spark ecosystem to ensure scalability.
Technologies Used
Apache Spark
PySpark for Spark's Python API
Spark SQL for data querying
Getting Started
To run these notebooks:

Ensure you have Python installed, along with Jupyter Notebooks or JupyterLab.
For phase1and2.ipynb, install the required Python packages using pip install pandas matplotlib seaborn scikit-learn.
For phase3.ipynb, Apache Spark needs to be set up along with PySpark. Follow the official Spark installation guide.
Contribution
Contributions are welcome. For major changes, please open an issue first to discuss what you would like to change.

License
Distributed under the MIT License. See LICENSE for more information.
