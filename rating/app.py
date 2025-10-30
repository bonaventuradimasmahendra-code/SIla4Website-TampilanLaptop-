from flask import Flask, render_template, request, redirect, url_for
import main as logic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    items = logic.fetch_items()
    return render_template('data.html', items=items)

@app.route('/statistik')
def statistik():
    try:
        items = logic.fetch_items()
        logic.statistic(items)
        listrating = [i[2] for i in items]
        average = sum(listrating)/len(listrating) if listrating else 0
        highest = max(listrating) if listrating else 0
        lowest = min(listrating) if listrating else 0
        return render_template('statistic.html', average=average, highest=highest, lowest=lowest)
    except ZeroDivisionError:
        return render_template('zero.html', listrating=0), 500

@app.route('/add', methods=['POST'])
def add():
    nama = request.form['nama'].capitalize()
    rating = int(request.form['rating'])
    kritik = request.form['kritik']

    logic.cursor.execute("INSERT INTO rating_pengguna (nama, rating, kritik_saran) VALUES (%s, %s, %s)", (nama, rating, kritik))
    logic.db.commit()
    return redirect(url_for('data'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
