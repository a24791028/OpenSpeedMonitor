from flask import Flask, render_template
import speedtest
import sqlite3
from datetime import datetime

app = Flask(__name__)

def log_speed():
    st = speedtest.Speedtest()
    download = st.download() / 1e6  # 转换为Mbps
    upload = st.upload() / 1e6
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 保存到数据库
    conn = sqlite3.connect('speed.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS speeds (timestamp TEXT, download REAL, upload REAL)')
    c.execute('INSERT INTO speeds VALUES (?, ?, ?)', (timestamp, download, upload))
    conn.commit()
    conn.close()

@app.route('/')
def dashboard():
    conn = sqlite3.connect('speed.db')
    c = conn.cursor()
    data = c.execute('SELECT * FROM speeds ORDER BY timestamp DESC LIMIT 10').fetchall()
    conn.close()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    log_speed()  # 每次运行检测一次速度
    app.run(debug=True)
