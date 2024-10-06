from models.user import User
from db.session import Database


class UserManager:
    def __init__(self):
        self.db = Database()
        self.db.create_tables(User)
        self.session = self.db.get_session()

    # select
    def get_user(self):
        users = self.session.query(User).all()
        for user in users:
            print(user)

    # insert
    def add_user(self):
        print("Name: ", end="")
        name = input()
        print("Email: ", end="")
        email = input()

        if not name or not email:
            print("Name and email cannot be empty!")
            return

        new_user = User(name=name, email=email)
        self.session.add(new_user)
        self.session.commit()
        print(f"Success registration {new_user}")

    # update
    def update_user(self):
        print("Please enter your ID and name: ", end="")
        id = input()
        name = input()

        user = self.session.query(User).filter_by(id=id, name=name).first()

        if user:
            print("Please enter new name and email", end="")
            new_name = input()
            new_email = input()

            user.name = new_name
            user.email = new_email
            self.session.commit()
            print(f"Success updating {user}")
        else:
            print("User not found")

    # delete
    def delete_user(self):
        print("Please enter your id and name: ", end="")
        id = input()
        name = input()

        user = self.session.query(User).filter_by(id=id, name=name).first()

        if user:
            self.session.delete(user)
            self.session.commit()
            print(f"Success deleting {user}")
        else:
            print("User not found")


def main():
    manager = UserManager()

    while True:
        print("Please select mode [get, add, update, delete]: ", end="")
        mode = input()

        if mode == "get":
            manager.get_user()
        elif mode == "add":
            manager.add_user()
        elif mode == "update":
            manager.update_user()
        elif mode == "delete":
            manager.delete_user()
        else:
            print("Invalid mode...")


if __name__ == "__main__":
    main()
