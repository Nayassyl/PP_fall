import re
class user:
    def init(self, _name="", _password=""):
        self.name = _name
        self.password = _password


class database:
    def init(self):
        self.__base = dict()

    def __check_for_name(self, name):
        if 4 <= len(name) <= 16:
            return True
        return False

    def __check_for_password(self, password):
        return bool(re.fullmatch("[A-Za-z0-9@#$%^&+=]{8,}", password))

    def __check_for_money(self, money):
        return bool(re.match("[0-9]*\.?[0-9]*", money))

    def save_data(self):
        with open("base.txt", "r+") as base:
            with open("data.txt", "r") as data:
                base.truncate(0)
                for i in data:
                    base.write(i)

    def add_in_terminal(self):
        check_for_name = check_for_password = check_for_money = False
        name = input("Enter the name of user:")
        password = input("Enter the password of user:")
        money = input("Enter the amount of money of user:")
        while not (check_for_name and check_for_password and check_for_money):
            if self.__check_for_name(name):
                check_for_name = True
            if self.__check_for_password(password):
                check_for_password = True
            if self.__check_for_money(password):
                check_for_money = True
            if not check_for_name:
                name = input("Wrong name\nEnter the name of user:")
            if not check_for_password:
                password = input("Wrong password\nEnter the password of user:")
            if not check_for_money:
                money = input(
                    "Wrond amount of money\nEnter the amount of money of user:")
        new_user = user(name, password)
        self.__base[new_user] = float(money)
        self.save_data()

    def add_from_file(self):
        with open("data.txt", "r") as file:
            for i in file:
                data = i.split()
                if (len(data) == 3):
                    if self.__check_for_name(data[0]) and self.__check_for_password(data[1]) and self.__check_for_money(data[2]):
                        self.__base[user(data[0], data[1])] = float(data[2])

    def change_password(self, user_name):
        is_exist = False
        for i, j in self.__base.items():
            if i.name == user_name:
                old_password = i.password
                new_password = input("Enter the new password:")
                check_for_password = False
                while not check_for_password:
                    if self.__check_for_password(new_password) and old_password != new_password:
                        check_for_password = True
                    if not check_for_password:
                        new_password = input(
                            "Wrong password\nEnter the password of user:")
                del self.__base[i]
                self.__base[user(user_name, new_password)] = j
                is_exist = True
                break
        if not is_exist:
            print("There is no such user in database")
        self.save_data()

    def show_database(self):
        counter = 1
        headers = ["ID", "Name", "Money"]
        print(f"# {headers[0]:<10}{headers[1]:<20}{headers[2]}")
        for i, j in self.__base.items():
            print(f"# {counter:<10}{i.name:<20}{j}")
            counter += 1

    def show_password(self):
        counter = 1
        headers = ["ID", "Name", "Password"]
        print(f"# {headers[0]:<10}{headers[1]:<20}{headers[2]}")
        for i in self.__base.keys():
            print(f"# {counter:<10}{i.name:<20}{i.password}")
            counter += 1