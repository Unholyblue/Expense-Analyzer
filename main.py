import argparse, csv, streamlit
from pathlib import Path
from datetime import datetime

file_path = Path("")

class ExpenseAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path

    def save_expense(self, x):
        with open(file_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date","Category","Description","Amount"])
            writer.writerows(x)

    def load_expense(self, x):
        if not file_path:
            return []
        with open(file_path, mode="r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)
            return list(reader)

    def creation_time():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
    def add_expense(self,x):
        expenses = self.load_expense()
        x = [self.creation_time()] + x
        expenses.append(x)
        self.save_expense(expenses)
        print("Expense added.")

    def delete_expense(self, x):
        expenses = self.load_expense()
        

    def edit_expense(self, x):
    def list_expense(self, x):

