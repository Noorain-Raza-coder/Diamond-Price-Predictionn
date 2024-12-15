from flask import Flask , render_template , request
from src.pipelines.prediction_pipeline import CustomData , PredictionPipeline




app = Flask(__name__)

@app.route('/')
def HomePage():
    return render_template("home.html")

@app.route('/predict' , methods = ['POST'])
def predict():

    custom_data_obj = CustomData(carat = float(request.form['carat']),
                                depth = float(request.form['depth']),
                                table = float(request.form['table']),
                                x = float(request.form['x']),
                                y = float(request.form['y']),
                                z = float(request.form['z']),
                                cut = request.form['cut'],
                                color = request.form['color'],
                                clarity = request.form['clarity'] )

    df = custom_data_obj.get_Data_as_dataFrame()

    print("Data Received\n")
    print(df)

    pred_obj = PredictionPipeline()
    prediction = pred_obj.initiate_prediction_pipeline(df)
    final_prediction = round(prediction[0] , 2)

    return render_template("home.html" , prediction = final_prediction) 



if __name__ == '__main__':
    app.run(host='0.0.0.0' , debug=True)