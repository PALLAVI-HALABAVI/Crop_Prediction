from flask import Flask, request, render_template, redirect, url_for, session
import numpy as np
import pickle


# Load the model and scalers
model = pickle.load(open('model.pkl', 'rb'))
sc = pickle.load(open('standscaler.pkl', 'rb'))
ms = pickle.load(open('minmaxscaler.pkl', 'rb'))

# Create Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy credentials
USERNAME = 'admin'
PASSWORD = 'cse@123'

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('predict'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            session['username'] = username
            return redirect(url_for('predict'))
        else:
            return 'Invalid credentials, please try again.'
    return render_template('login.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        try:
            N = int(request.form['Nitrogen'])
            P = int(request.form['Phosporus'])
            K = int(request.form['Potassium'])
            temp = float(request.form['Temperature'])
            humidity = float(request.form['Humidity'])
            ph = float(request.form['Ph'])
            rainfall = float(request.form['Rainfall'])
        except ValueError:
            return render_template('predict.html', result="Invalid input values. Please enter numeric values.")

        feature_list = [N, P, K, temp, humidity, ph, rainfall]
        single_pred = np.array(feature_list).reshape(1, -1)

        try:
            scaled_features = ms.transform(single_pred)
            final_features = sc.transform(scaled_features)
            prediction = model.predict(final_features)
        except Exception as e:
            return render_template('predict.html', result=f"An error occurred during prediction: {e}")

        crop_dict = {
            1: {"crop": "Rice", "image": "rice.jpg"},
            2: {"crop": "Maize", "image": "maize.jpg"},
            3: {"crop": "Jute", "image": "jute.jpg"},
            4: {"crop": "Cotton", "image": "cotton.jpg"},
            5: {"crop": "Coconut", "image": "coconut.jpg"},
            6: {"crop": "Papaya", "image": "papaya.jpg"},
            7: {"crop": "Orange", "image": "orange.jpg"},
            8: {"crop": "Apple", "image": "apple.jpg"},
            9: {"crop": "Muskmelon", "image": "muskmelon.jpg"},
            10: {"crop": "Watermelon", "image": "watermelon.jpg"},
            11: {"crop": "Grapes", "image": "grapes.jpg"},
            12: {"crop": "Mango", "image": "mango.jpg"},
            13: {"crop": "Banana", "image": "banana.jpg"},
            14: {"crop": "Pomegranate", "image": "pomegranate.jpg"},
            15: {"crop": "Lentil", "image": "lentil.jpg"},
            16: {"crop": "Blackgram", "image": "blackgram.jpg"},
            17: {"crop": "Mungbean", "image": "mungbean.jpg"},
            18: {"crop": "Mothbeans", "image": "mothbeans.jpg"},
            19: {"crop": "Pigeonpeas", "image": "pigeonpeas.jpg"},
            20: {"crop": "Kidneybeans", "image": "kidneybeans.jpg"},
            21: {"crop": "Chickpea", "image": "chickpea.jpg"},
            22: {"crop": "Coffee", "image": "coffee.jpg"}
        }

        if prediction[0] in crop_dict:
            crop_info = crop_dict[prediction[0]]
            crop = crop_info["crop"]
            result = "{} is the best crop to be cultivated right there".format(crop)
            image_file = crop_info["image"]
        else:
            result = "Sorry, we could not determine the best crop to be cultivated with the provided data."
            image_file = "crops.jpg"

        return redirect(url_for('result', result=result, image_file=image_file))
    return render_template('predict.html')

@app.route('/result')
def result():
    result = request.args.get('result')
    image_file = request.args.get('image_file')
    return render_template('result.html', result=result, image_file=image_file)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)


#pip install skicit-learn==1.2.2
