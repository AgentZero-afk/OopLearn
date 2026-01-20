from dataclasses import dataclass

@dataclass(frozen=True)
class Transaction:
    amount: float
    description: str


class AccountError(Exception):
    pass
class TransactionError(AccountError):
    pass

class Account:
    def __init__(self,owner:str,initial_balance:float = 0.0):
        self.owner = owner
        self._initial_balance = initial_balance
        self._transactions = []


    @property
    def balance(self):
        balance = self._initial_balance + sum(t.amount for t in self._transactions)
        return balance



    def add_transaction(self,transaction:Transaction):
        if not isinstance(transaction, Transaction):
            raise TypeError("Ожидается объект Transaction")
        new_transaction = self.balance + transaction.amount
        if new_transaction < 0:
            raise TransactionError("Транзакция невозможна, недостаточно средств.")
        self._transactions.append(transaction)

    @classmethod
    def from_csv(cls,csv_string:str):
        name, balance = csv_string.split(',')
        return cls(name.strip(),float(balance.strip()))


    def __len__(self):
        return len(self._transactions)

    def __str__(self):
        return f'Счет {self.owner}'

    def __repr__(self):
        return f'Account(owner={self.owner!r}, initial_balance={self._initial_balance})'