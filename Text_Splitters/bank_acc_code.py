from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

text = """
class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. Remaining balance: {self.balance}")
        else:
            print("Insufficient balance.")

# Example usage
acc1 = BankAccount("123456", "Sneha", 500)
acc1.deposit(200)
acc1.withdraw(100)
acc1.withdraw(700)
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=200,
    chunk_overlap=0,
)

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks[0])
print(chunks[1])
