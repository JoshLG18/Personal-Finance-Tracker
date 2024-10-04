This Personal Finance Tracker is a Python application designed to help users track and manage their personal finances efficiently. 
It allows users to enter transactions (with dates, amounts, categories, and descriptions) and retrieve records based on a date range. 
The application also calculates total income and expenses within the specified range, helping users maintain better control of their financial habits.

**Features

Add new financial entries: Easily add records of income and expenses with relevant details like date, category, amount, and description.
View transaction history: Retrieve transactions based on a specified date range.
Summarize transactions: Automatically calculates total income and expenses within the filtered date range.
CSV-based storage: All data is stored in a CSV file, which can be easily exported or modified outside the application.

**Project Files

**main.py
Handles the core functionality of the application.
Reads and writes transaction data to a CSV file (finance_data.csv).
Filters transactions based on a user-defined date range.
Displays total income and expense summary.

**data_entry.py
Provides utility functions for capturing user input, such as amount, category, date, and description.
These functions are utilized in main.py to facilitate interaction with the user.
