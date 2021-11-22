
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
        print(request.form.get('review', ''))
        return render_template('index.html')

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=8080)
