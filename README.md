📊 Personal Expense Tracker (Python)

A command-line-based Expense Tracker built with Python that helps users record, view, and analyze their daily expenses.
It stores data in a CSV file and provides visual insights with pie charts using Matplotlib.

✨ Features

✅ Add Expenses – Record daily spending across multiple categories (Food, Travel, Shopping, Health, Other Bills)
✅ View All Records – See a clean, formatted table of all saved expenses
✅ Calculate Totals – Quickly view total spending across categories
✅ Date-Wise Search – View expenses on a specific date
✅ Month-Wise Filter – Analyze monthly spending trends (MM-YYYY format)
✅ Pie Chart Visualization – Visualize spending distribution using Matplotlib

🛠 Tech Stack

Language: Python

Libraries: csv, datetime, os, matplotlib

Data Storage: CSV File

📂 Project Structure
Expense_Tracker/
│
├── data.csv               # Stores expense data
├── expense_tracker.py     # Main Python program
├── assets/                # Folder for screenshots
│   └── pie_chart.png
└── README.md
📸 Screenshots

Pie Chart Visualization
![Pie Chart]("D:\expense_tracker_project\assets\Figure_1.png")
![Pie Chart]("D:\expense_tracker_project\assets\Figure_2.png")

🚀 How to Run

Follow these steps to set up and run the project on your machine:

1️⃣ Clone the repository

git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker


2️⃣ Install dependencies
Make sure you have Matplotlib installed:

pip install matplotlib


3️⃣ Run the project

python expense_tracker.py

📈 Future Improvements

🔹 Build a GUI using Tkinter or PyQt
🔹 Use SQLite/MySQL for better data management
🔹 Add monthly/yearly expense reports in PDF format
🔹 Support for multiple users with login feature

🎯 Why I Built This Project

I created this project to practice Python file handling, CSV operations, and data visualization.
It also helped me learn how to make a complete project from scratch — from coding and structuring files to generating insights using Matplotlib.


