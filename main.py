# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd

from SalesData import SalesData
from FileOperation import FileOperation
from SmartArray import SmartArray
from Users import Users

if __name__ == '__main__':

# Example usage:
# Instantiate the FileOperation class
    file_operator = FileOperation()
    print("Data from Excel file:")
# Reading data from an Excel file
# data_from_excel = file_operator.read_file("YafeNof.csv")
print("Data from Excel file:")
# print(data_from_excel)

# Saving data to a new Excel file
new_data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
file_operator.save_to_excel(new_data, "new_data.csv")

# Example usage:
sales_data = SalesData("YafeNof.csv")
sales_data.eliminate_duplicates()
print("Total Sales per Product:")
#print(sales_data.calculate_total_sales())
print("_calculate_total_sales_per_month:")
# print(sales_data._calculate_total_sales_per_month())
print("_identify_best_selling_product:")
# print(sales_data._identify_best_selling_product())
print("Analysis Results:")
# print(sales_data.analyze_sales_data())
print("Analysis Results with Additional Values:")
# print(sales_data.add_additional_values())

print("calculate_cumulative_sales:")
# print(sales_data.calculate_cumulative_sales())
print("add_90_percent_values_column:")
#print(sales_data.add_90_percent_values_column())
print("bar_chart_category_sum:")
# print(sales_data.bar_chart_category_sum())
print("calculate_mean_quantity:")
# print(sales_data.calculate_mean_quantity())
print("filter_by_sellings_or_and:")
# print(sales_data.filter_by_sellings_or_and())
print("divide_by_2:")
# print(sales_data.divide_by_2())
print("calculate_stats:")
# print(sales_data.calculate_stats())

###############################
# Task 6
# sales_data.bar_chart_category_sum()
# sales_data.line_plot_total_sales_per_month()
# sales_data.scatter_plot_quantity_vs_price()
# sales_data.histogram_sales_distribution()
# sales_data.box_plot_sales_distribution()
# sales_data.seaborn_violin_plot()
sales_data.seaborn_pair_plot()

# sales_data.pie_chart_sales_distribution()
# sales_data.area_plot_sales_over_time()
# sales_data.heatmap_sales_correlation()
# sales_data.polar_plot_sales_distribution()
# sales_data.boxplot_by_product()

# Task 7

product_name = "Chumash"  # שינוי שם המוצר שברצונך לבדוק
#random_data = sales_data.generate_random_sales(product_name)
# print("Random Number:", random_data[0])
# print("Range:", random_data[1])

# sales_data.print_python_version()
# print(sales_data.process_parameters(10, 'apple', 'banana', 'orange', 'tag1: value1', 'tag2: value2', 20))
# sales_data.printFromTheTable()
# sales_data.iterate_table()

users = Users("UsersName.txt")
file_content = users._isExistFile_True_orCreateNew_False()  # קריאת הקובץ או יצירתו אם הוא לא קיים
# print("File content:", file_content)

# קריאה לפונקציה ושימוש בגנרטור
names_generator = users.read_names()
# עכשיו ניתן להשתמש בגנרטור כדי לקבל את השמות בצורה עצלה ואפקטיבית
# for name in names_generator:
#    print(name)

# יצירת מערך חכם וקריאת המשתמשים מהקובץ
smart_array = SmartArray("UsersName.txt")
#  הדפסת המשתמשים בלי 10%
# print(smart_array.filtered_users)
# הדפסת משתמשים בשורות זוגיות
# print(smart_array.filter_even_rows_users())

usersEmail = Users("UsersEmail.txt")
# קריאת קובץ המיילים ובדיקת תקינותם
# print( usersEmail.is_all_emails_valid())

# סינון המיילים של ג'ימייל בלבד
# print(usersEmail.filter_gmail())
#8-7
# emails_file = "UsersEmail.txt"
# usernames_file = "UsersName.txt"
# emails, usernames = read_emails_and_usernames(emails_file, usernames_file)
#
# print("Emails:")
# print(emails)
#
# print("\nUsernames and Emails:")
# for username, email in usernames.items():
#     print(f"Username: {username}, Email: {email}")
#8-8
# check_username("Rachel","UsersName.txt")
#8-9
#
# uppercased_names= convert_to_uppercase("UsersName.txt")
# print(uppercased_names)
#8-10
# customers = [15, 20, 76, 88, 4, 43, 19, 5, 9]
# total_earnings = calculate_payment(customers)
# print("Total earnings:", total_earnings)