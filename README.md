**Overview**

This project aims to develop a machine learning based crop-prediction model to support farmers in making informed decisions about crop selection, 
planting, and harvesting. The model was trained on a large dataset of historical crop and weather data, using deep learning techniques. 
The results of the model showed high accuracy in predicting crop yield, surpassing the performance of traditional crop prediction methods. 
The model has been deployed with user-friendly interface, thus enabling farmers to input a few values and obtain informed decisions about when and what to plant. 
This project represents a significant step forward in using ML to improve the efficiency and profitability of agriculture.

**Data**

The data used to train the model was collected from the [Crop Prediction](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset) dataset. 
The dataset consists of 2200 samples of 22 different crops whose predictions are made using 7 features: nitrogen, phosphorus, potassium, and pH content of the soil, temperature, 
humidity and rainfall. The dataset is perfectly balanced, with each crop having 100 samples.

**Training**

The model was trained on the data with a 80:20 train-test split ratio. The objective(loss) function used was categorical crossentropy, and the optimizer used was ADAM. 
The performance metric used to evaluate the model is accuracy. Training was done for 100 epochs.

**Technologies Used**

Python: Programming language used for model development, data preprocessing, and web application development.
Scikit-learn: Machine learning library used for model training, evaluation, and prediction.
Pandas: Data manipulation library used for data preprocessing and analysis.
NumPy: Library for numerical computing used for handling arrays and mathematical operations.
Flask: Web framework used for building the user interface and handling HTTP requests.
HTML/CSS: Markup and styling languages used for designing the web interface.
JavaScript: Scripting language used for client-side interactions and enhancing the user interface.


install new version of scikit-learn  and numpy
#pip install scikit-learn==1.2.2

