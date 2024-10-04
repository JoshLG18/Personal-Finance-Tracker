from datetime import datetime

dateformat = "%d/%m/%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}

def get_date(prompt, allow_default=False):
    date_string = input(prompt)
    if allow_default and not date_string:
        return datetime.today().strftime(dateformat)
    try:
        valid_date = datetime.strptime(date_string,dateformat)
        return valid_date.strftime(dateformat)
    except ValueError:
        print("Invalid Date Format. Please enter the data in dd/mm/yyyy format")
        return get_date(prompt, allow_default)


def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()


def get_category():
    category = input("Enter the category ('I' for Income or 'E' for Expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    else:
        print("Invalid category. Please enter 'I' for Income or 'E' for Expense")
        return get_category


def get_description():
    return input("Enter a description (optional)")
