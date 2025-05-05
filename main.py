from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def getDB():
    connection = sqlite3.connect('database.db', check_same_thread=False)
    connection.execute("PRAGMA journal_mode=WAL;")
    cursor = connection.cursor()
    data = cursor.execute('SELECT * FROM temperature ORDER BY id DESC').fetchone()
    return data

@app.route('/')
def index():
    data = getDB()
    return render_template('index.html', date=data[1], temp=data[2], press=data[3], hum=data[4])

@app.route('/api/get1h')
def get1h():
    connection = sqlite3.connect('database.db', check_same_thread=False)
    connection.execute("PRAGMA journal_mode=WAL;")
    cursor = connection.cursor()
    data = cursor.execute('SELECT * FROM temperature ORDER BY id DESC').fetchall()
    give = []
    i = 0 
    for row in data:
        i+=1
        give.append(row)
        if i == 4:
            break
    return give
    

if __name__ == '__main__':
    #print(test)
    app.run(debug=True,port=1111,host='0.0.0.0')
