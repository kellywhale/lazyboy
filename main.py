from flask import Flask, render_template, request
from notification import NotificationManager
import datetime

app = Flask(__name__)


year = datetime.datetime.now().year


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.form
        print(data["yourName"])
        costumer_care = NotificationManager()
        costumer_care.send_email(data["yourName"], data["yourEmail"], data["yourMessage"])
        return render_template('index.html', current_year=year, mgs_sent=True)

    return render_template('index.html',  current_year=year, mgs_sent=False)




if __name__ == "__main__":
    app.run(debug=True)