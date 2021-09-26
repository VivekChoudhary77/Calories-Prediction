# Calories Burnt Prediction using Machine Learning Algorithm
## Machine learning algorithm used Random Forest Regressor

[Random Forest Regressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)

![](https://github.com/VivekChoudhary77/Calories-Prediction/blob/master/images/csv%20file.PNG)

- Takes 7 input values i.e. ***Gender,Age,Height,Weight,Duration,Heart Rate,Body Temprature.***

- Machine Learning algorithm used for regression task.

- A random forest is a meta estimator that fits a number of classifying decision trees on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting.

- n_estimators = 10 used.

- used pickle to dump the model for creating a .pkl file to be read by flask web application.

- used flask web framework for deploying the model locally.

- created a Landing page using frontend technologies HTML forms and for designing CSS.

- used HTML forms to take user input.

- after entering details in forms submit button routes the *predict* **METHOD** in the app.py i.e. flask web application 
---
### Landing Page
![](https://github.com/VivekChoudhary77/Calories-Prediction/blob/master/images/caloriesp1.PNG)

## One Hot Encoding
- One-hot Encoding is a type of vector representation in which all of the elements in a vector are 0, except for one, which has 1 as its value, where 1 represents a boolean specifying a category of the element.

[Understand One hot encoding](https://stackabuse.com/one-hot-encoding-in-python-with-pandas-and-scikit-learn/)

- used 0:Male (0 for male) 1:Female (1 for female)

| Before        | After         |
| ------------- |:-------------:|
| Female        | 1             |
| Male          | 0             |
---
### Before Prediction
![](https://github.com/VivekChoudhary77/Calories-Prediction/blob/master/images/caloriesp2.PNG)

---
### After Prediction
![](https://github.com/VivekChoudhary77/Calories-Prediction/blob/master/images/afterprediction.PNG)
