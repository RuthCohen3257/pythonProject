from Users import Users


class SmartArray:
    def __init__(self, filename):
        self.users = []
        istrue = Users(filename)
        if istrue._isExistFile_True_orCreateNew_False():
            with open(filename, 'r') as file:
                for line in file:
                    self.users.append(line.strip())

        self.filtered_users = self.filter_users()
#3
    def filter_users(self):
        # כמות המשתמשים שנשמור
        num_users_to_keep = int(len(self.users) * 0.1)
        # מחיקת המשתמשים הראשונים 10%
        return self.users[num_users_to_keep:]

#4
    def filter_even_rows_users(self):
        even_rows=[]
        # כמות המשתמשים שנשמור
        for i, line in enumerate(self.users, start=1):
            # בדיקה אם מספר השורה הוא זוגי
            if i % 2 == 0:
                even_rows.append(line.strip())
        return even_rows