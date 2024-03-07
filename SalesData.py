import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from datetime import datetime
import sys


class SalesData:

    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)

    # 4
    def eliminate_duplicates(self):
        try:
            self.data = self.data.drop_duplicates()
            self.data = self.data.dropna()
        except Exception as e:
            print(f"An error occurred: {e}")

    # 5
    def calculate_total_sales(self):
        try:
            total_sales = self.data.groupby('Product')['Quantity'].sum().reset_index()
            return total_sales
        except Exception as e:
            print(f"<Ruth , {datetime.now().strftime('%d.%m.%y, %H:%M')}> An error occurred: {e} <Ruth>")

    # 6
    def _calculate_total_sales_per_month(self):
        try:
            self.data['Date'] = pd.to_datetime(self.data['Date'], dayfirst=True)
            self.data['Month'] = pd.to_datetime(self.data['Date']).dt.month
            total_sales_per_month = self.data.groupby('Month')['Quantity'].sum().reset_index()
            return total_sales_per_month
        except Exception as e:
            print(f"<Ruth , {datetime.now().strftime('%d.%m.%y, %H:%M')}> An error occurred: {e} <Ruth>")

    # 7
    def _identify_best_selling_product(self):
        try:
            best_selling_product = self.data.groupby('Product')['Quantity'].sum().idxmax()
            return best_selling_product
        except Exception as e:
            print(f"<Ruth , {datetime.now().strftime('%d.%m.%y, %H:%M')}> An error occurred: {e} <Ruth>")

    # 8
    def _identify_month_with_highest_sales(self):
        try:
            total_sales_per_month = self._calculate_total_sales_per_month()
            month_with_highest_sales = total_sales_per_month.loc[total_sales_per_month['Quantity'].idxmax()]['Month']
            return month_with_highest_sales
        except Exception as e:
            print(f"<Ruth , {datetime.now().strftime('%d.%m.%y, %H:%M')}> An error occurred: {e} <Ruth>")

    # 9
    def analyze_sales_data(self):
        try:
            analysis_results = {}
            analysis_results['best_selling_product'] = self._identify_best_selling_product()
            analysis_results['month_with_highest_sales'] = self._identify_month_with_highest_sales()
            return analysis_results
        except Exception as e:
            print(f"<Your Name , {datetime.now().strftime('%d.%m.%y, %H:%M')}> An error occurred: {e} <Ruth>")

    # 10
    def add_additional_values(self):
        try:
            total_sales_per_month = self._calculate_total_sales_per_month()
            analysis_results = self.analyze_sales_data()
            analysis_results['minimest_selling_product'] = self.data.groupby('Product')['Quantity'].sum().idxmin()
            analysis_results['average_sales_per_month'] = total_sales_per_month['Quantity'].mean()
            return analysis_results
        except Exception as e:
            print(f"An error occurred: {e}")

    # 11
    def calculate_cumulative_sales(self):
        try:
            self.data['Date'] = pd.to_datetime(self.data['Date'])
            self.data['Month'] = self.data['Date'].dt.month
            cumulative_sales = self.data.groupby(['Product', 'Month'])['Quantity'].sum().groupby('Product').cumsum()
            return cumulative_sales
        except Exception as e:
            print(f"An error occurred: {e}")

    # 12
    def add_90_percent_values_column(self):
        try:
            self.data['discount'] = self.data['Quantity'] * 0.9
            return self.data
        except Exception as e:
            print(f"An error occurred: {e}")

    # 13
    def bar_chart_category_sum(self):
        try:
            sns.barplot(x='Product', y='Quantity', data=self.data.groupby('Product')['Quantity'].sum().reset_index())
            plt.show()
        except Exception as e:
            print(f"An error occurred: {e}")

    # 14
    def calculate_mean_quantity(self):
        try:
            quantity_array = self.data['Total'].to_numpy()
            mean = np.mean(quantity_array)
            median = np.median(quantity_array)
            second_max = np.partition(quantity_array, -2)[-2]
            return mean, median, second_max
        except Exception as e:
            print(f"An error occurred: {e}")

    # 15
    def filter_by_sellings_or_and(self):
        try:
            condition1 = (self.data['Quantity'] > 5) | (self.data['Quantity'] == 0)
            sales_counts = self.data['Product'].value_counts()
            products_sold_less_than_2_times = sales_counts[sales_counts < 2].index
            condition2 = (self.data['Price'] > 300) & self.data['Product'].isin(products_sold_less_than_2_times)
            filtered_data = self.data[condition1 & condition2]
            return filtered_data
        except Exception as e:
            print(f"An error occurred: {e}")

    # 16
    def divide_by_2(self):
        try:
            self.data['BlackFridayPrice'] = self.data['Price'] / 2
            return self.data
        except Exception as e:
            print(f"An error occurred: {e}")

    # 17
    def calculate_stats(self, columns=None):
        try:
            if columns is None:
                columns = self.data.columns
            stats = {}
            for column in columns:
                column_data = self.data[column]
                if pd.api.types.is_numeric_dtype(column_data):
                    stats[column] = {
                        'maximum': column_data.max(),
                        'sum': column_data.sum(),
                        'absolute_values': np.abs(column_data),
                        'cumulative_maximum': column_data.cummax()
                    }
                else:
                    print(f"Skipping non-numeric column '{column}'")
            return stats
        except Exception as e:
            print(f"An error occurred: {e}")

    ####################################
    # Task 6

    def bar_chart_category_sum(self):
        """
        Plot a bar chart to represent the sum of quantities sold for each product.
        """
        try:
            sns.barplot(x='Product', y='Quantity', data=self.data.groupby('Product')['Quantity'].sum().reset_index())
            plt.title('Bar Chart of Total Sales by Product')
            plt.xlabel('Product')
            plt.ylabel('Total Quantity Sold')
            plt.xticks(rotation=45)
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting bar chart: {e}")

    def line_plot_total_sales_per_month(self):
        """
        Plot a line chart to represent the total sales per month.
        """
        try:
            total_sales_per_month = self._calculate_total_sales_per_month()
            plt.plot(total_sales_per_month['Month'], total_sales_per_month['Quantity'], marker='o')
            plt.title('Total Sales per Month')
            plt.xlabel('Month')
            plt.ylabel('Total Sales')
            plt.xticks(total_sales_per_month['Month'])
            plt.grid(True)
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting line chart: {e}")

    def scatter_plot_quantity_vs_price(self):
        """
        Plot a scatter plot of Quantity vs Price.
        """
        try:
            plt.scatter(self.data['Price'], self.data['Quantity'])
            plt.title('Scatter Plot of Quantity vs Price')
            plt.xlabel('Price')
            plt.ylabel('Quantity')
            plt.grid(True)
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting scatter plot: {e}")

    def histogram_sales_distribution(self):
        """
        Plot a histogram to visualize the distribution of sales.
        """
        try:
            plt.hist(self.data['Quantity'], bins=10, color='skyblue', edgecolor='black')
            plt.title('Histogram of Sales Distribution')
            plt.xlabel('Quantity')
            plt.ylabel('Frequency')
            plt.grid(True)
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting histogram: {e}")

    def box_plot_sales_distribution(self):
        """
        Plot a box plot to visualize the distribution of sales.
        """
        try:
            sns.boxplot(x=self.data['Quantity'])
            plt.title('Box Plot of Sales Distribution')
            plt.xlabel('Quantity')
            plt.grid(True)
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting box plot: {e}")

    def seaborn_violin_plot(self):
        """
        Plot a violin plot using Seaborn to visualize the distribution of sales.
        """
        try:
            sns.violinplot(x=self.data['Quantity'])
            plt.title('Violin Plot of Sales Distribution')
            plt.xlabel('Quantity')
            plt.grid(True)
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting violin plot: {e}")

    def seaborn_pair_plot(self):
        """
        Plot a pair plot using Seaborn to visualize pairwise relationships in the dataset.
        """
        try:
            sns.pairplot(self.data)
            plt.title('Pair Plot of Sales Data')
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting pair plot: {e}")

    def pie_chart_sales_distribution(self):
        """
        גרף עוגה להצגת התפלגות המכירות לפי סוג המוצר.
        """
        try:
            sales_distribution = self.data.groupby('Product')['Quantity'].sum()
            plt.figure(figsize=(8, 8))
            plt.pie(sales_distribution, labels=sales_distribution.index, autopct='%1.1f%%', startangle=140)
            plt.title('Sales Distribution by Product')
            plt.axis('equal')
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting pie chart: {e}")

    def area_plot_sales_over_time(self):
        """
        גרף אזור מראה את המכירות לאורך הזמן.
        """
        try:
            sales_over_time = self.data.groupby('Date')['Quantity'].sum()
            plt.fill_between(sales_over_time.index, sales_over_time.values, color="skyblue", alpha=0.4)
            plt.title('Sales Over Time')
            plt.xlabel('Date')
            plt.ylabel('Total Sales')
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting area plot: {e}")

    def heatmap_sales_correlation(self):
        """
        גרף חום מראה את הקורלציה בין שדות הנתונים.
        """
        try:
            # Exclude non-numeric columns from correlation calculation
            numeric_data = self.data.select_dtypes(include=['number'])

            sales_correlation = numeric_data.corr()
            sns.heatmap(sales_correlation, annot=True, cmap='coolwarm')
            plt.title('Sales Data Correlation')
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting heatmap: {e}")

    def polar_plot_sales_distribution(self):
        """
        גרף פולארי מראה את ההתפלגות של המכירות לפי זוויות.
        """
        try:
            sales_distribution = self.data.groupby('Product')['Quantity'].sum()
            num_products = len(sales_distribution)
            angles = [n / float(num_products) * 2 * np.pi for n in range(num_products)]

            plt.figure(figsize=(6, 6))
            plt.polar(angles, sales_distribution.values)
            plt.title('Polar Plot of Sales Distribution')
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting polar plot: {e}")

    def boxplot_by_product(self):
        """
        גרף קופסתי מראה את התפלגות המכירות לפי סוג המוצר.
        """
        try:
            sns.boxplot(x='Product', y='Quantity', data=self.data)
            plt.title('Box Plot of Sales Distribution by Product')
            plt.xticks(rotation=45)
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting box plot by product: {e}")

    # Task 7
    # 3
    def generate_random_sales(self, product_name):

        # חישוב מספר המכירות של המוצר המבוקש
        sales_count = self.data[self.data['Product'] == product_name]['Quantity'].sum()

        # חישוב הסכום הגבוה ביותר ששולם עבור המוצר המבוקש
        max_price = self.data[self.data['Product'] == product_name]['Total'].max()

        # בניית הטווח בין מספר המכירות לבין הסכום הגבוה ביותר
        start_range = min(sales_count, max_price)
        end_range = max(sales_count, max_price)

        # הגרלת מספר בטווח
        random_number = np.random.randint(start_range, end_range)

        # הוספת המספר המוגרל והטווח לתוך מערך
        random_data = [random_number, (start_range, end_range)]

        return random_data

    # 4
    def print_python_version(self):
        """
        פונקציה זו מדפיסה את גרסת Python שמותקנת על המחשב.
        """
        print("Python version:", sys.version)

    # 5
    def process_parameters(self, *args):
        """
        פונקציה זו מקבלת מספר לא ידוע של פרמטרים.
        היא מדפיסה את הערך של פרמטרים שאינם מסומנים כ"תג".
        פרמטרים המסומנים כ"תג" מכניסה למילון ומחזירה אותו.
        """
        parameters_dict = {}

        for arg in args:
            if isinstance(arg, str) and ':' in arg:
                # בדיקה האם הפרמטר מכיל ":" - סימן שמציין פרמטר עם תג
                if ':' in arg:
                    # מפרידים את הפרמטר לשם התג ולערך
                    tag, value = arg.split(':', 1)
                    parameters_dict[tag.strip()] = value.strip()
            else:
                # אם אין ":" - מדפיסים את הערך
                print(arg)

        return parameters_dict

    # 6
    def printFromTheTable(self):
        # הדפסת הטבלה הראשית
        for i in range(3):
            print(f" {i + 1}הטבלה הראשית: ")
            print(self.data)
            print("\n")

        # הדפסת שלוש שורות ראשונות
        print("שלוש שורות ראשונות:")
        print(self.data.head(3))
        print("\n")

        # הדפסת שני שורות אחרונות
        print("שני שורות אחרונות:")
        print(self.data.tail(2))
        print("\n")

        # הדפסת שורה אקראית
        import random
        random_index = random.randint(0, len(self.data) - 1)
        print("שורה אקראית:")
        print(self.data.iloc[random_index])

    # 7
    def iterate_numeric_columns(self):
        try:
            for index, row in self.data.iterrows():
                print(row)
        except Exception as e:
            print(f"Error iterating over numeric columns: {str(e)}")
