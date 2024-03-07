import os
import re
#8-1
def create_file_if_not_exists(file_path, default_content="", subdirectory=""):
    # Check if subdirectory exists, if not, create it
    if subdirectory:
        if not os.path.exists(subdirectory):
            os.makedirs(subdirectory)

    # Construct full path to the file according to the subdirectory if exists
    if subdirectory:
        file_path = os.path.join(subdirectory, file_path)

    # Check if the file exists, if not, create it
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write(default_content)
            print(f"File {file_path} created.")
    else:
        print(f"File {file_path} already exists.")
# 8-2
def read_usernames_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                yield line.strip()  # מחזיר שם משתמש בלי רווחים בתחילה ובסוף השורה
    except FileNotFoundError:
        print(f"File {file_path} not found.")
# 8-3
class LimitedArray:
    def __init__(self, limit):
        self.array = []
        self.limit = limit

    def append(self, item):
        if len(self.array) < self.limit:
            self.array.append(item)

    def __repr__(self):
        return repr(self.array)
def read_usernames_into_array(file_path):
    try:
        with open(file_path, 'r') as file:
            usernames_array = LimitedArray(int(0.9 * sum(1 for line in file)))  # מוגבל ל-90% מכמות השמות
            file.seek(0)  # חזרה לתחילת הקובץ
            for line in file:
                usernames_array.append(line.strip())  # הוספת שם משתמש למערך
            return usernames_array
    except FileNotFoundError:
        print(f"File {file_path} not found.")
# 8-4
def read_even_usernames_into_array(file_path):
    try:
        with open(file_path, 'r') as file:
            usernames_array = []  # מערך ריק לשמות המשתמשים
            for line_number, line in enumerate(file, start=1):  # משתמשים ב-enumerate כדי לקבל את מספר השורה
                if line_number % 2 == 0:  # בודקים אם מספר השורה הוא זוגי
                    usernames_array.append(line.strip())  # הוספת שם משתמש למערך
            return usernames_array
    except FileNotFoundError:
        print(f"File {file_path} not found.")
#8-5
def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email)
def read_and_validate_emails(file_path):
    valid_emails = []
    invalid_emails = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                email = line.strip()
                if validate_email(email):
                    valid_emails.append(email)
                else:
                    invalid_emails.append(email)

        print("Valid Emails:")
        for email in valid_emails:
            print(email)

        print("\nInvalid Emails:")
        for email in invalid_emails:
            print(email)

    except FileNotFoundError:
        print(f"File {file_path} not found.")
#8-6
def get_gmail_emails(file_path):
    gmail_emails = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                email = line.strip()
                if email.endswith('@gmail.com'):
                    gmail_emails.append(email)

            return gmail_emails

    except FileNotFoundError:
        print(f"File {file_path} not found.")
#8-7
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
#8-8
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
#8-9
def convert_to_uppercase(file_path):
    with open(file_path, 'r') as file:
        usernames = set(line.strip() for line in file)
    # השתמש ברשימה המקורית כדי לא לשנות את הרשימה המקורית
    uppercased_names = [name.upper() for name in usernames]


    return uppercased_names
#8-10
def calculate_payment(customers):
    total_payment = 0
    for num_customers in customers:
        if num_customers % 8 == 0:
            total_payment += 200 * (num_customers // 8)
        else:
            total_payment += 200 * (num_customers // 8) + 50

    return total_payment
# -------Example:-------
#8-1
# create_file_if_not_exists("example.txt", "This is default content for the example file.")
#
# # Example with subdirectory:
# create_file_if_not_exists("example2.txt", "This is default content for example file 2.", "subfolder")
#8-2
# file_path = "UsersName.txt"
# usernames_generator = read_usernames_from_file(file_path)
#
#
# print("Usernames:")
# for username in usernames_generator:
#     print(username)
# 8-3
# file_path = "UsersName.txt"
# usernames_array = read_usernames_into_array(file_path)
#
# print("Usernames Array:")
# print(usernames_array)
# 8-4
# file_path = "UsersName.txt"
# even_usernames_array = read_even_usernames_into_array(file_path)
#
# print("Even Usernames Array:")
# print(even_usernames_array)
#8-5
# file_path = "UsersEmail.txt"
# read_and_validate_emails(file_path)
#8-6
# file_path = "UsersEmail.txt"
# gmail_emails = get_gmail_emails(file_path)
#
# print("Gmail Emails:")
# for email in gmail_emails:
#     print(email)
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