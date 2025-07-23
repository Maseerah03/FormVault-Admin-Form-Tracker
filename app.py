from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# ?? Database setup function
def init_db():
    conn = sqlite3.connect('formvault.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname TEXT NOT NULL,
            department TEXT NOT NULL,
            request_type TEXT NOT NULL,
            reason TEXT NOT NULL,
            date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# ?? Initialize the database when app starts
init_db()

# ?? Route 1: Serve the Form Page
@app.route('/')
def form():
    return render_template('form.html')

# ?? Route 2: Handle Form Submission
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        fullname = request.form.get('fullname')
        department = request.form.get('department')
        request_type = request.form.get('requestType')
        reason = request.form.get('reason')
        date = request.form.get('date')

        conn = sqlite3.connect('formvault.db')
        c = conn.cursor()
        c.execute('''
            INSERT INTO submissions (fullname, department, request_type, reason, date)
            VALUES (?, ?, ?, ?, ?)
        ''', (fullname, department, request_type, reason, date))
        conn.commit()
        conn.close()

        return redirect('/dashboard')

# ?? Route 3: Admin Dashboard to View Submissions
@app.route('/dashboard')
def dashboard():
    conn = sqlite3.connect('formvault.db')
    c = conn.cursor()
    c.execute('SELECT * FROM submissions ORDER BY id DESC')
    rows = c.fetchall()
    conn.close()
    return render_template('dashboard.html', submissions=rows)

# ?? Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
