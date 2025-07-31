import psutil
import time
import sqlite3

def log_top_processes():
    conn = sqlite3.connect('data/logs.sqlite')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS processes (timestamp TEXT, pid INTEGER, name TEXT, cpu REAL)''')

    while True:
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
            try:
                c.execute("INSERT INTO processes VALUES (datetime('now'), ?, ?, ?)",
                          (proc.info['pid'], proc.info['name'], proc.info['cpu_percent']))
            except Exception:
                continue
        conn.commit()
        time.sleep(10)

if __name__ == '__main__':
    log_top_processes()
