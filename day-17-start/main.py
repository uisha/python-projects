class User:
    def __init__(self, username, id):
        self.username = username
        self.id = id
        self.followers = 0
        self.following = 0

    def follow(self, user_followed):
        user_followed.followers += 1
        self.following += 1


user_1 = User("User1", "001")
user_2 = User("User2", "002")

print(user_1.username, user_1.id)
print(f"    Followers: {user_1.followers}\n    Following: {user_1.following}")
print(user_2.username, user_2.id)
print(f"    Followers: {user_2.followers}\n    Following: {user_2.following}")

cont = input("Press any key to continue! ")

user_2.follow(user_1)

print(user_1.username, user_1.id)
print(f"    Followers: {user_1.followers}\n    Following: {user_1.following}")
print(user_2.username, user_2.id)
print(f"    Followers: {user_2.followers}\n    Following: {user_2.following}")
