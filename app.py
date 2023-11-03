import pickle
import numpy as np
from flask import Flask, request, render_template


app = Flask(__name__)

# Predective function
def BrestCancerPredection(input_data):

    model_path = "./model/brestcanser.pkl"

    print(model_path)
    input_array_shape = np.asarray(input_data).reshape(1, -1)

    with open(model_path, "rb") as file:
        clf = pickle.load(file)
    result = clf.predict(input_array_shape)
    return result[0]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the floating-point values from the form
        values = []

        for i in range(0, 31):
            field_name = f'value{i}'
            if field_name in request.form:
                try:
                    value = float(request.form[field_name])
                    print(field_name, "  " , value)
                    values.append(value)
                except ValueError:
                    return "Invalid input. All values must be floating-point numbers."

        # values_tuple = tuple(values)
        # print(values)
        output = BrestCancerPredection(values)

        if output == 0:
            result = "Brest cancer type: MALIGNANT"
        else:
            result = "Brest cancer type: BENIGN"

        return render_template('result.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False)