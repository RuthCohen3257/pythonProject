import pandas as pd

from FileReaderInterface import FileReaderInterface


class FileOperation(FileReaderInterface):

    #1
    def read_file(self, file_path: str):
        """
        Read data from an Excel file located at the specified file path.

        Parameters:
            file_path (str): The path to the Excel file.

        Returns:
            pandas.DataFrame: The DataFrame containing the data from the Excel file.
        """
        try:
            data = pd.read_csv(file_path)
            return data
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except Exception as e:
            print(f"Error occurred while reading Excel file: {e}")
#2
    def save_to_excel(self, data, file_name: str):
        """
        Save the provided data to a new Excel file with the given file name.

        Parameters:
            data (pandas.DataFrame): The data to be saved to Excel.
            file_name (str): The name of the Excel file.

        Returns:
            None
        """
        try:
            data.to_csv(file_name)
            print(f"Data successfully saved to '{file_name}'.")
        except Exception as e:
            print(f"Error occurred while saving to Excel file: {e}")


