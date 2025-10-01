class BankAccount:
    def __init__(self, first_name, last_name, account_number, balance=0):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__account_number = account_number
        self.__balance = balance

    def get_first_name(self):
        return self.__first_name

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
            return self.__balance
        self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return self.__balance


def main():
    accounts = [
        BankAccount("Tyson", "Radke", "TR123456", 1000),
        BankAccount("Dan", "Obermiller", "DO654321", 500)
    ]

    running = True
    while running:
        print("Banking menu will go here")
        running = False

if __name__ == "__main__":
    main()
