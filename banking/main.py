from banking.bank import BankAccount

if __name__ == "__main__":
    account = BankAccount("Alice")
    print("Initial Balance:", account.get_balance())

    account.deposit(100)
    account.withdraw(30)

    print("Final Balance:", account.get_balance())
    print("Transaction Log:", account.get_transactions())
