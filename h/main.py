# Basic Implementation of IF100 Take-Home Exam 5 - Retail Data Analysis
# Due: May 29th

# Import required libraries
from collections import defaultdict

# Define data file path
DATA_FILE = 'superstore_sales.txt'

# Function to read data
def read_data(file_path):
    data = []
    file = open(file_path, 'r')
    for line in file:
        data.append(line.strip().split('\t'))
    file.close()
    return data

# Function to filter data
def filter_data(data, region, category, segment):
    filtered = []
    for record in data:
        if (region == 'all' or record[13].lower() == region.lower()) and \
           (category == 'all' or record[14].lower() == category.lower()) and \
           (segment == 'all' or record[7].lower() == segment.lower()):
            filtered.append(record)
    return filtered

# Function to calculate totals
# Function to calculate totals
def calculate_totals(filtered_data):
    total_sales = 0
    total_profit = 0
    total_quantity = 0

    for record in filtered_data:
        # Ensure the record has exactly 21 fields
        if len(record) == 21:
            total_sales += float(record[18])
            total_profit += float(record[20])
            total_quantity += int(record[17])
        else:
            print(f"Skipping malformed record: {record}")

    return total_sales, total_profit, total_quantity
# Main function
def main():
    data = read_data(DATA_FILE)

    region = input("Enter region (East, West, South, Central, all): ").strip()
    category = input("Enter category (Furniture, Technology, Office Supplies, all): ").strip()
    segment = input("Enter segment (Consumer, Corporate, Home Office, all): ").strip()

    filtered_data = filter_data(data[1:], region, category, segment)
    total_sales, total_profit, total_quantity = calculate_totals(filtered_data)

    print("Total Records:", len(filtered_data))
    print("Total Sales:", round(total_sales, 2))
    print("Total Profit:", round(total_profit, 2))
    print("Total Quantity:", total_quantity)

    while True:
        subcategory = input("Enter sub-category or 'exit': ").strip().lower()
        if subcategory == 'exit':
            break

    print("End of Analysis")

if __name__ == "__main__":
    main()
