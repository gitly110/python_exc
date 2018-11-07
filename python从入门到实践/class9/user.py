class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print('first name：', self.first_name.title())
        print('last name:', self.last_name.title())

    def greet_user(self, greet):
        print('Hello ' + greet)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


if __name__ == '__main__':
    user1 = User('tom', 'Willson')
    user1.describe_user()
    user1.greet_user(user1.first_name.title())

    print('=' * 50)

    user2 = User('jim', 'green')
    user2.increment_login_attempts()
    user2.increment_login_attempts()
    user2.increment_login_attempts()
    print('login_attempts:' + str(user2.login_attempts))
    user2.reset_login_attempts()
    print('login_attempts:' + str(user2.login_attempts))
