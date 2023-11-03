# Predict Type of the Breast Cancer using Flask

In this section, we have used a simple LoggisticRegression to diagnose the breast cancer.

Create model (pkl) file and call the pkl file to predict the cancer


```
def BrestCancerPredection(input_data):
```


Creating the flask API

```
app = Flask("__name__")
```


Collect the data from the html and return the result.
```
@app.route('/', methods=['GET', 'POST'])
def index():
        return render_template('result.html', result=result)
    return render_template('index.html')

```

The run() method of Flask class runs the application on the local development server.
```
app.run()
```


Yay, our first model is ready, let’s test our bot.
The above given Python script is executed from Python shell.

Go to Anaconda Prompt, and run the below query.
```
python app.py
```


Below message in Python shell is seen, which indicates that our App is now hosted at http://127.0.0.1:5000/ or localhost:5000
```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
