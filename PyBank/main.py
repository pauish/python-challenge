import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

months = []
profit = 0
great_increase = 0
great_month = ""
great_decrese = 0
worst_month = ""

with open(budget_csv, "r", encoding="utf-8-sig") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    header = next(csv_reader)

    for row in csv_reader:
        months.append(row[0])
        if great_increase < int(row[1]):
            great_increase = int(row[1])
            great_month = row[0]
        
        if great_decrese > int(row[1]):
            great_decrese = int(row[1])
            worst_month = row[0]

        profit = profit + int(row[1])
        
print("""
Financial Analysis
----------------------------
""")
print(f"Total Months: {len(months)}")
print(f"Total: ${int(profit)}")
print(f"Average Change: ${round(profit / len(months),2)}")
print(f"Greatest Increase in Profits: {great_month} (${great_increase})")
print(f"Greatest Decrease in Profits {worst_month} (${great_decrese})")

output_file = os.path.join("analysis","results.txt")

with open(output_file,"w") as f:
    print("""
Financial Analysis
----------------------------
    """, file=f)
    print(f"Total Months: {len(months)}",file=f)
    print(f"Total: ${int(profit)}",file=f)
    print(f"Average Change: ${round(profit / len(months),2)}",file=f)
    print(f"Greatest Increase in Profits: {great_month} (${great_increase})",file=f)
    print(f"Greatest Decrease in Profits {worst_month} (${great_decrese})",file=f)