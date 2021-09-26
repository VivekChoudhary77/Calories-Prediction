from flask import Flask, request,jsonify, render_template
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template("ML.html")

@app.route("/predict", methods = ["POST"])
def predict():
    data1 = request.form.get("a")
    data2 = request.form.get("b")
    data3 = request.form.get("c")
    data4 = request.form.get("d")
    data5 = request.form.get("e")
    data6 = request.form.get("f")
    data7 = request.form.get("g")

    features_as_array = np.array([[data1, data2, data3, data4, data5, data6, data7]])
    prediction = model.predict(features_as_array)

    output = round(prediction[0], 2)

    return render_template("ML.html", prediction_text = "The Calories burnt for the entered details is {} kcal.".format(output))

if __name__ == '__main__':
    app.run(debug=True)
