from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)
@app.route('/')
def show_time():
    current_time = datetime.now()

    formated_date = current_time.strftime("%d/%m/%Y")
    formated_time = current_time.strftime("%H:%M:%S")
    weekdays = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота','Воскресенье']
    weekday = weekdays[current_time.weekday()]


    return render_template("index.html",
                           date=formated_date,
                           time=formated_time,
                           weekday=weekday)

if __name__ == "__main__":
    app.run()
