import unittest
from banking.bank import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Alice")

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 0)

    def test_deposit_valid(self):
        self.account.deposit(100)
        self.assertEqual(self.account.get_balance(), 100)

    def test_deposit_invalid(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-50)

    def test_withdraw_valid(self):
        self.account.deposit(200)
        self.account.withdraw(100)
        self.assertEqual(self.account.get_balance(), 100)

    def test_withdraw_invalid_amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-30)

    def test_withdraw_insufficient_balance(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(50)

    def test_transactions_logged(self):
        self.account.deposit(50)
        self.account.withdraw(20)
        self.assertIn("Deposited 50", self.account.get_transactions())
        self.assertIn("Withdrew 20", self.account.get_transactions())

if __name__ == '__main__':
    unittest.main()
