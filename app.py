from flask import Flask, render_template, request
import requests
import os
import atexit

app = Flask(__name__)

ALPHA_VANTAGE_API_KEY = '3LJ2YNMNTEG8OVHB'  # Replace with your actual API key

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    current_price = None
    predicted_price = None
    if request.method == 'POST':
        stock_symbol = request.form['stock_symbol']
        prediction, current_price, predicted_price = predict(stock_symbol)
    return render_template('index.html', prediction=prediction, current_price=current_price, predicted_price=predicted_price)

def fetch_real_time_price(stock_symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock_symbol}&interval=1min&apikey={ALPHA_VANTAGE_API_KEY}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        latest_timestamp = max(data['Time Series (1min)'].keys())  # Get the latest timestamp
        latest_price = float(data['Time Series (1min)'][latest_timestamp]['4. close'])
        return latest_price
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None
    except (KeyError, ValueError) as e:
        print("Error parsing data:", e)
        return None

def predict(stock_symbol):
    current_price = fetch_real_time_price(stock_symbol)

    if current_price is None:
        return 'Error fetching data', None, None

    predicted_percentage_increase = 0.02  # 2% predicted increase (modify as needed)
    predicted_price = current_price * (1 + predicted_percentage_increase)

    prediction = 'Buy' if predicted_price > current_price else 'Sell'

    return prediction, current_price, predicted_price

def save_pid():
    pid_file = 'app.pid'
    with open(pid_file, 'w') as f:
        f.write(str(os.getpid()))

atexit.register(lambda: os.remove('app.pid') if os.path.exists('app.pid') else None)
save_pid()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Bind to all available network interfaces
