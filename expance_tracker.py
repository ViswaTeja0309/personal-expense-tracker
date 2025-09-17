import datetime as d
import csv as c
import os
import matplotlib.pyplot as plt

# Function to safely take integer input
def error(n):
    while True:
        try:
            return int(input(n))
        except ValueError:
            print("Please Enter a Valid Number !")

# Function to load data from CSV
def load_data():
    with open("data.csv", "r") as f:
        r = c.reader(f)
        header = next(r)  # skip header
        return list(r)

# Function to filter expenses based on month (MM-YYYY)
def month_expenses(month):
    data = load_data()
    return [row for row in data if row[0][5:7] + "-" + row[0][:4] == month]

# Function to draw a pie chart for a given month
def pie_chart(month):
    expenses_data = month_expenses(month)
    if not expenses_data:
        print(f"No data found for {month}")
    else:
        expenses_row = {"FOOD": 0, "TRAVEL": 0, "SHOPPING": 0, "HEALTH": 0, "OTHER_BILLS": 0}
        for rows in expenses_data:
            expenses_row["FOOD"] += int(rows[1])
            expenses_row["TRAVEL"] += int(rows[2])
            expenses_row["SHOPPING"] += int(rows[3])
            expenses_row["HEALTH"] += int(rows[4])
            expenses_row["OTHER_BILLS"] += int(rows[5])
        if sum(expenses_row.values()) == 0:
            print(f"No expenses found in {month}")
        else:
            labels = list(expenses_row.keys())
            sizes = list(expenses_row.values())
            colors = ["Green", "yellow", "Blue", "Red", "purple"]
            explode = [0.1, 0, 0, 0, 0]  # explode first slice
            plt.pie(sizes, labels=labels, colors=colors, explode=explode,
                    autopct='%1.1f%%', startangle=90, shadow=True)
            plt.title(f"Expenses on {month}")
            plt.axis('equal')
            plt.show()

# Function to calculate total expenses from file
def total():
    ttl = {"FOOD": 0, "TRAVEL": 0, "SHOPPING": 0, "HEALTH": 0, "OTHER_BILLS": 0}

    with open("data.csv", "r") as f:
        r = c.reader(f)
        next(r)  # skip header
        for i in r:
            ttl["FOOD"] += int(i[1])
            ttl["TRAVEL"] += int(i[2])
            ttl["SHOPPING"] += int(i[3])
            ttl["HEALTH"] += int(i[4])
            ttl["OTHER_BILLS"] += int(i[5])
    return ttl

# Create CSV file with header if not exists
if not os.path.exists("data.csv"):
    with open("data.csv", "w", newline="") as f:
        w = c.writer(f)
        w.writerow(["DATE", "FOOD", "TRAVEL", "SHOPPING", "HEALTH", "OTHER_BILLS"])

while True:

    print("\n___SELECT ONE FROM BELOW WHAT YOU WANT___")
    print("\n1.ADD EXPESCES")
    print("2.VIEW EXPANSES")
    print("3.VIEW TOTAL")
    print("4.VIEW EXPENSES ON PARTICULAR_DATE")
    print("5.VIEW EXPENSES ON PIE_CHART")
    print("6..EXIT")

    n = input("select one frome above:")

    if n == "1":
        # Take user input and add expenses to file
        FOOD = error("enter you spent on food:")
        TRAVEL = error("enter you spent on travel:")
        SHOPPING = error("enter  spent on shopping:")
        HEALTH = error("enter you spent on health:")
        OTHER_BILLS = error("enter you spent on others_bills:")
        today = d.date.today()

        with open("data.csv", "a", newline="") as f:
            w = c.writer(f)
            w.writerow([today, FOOD, TRAVEL, SHOPPING, HEALTH, OTHER_BILLS])

        print("Expenses Added Successfully!")

    elif n == "2":
        # Display all expenses from file
        print("\n_YOUR EXPENSES ARE_")
        with open("data.csv", "r") as f:
            r = c.reader(f)
            header = next(r)
            print(f"{header[0]:<12}{header[1]:<8}{header[2]:<8}{header[3]:<10}{header[4]:<8}{header[5]:<12}")
            print("-" * 60)
            for row in r:
                print(f"{row[0]:<12}{row[1]:<8}{row[2]:<8}{row[3]:<10}{row[4]:<8}{row[5]:<12}")

    elif n == "3":
        # Show total expenses
        print("\n__YOUR TOTAL EXPENSES__")
        TOTAL = total()
        for i, j in TOTAL.items():
            print(f"{i} : {j}")
        print(f"THE TOTAL EXPENSES ARE :- {sum(TOTAL.values())}Rs. SPENT ON :- {d.date.today().strftime('%d-%m-%Y')}")

    elif n == "4":
        # View expenses on a particular date (with input validation)
        print("\n___YOUR EXPENSES ON PARTICULAR_DATE___")
        while True:
            date_input = input("Enter date (YYYY-MM-DD): ")
            try:
                d.datetime.strptime(date_input, "%Y-%m-%d")  # validate format
                break
            except ValueError:
                print("Invalid date format! Please enter in YYYY-MM-DD format!")

        with open("data.csv", "r") as f:
            r = c.reader(f)
            header = next(r)
            print("Expenses On :", date_input)
            print(f'{header[0]:<5}{header[1]:<8}{header[2]:<8}{header[3]:<5}{header[4]:<5}{header[5]:<8}')
            print("-" * 60)
            for k in r:
                if k[0] == date_input:
                    print(f'{k[0]:<5}{k[1]:<8}{k[2]:<8}{k[3]:<5}{k[4]:<5}{k[5]:<8}')

    elif n == "5":
        print("\n---VISUAL_EXPENCES---")
        print("\n1.want particular month_expenses in pie_chart")
        print("2.want expenses of today in pie_chart")
        user_input = input("\nenter any one from above list:-")
        if user_input == "1":
            while True:
                month = input("Enter month and year (MM-YYYY): ")
                try:
                    d.datetime.strptime(month, "%m-%Y")  # validate month-year format
                    break
                except ValueError:
                    print("Invalid month format! Please enter in MM-YYYY format.")
            pie_chart(month)
        elif user_input == "2":
            # Generate pie chart for today's expenses
            visual_data = load_data()
            today_date = d.date.today().strftime("%Y-%m-%d")
            today_expenses = [data for data in visual_data if data[0] == today_date]
            if not today_expenses:
                print(f"No data found on {today_date}")
            else:
                today_data = {"FOOD": 0, "TRAVEL": 0, "SHOPPING": 0, "HEALTH": 0, "OTHER_BILLS": 0}
                for present_data in today_expenses:
                    today_data["FOOD"] += int(present_data[1])
                    today_data["TRAVEL"] += int(present_data[2])
                    today_data["SHOPPING"] += int(present_data[3])
                    today_data["HEALTH"] += int(present_data[4])
                    today_data["OTHER_BILLS"] += int(present_data[5])
                if sum(today_data.values()) == 0:
                    print(f"No expenses found on {today_date}")
                else:
                    labels = list(today_data.keys())
                    sizes = list(today_data.values())
                    colors = ["green", "yellow", "blue", "red", "purple"]
                    explode = [0.1, 0, 0, 0, 0]
                    plt.pie(sizes, labels=labels, colors=colors, explode=explode,
                            autopct='%1.1f%%', startangle=90, shadow=True)
                    plt.title(f"Today {today_date} Expenses")
                    plt.axis('equal')
                    plt.show()
        else:
            print("Invalid input please enter 1(or)2")
            continue

    elif n == "6":
        print("\nTHANK YOU! SEE U NEXT DAY_ ")
        break
