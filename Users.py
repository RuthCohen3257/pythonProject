# Task 8
import os
import re


class Users:
    def __init__(self, filename):
        self.filename = filename

    # 1
    def _isExistFile_True_orCreateNew_False(self):
        try:
            with open(self.filename, 'r'):
                return True
        except FileNotFoundError:
            directory = os.path.join(os.getcwd(), "files")
            os.makedirs(directory, exist_ok=True)
            new_file_path = os.path.join(directory, os.path.basename(self.filename))
            with open(new_file_path, 'w') as file:
                file.write("default_content")
                return False

    # 2
    def read_names(self):
        if self._isExistFile_True_orCreateNew_False():
            with open(self.filename, 'r') as file:
                for line in file:
                    yield line.strip()  # מחזיר את השם ללא רווחים ותווים נוספים מיותרים

    # סעיפים 4,3 נמצאים במחלקת SmartArray
    # 5
    def is_valid_email(self, email):
        # בדיקת תקינות כתובת המייל באמצעות regular expression
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def is_all_emails_valid(self):
        if (self._isExistFile_True_orCreateNew_False()):
            with open(self.filename, 'r') as file:
                for line in file:
                    email = line.strip()
                    if not self.is_valid_email(email):
                        return False
        return True
#6
    def filter_gmail(self):
        gmail_emails=[]
        if self._isExistFile_True_orCreateNew_False():
            with open(self.filename, 'r') as file:
                for line in file:
                    if line.strip().endswith('@gmail.com'):
                        gmail_emails.append(line)
        return gmail_emails
    # 7
    def read_emails_and_usernames(emails_file, usernames_file):
        emails = set()
        usernames = {}

        try:
            with open(emails_file, 'r') as emails_f, open(usernames_file, 'r') as usernames_f:
                for email, username in zip(emails_f, usernames_f):
                    email = email.strip()
                    username = username.strip()
                    emails.add(email)
                    if username not in usernames:
                        usernames[username] = email

        except FileNotFoundError as e:
            print(f"File not found: {e.filename}")

        return emails, usernames

    # 8-8
    def check_username(user_name, file_path):
        try:
            with open(file_path, 'r') as file:
                usernames = set(line.strip() for line in file)

            # ממיר את השם למספרי ASCII
            ascii_name = [ord(char) for char in user_name]
            # מחזיר את השם לסטרינג
            user_name = ''.join([chr(char) for char in ascii_name])

            # בדיקה האם השם קיים ברשימת המשתמשים
            if user_name in usernames:
                print(f"The username {user_name} exists in the usernames list.")
            else:
                print(f"The username {user_name} does not exist in the usernames list.")

            # ספירת כמה פעמים מופיעה האות "A" בשם
            count_A = user_name.count('A')
            print(f"The letter 'A' appears {count_A} times in the username.")

        except FileNotFoundError:
            print(f"File {file_path} not found.")

    # 8-9
    def convert_to_uppercase(file_path):
        with open(file_path, 'r') as file:
            usernames = set(line.strip() for line in file)
        # השתמש ברשימה המקורית כדי לא לשנות את הרשימה המקורית
        uppercased_names = [name.upper() for name in usernames]

        return uppercased_names

    # 8-10
    def calculate_payment(customers):
        total_payment = 0
        for num_customers in customers:
            if num_customers % 8 == 0:
                total_payment += 200 * (num_customers // 8)
            else:
                total_payment += 200 * (num_customers // 8) + 50

        return total_payment