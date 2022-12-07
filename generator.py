import csv
import random
import calendar
from datetime import datetime, timedelta
from collections import defaultdict

# Start and end dates for the data
# You can change that to what you want
start_date = datetime.strptime('2022-01-01', '%Y-%m-%d')
end_date = datetime.strptime('2022-12-31', '%Y-%m-%d')

# Number of lines in the file
# Change the value to what you need
rows_number = 100

# CSV filename
# Change csv name if you want
file_name = 'data.csv'

# A dictionary with fixed lines to import each month.
# Use it for loans, salary, etc...
# You can add as many as you want, they will appears each month between the 1st and the 10th day
# If value is negative, it will reflect as debit in the csv.
fix_lines = defaultdict(int, {
    'Phone bill': -50,
    'Electricity bill': -100,
    'Water bill': -75,
    'Salary': 2500,
    'Priv LLC': 400
})

# Generate some random data
data = []
for _ in range(rows_number):
    # Generate a random date within the specified range
    date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    # Generate a random amount between -1000 and -10, with 2 digits. You can change the values.
    amount = round(random.uniform(-1000, -10),2)
    # Generate a random label. You can add as many as you want
    labels = ['Food Delicious', 'Expensive Gas', 'Fancy Restaurant', 'Jolly Jumpers', 'Holy Cow']
    label = random.choice(labels)

    data.append((date, 'Debit', amount, label))

# Add rows for fixed charges
for label, amount in fix_lines.items():
    # Generate a date for each month within the specified range
    date = start_date
    while date <= end_date:
        day = random.randint(1, 10)
        date = datetime(date.year, date.month, day)
        data.append((date, 'Credit' if amount > 0 else 'Debit', amount, label))
        # Get the number of days in the month of the current date
        days_in_month = calendar.monthrange(date.year, date.month)[1]
        # Add the number of days in the month to the current date to get the next month
        date += timedelta(days=days_in_month)

# Sort the data by date
data.sort()

# Add an ID to each row
for i, row in enumerate(data):
    data[i] = (i + 1, row[0], row[1], row[2], row[3])

# Write the data to a CSV file
with open(file_name, 'w', newline='') as csvfile:
    # Add column headers
    fieldnames = ['ID', 'Date', 'Type', 'Amount', 'Label']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Write the data rows
    for row in data:
        writer.writerow({
            'ID': row[0],
            'Date': row[1].strftime('%Y-%m-%d'),
            'Type': row[2],
            'Amount': row[3],
            'Label': row[4],
        })

print("File is saved under "+file_name+" enjoy it while it last !")