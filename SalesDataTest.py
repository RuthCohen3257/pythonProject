import os
import unittest
from unittest.mock import patch, Mock

import pandas as pd

from FileOperation import FileOperation
from SalesData import SalesData

class SalesDataTest(unittest.TestCase):

    def setUp(self):
        # Initialize a sample DataFrame for testing
        self.sample_data = {
            'Customer ID': [3, 5, 2, 6, 8, 7, 9, 15, 6, 2, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20],
            'Date': ['15.01.2023', '16.01.2023', '17.01.2023', '10.02.2023', '05.03.2023', '19.01.2023', '13.02.2023',
                     '05.03.2023', '13.02.2023', '17.01.2023', '01.04.2023', '02.04.2023', '03.04.2023', '04.04.2023',
                     '05.04.2023', '06.04.2023', '07.04.2023', '08.04.2023', '09.04.2023', '10.04.2023'],
            'Product': ['Sidur', 'Teilim', 'Sidur', 'Chumash', 'Tanach', 'Sidur', 'Tanach', 'Chumash', 'Gmara', 'Gmara',
                        'Sidur', 'Teilim', 'Chumash', 'Tanach', 'Gmara', 'Sidur', 'Teilim', 'Chumash', 'Tanach',
                        'Gmara'],
            'Price': [60, 400, 50, 300, 80, 50, 30, 800, 300, 500, 40, 450, 200, 70, 600, 45, 350, 250, 90, 550],
            'Quantity': [3, 5, 10, 2, 20, 5, 9, 30, 9, 10, 8, 4, 15, 12, 7, 6, 8, 5, 18, 3],
            'Total': [180, 2000, 600, 800, 1800, 250, 2900, 24200, 2900, 5000, 320, 1800, 3000, 840, 4200, 270, 2800,
                      1250,
                      1620, 1650]
        }
        self.test_df = pd.DataFrame(self.sample_data)
        self.your_class_instance = FileOperation()  # Instantiate without passing any arguments

    def test_eliminate_duplicates_empty_data(self):
        # יצירת מופע של המחלקה שבה נמצאת הפונקציה, עם כתובת קובץ זמנית
        instance = SalesData('YafeNof.csv')
        # טסט על DataFrame ריק
        instance.data = pd.DataFrame()
        instance.eliminate_duplicates()
        # בדיקה שאין שינויים ושהפונקציה עובדת כראוי גם על DataFrame ריק
        expected_data = pd.DataFrame()
        pd.testing.assert_frame_equal(instance.data, expected_data)

    @patch("pandas.read_csv")
    def test_read_excel_file_found(self, mock_read_csv):
        # בדיקה שהפונקציה פועלת תקין כאשר הקובץ קיים
        file_op = FileOperation()
        file_path = "YafeNof.csv"
        mock_read_csv.return_value = Mock()  # מסימול חזרה של pandas.DataFrame
        result = file_op.read_file(file_path)
        self.setUp()
        mock_read_csv.assert_called_once_with(file_path)

    @patch("pandas.DataFrame.to_csv")
    def test_save_to_csv(self, mock_to_csv):
        # Sample data
        data = {
            'Customer ID': [3, 5, 2, 6, 8],
            'Date': ['15.01.2023', '16.01.2023', '17.01.2023', '10.02.2023', '05.03.2023'],
            'Product': ['Sidur', 'Teilim', 'Sidur', 'Chumash', 'Tanach'],
            'Price': [60, 400, 50, 300, 80],
            'Quantity': [3, 5, 10, 2, 20],
            'Total': [180, 2000, 600, 800, 1800]
        }

        # Instantiate FileOperation
        file_op = FileOperation()

        # Call save_to_excel method
        file_op.save_to_excel(pd.DataFrame(data),  "YafeNofTest.csv")

        # Assert that to_excel method is called with the correct arguments
        mock_to_csv.assert_called_once_with( "YafeNofTest.csv")



    @patch("pandas.DataFrame.drop_duplicates")
    def test_eliminate_duplicates(self, mock_drop_duplicates):
        # Mocking the drop_duplicates method of DataFrame
        file_op = SalesData("YafeNof.csv")
        file_op.eliminate_duplicates()
        # Assert that drop_duplicates method was called on the DataFrame
        mock_drop_duplicates.assert_called_once()




if __name__ == '__main__':
    unittest.main()
