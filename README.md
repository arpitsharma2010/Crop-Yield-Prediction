Crop Yield Prediction Project
Overview
This repository contains the implementation of a crop yield prediction system, which uses machine learning models to predict the yield of crops in tons per hectare based on various environmental and cultivation factors. The project includes two main phases:

Here is the link to the dataset used for this project :-
https://www.kaggle.com/datasets/samuelotiattakorah/agriculture-crop-yield

Machine learning model development and validation using Python and popular data science libraries.
Integration with a Flask web application to allow users to interact with the model through a web interface.
Files
code_using_ml.ipynb: Machine learning implementation using Pandas, Scikit-learn, and Matplotlib for data visualization and model training.
code_using_spark.ipynb: Enhancement of the project using Apache Spark to handle larger datasets and improve processing efficiency.
app.py: Flask application that serves a web interface for the crop yield prediction model.
home.html, styles.css: Frontend files for the web application providing a user-friendly interface for data input and display of the prediction results.
Phase 1 and 2: Machine Learning Implementation
Description
These phases focus on:

Preprocessing the data to prepare it for machine learning.
Performing exploratory data analysis to uncover insights from the data.
Training and evaluating models such as Linear Regression, K-Nearest Neighbors, and Naive Bayes.
Technologies Used
Python
Pandas for data manipulation
Matplotlib and Seaborn for data visualization
Scikit-learn for building machine learning models
Phase 3: Apache Spark Implementation
Description
Leverages Apache Spark for:

Efficient data handling and processing of large datasets.
Utilizing Spark SQL and DataFrame API for data transformations and aggregations.
Integrating machine learning pipelines in a distributed environment.
Technologies Used
Apache Spark
PySpark
Flask Web Application
Description
The Flask app provides a web interface to interact with the machine learning model. Users can input parameters such as rainfall, temperature, crop type, soil type, and other factors to receive a prediction on crop yield.

Setup
Run pip install flask to install Flask.
Use python app.py to start the web server.
Open a web browser and go to http://127.0.0.1:5000/ to view the application.
Technologies Used
Flask for the web framework.
HTML/CSS for the frontend.
Getting Started
To set up and run the project:

Ensure Python is installed.
Install required libraries using pip install pandas matplotlib seaborn scikit-learn pyspark flask.
Follow instructions in the Flask Web Application section to launch the web interface.
Contribution
Contributions are welcome. Please open an issue first to discuss what you would like to change.

License
Distributed under the MIT License. See LICENSE for more information.
