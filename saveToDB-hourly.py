import bme280
from smbus2 import SMBus
import sqlite3
from datetime import datetime

#getting data
port = 1
address = 0x76
bus = SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)
data = bme280.sample(bus, address, calibration_params)
temperature = round(data.temperature, 2)
pressure = round(data.pressure, 1)
humidity = round(data.humidity, 1)

#print(data.timestamp)
#print(temperature)
#print(pressure)
#print(humidity)

time = datetime.now().strftime('%d.%m.%Y %H:%M')

#connecting to db
connection = sqlite3.connect('database.db')
connection.execute("PRAGMA journal_mode=WAL;")
cursor = connection.cursor()
checkExist = cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='temperature_hourly'").fetchall()
if checkExist == []:
    id = 1
else:
    currentid = cursor.execute("SELECT id FROM temperature_hourly ORDER BY id DESC").fetchone()
    id = currentid[0]+1
cursor.execute('CREATE TABLE IF NOT EXISTS temperature_hourly (id int, time text, temperature int, pressure int, humidity int)')
cursor.execute('INSERT INTO temperature_hourly (id, time, temperature, pressure, humidity) VALUES (?,?,?,?,?)', (id, time, temperature, pressure, humidity)) 
connection.commit()

test = cursor.execute('SELECT * FROM temperature_hourly')
for row in test:
    print(row)

# | @hourly | -- crontab

connection.close()
