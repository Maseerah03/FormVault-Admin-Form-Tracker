# FormVault – Admin Request Tracker

FormVault is a full-stack internal tool for submitting and managing employee requests such as leave, travel reimbursements, or work-from-home approvals. It is built using Python Flask, HTML, Bootstrap, JavaScript, and SQLite. This project simulates real-world internal tools used in organizations to streamline operations.

## 📌 Features

- 📄 Internal request form with structured fields
- ✅ Frontend validation using JavaScript
- 🗃 Data persistence using SQLite (no external DB required)
- 📊 Admin dashboard with responsive Bootstrap table view
- 🔁 Organized code structure using Flask’s standard conventions

## 🚀 Technologies Used

| Layer     | Tech Stack                         |
|-----------|-------------------------------------|
| Frontend  | HTML5, Bootstrap 5, JavaScript      |
| Backend   | Python 3.11, Flask                  |
| Database  | SQLite3 (lightweight embedded DB)   |
| Tools     | Git, GitHub                         |


## 💡 How It Works

- User visits `/` to access the internal request form.
- JavaScript checks that all fields are filled properly.
- On submission, Flask captures the data and stores it in a SQLite database.
- The user is redirected to `/dashboard`, where all past submissions are listed in a styled table.

## 🔧 Installation and Run

### Prerequisites:
- Python 3.x
- Flask installed (via pip)

### Steps to Run:

```bash
# Step 1 – Install dependencies
pip install flask

# Step 2 – Run the application
python app.py

# Step 3 – Open in your browser
http://127.0.0.1:5000/
