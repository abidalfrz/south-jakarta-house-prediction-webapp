from flask import Flask, render_template, redirect, url_for, request, flash
import pandas as pd
import numpy as np
from services.preprocessing import preprocess_data
from services.predictor import predictor

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            data = {
                'nama_rumah': request.form['nama_rumah'],
                'luas_bangunan': int(request.form['luas_bangunan']),
                'luas_tanah': int(request.form['luas_tanah']),
                'kamar_tidur': int(request.form['kamar_tidur']),
                'kamar_mandi': int(request.form['kamar_mandi']),
                'garasi': int(request.form['garasi']),
            }

            df = pd.DataFrame([data])
            X = preprocess_data(df)
            prediction = predictor.predict(X)[0]
            prediction = np.expm1(prediction)  # Inverse of log1p transformation
            flash('Prediction successful!', 'success')
            return render_template('result.html', price=prediction)
        except Exception as e:
            flash(f'Error occurred: {str(e)}', 'error')
            return redirect(url_for('home'))
    return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug=True)
