# Bank Statement Generator
This Python script allows you to generate bank statements and export them to CSV.
It was created for training purposes to design exercises for Data Analysts, bank investigators or OSINT fans.

You can modify some script variables to get what you want:
- csv file name
- Number of lines
- Start and end date
- Monthly fixed costs and income (such as salaries, rents, credits, telephone or electricity bills, etc.) in the form of a dictionary.
- A list of tags that will be used to generate random paylines
- The range of random payment amounts

## How it works ?
The script will generate a CSV file containing one row per month for each dictionary item (between the 1st and 10th of each month), then add the number of rows you specified with random payouts.

The file will be sorted by date, with an ID for each line.
Don't forget to change the name of the file if you want to generate more than one.

Have fun !

## Please be kind
I'm a total python beginner, so I wrote this script with my basic skills. Do not hesitate to improve or add functionalities.