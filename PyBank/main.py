# Import modules
import csv

# File path
budget_csv = r"Resources/budget_data.csv"
budget_output_txt = r"analysis/budget_output.txt"

# Create variables
greatest_decrease = 0
greatest_increase = 0
previous_profit_loss = 0
profit_loss_changes = []
total_months = 0
total_net_profit = 0

# Create date variables
greatest_decrease_date = ""
greatest_increase_date = ""

# Read the dataset from budget-data.csv
with open(budget_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Skip header
    header = next(csv_reader)

    # Loop thru all rows in CSV
    for row in csv_reader:
        date = row[0]
        profit_loss = int(row[1])

        # Increase total month count and find net total
        total_months += 1
        total_net_profit += profit_loss

        # Find any profit/loss changes
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            profit_loss_changes.append(change)

            # Update greatest decrease and increase
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = date
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = date

        previous_profit_loss = profit_loss

# Find average of profit/loss changes
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

# Print output
print(f'Financial Analysis')
print(f'----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_net_profit}')
print(f'Average Change: ${round(average_change,2)}')
print(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})')

# Save output to text file
with open(budget_output_txt, "w") as output_txt_file:
    output_txt_file.write(f'Financial Analysis\n')
    output_txt_file.write(f'----------------------------\n')
    output_txt_file.write(f'Total Months: {total_months}\n')
    output_txt_file.write(f'Total: ${total_net_profit}\n')
    output_txt_file.write(f'Average Change: ${round(average_change, 2)}\n')
    output_txt_file.write(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n')
    output_txt_file.write(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n')