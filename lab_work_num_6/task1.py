class UserAccount:

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def check_password(self, entered_password):
        if entered_password == self.__password:
            return True
        else:
            return False

    def set_password(self, current_password, new_password):
        if self.check_password(current_password):
            self.__password = new_password
        else:
            raise ValueError


user1 = UserAccount('misha', 'xxx@ku.com', 123)

user1.set_password(123, 321)

if user1.check_password(321) == True:
    print('все круто')
