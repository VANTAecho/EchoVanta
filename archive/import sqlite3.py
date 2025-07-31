import sqlite3
import pandas as pd

def detect_anomalies(threshold=50):
    conn = sqlite3.connect('data/logs.sqlite')
    df = pd.read_sql_query("SELECT * FROM processes ORDER BY timestamp DESC LIMIT 100", conn)
    high_cpu = df[df['cpu'] > threshold]
    if not high_cpu.empty:
        print("⚠️  High CPU processes:\n", high_cpu)

if __name__ == '__main__':
    detect_anomalies()
