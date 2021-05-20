class Atm:
    def __init__(self,pin,cardnumber): 
        self.cardnumber = cardnumber
        self.pin = pin

    def CashWithdrawal(self, amount):
        new_amount = 500-amount
        print ("WithDrawal Successful : " + str(new_amount) + "Remaining Balance is: " + str(new_amount))

    def balance(self): 
        print ("You are so rich. You have 20 million dollars in your account.")

def main():
    name = input("Helo Sir/Madam. What is your Kind Name?")
    print("Hello, " + name)
    cardnumber = input("Enter your card number")
    pin = input("Enter your PIN")
    new_user = Atm(cardnumber,pin)

print("Chooser you action")
print("1) Balance")
print("2) CashWithdrawal")
action = int(input(" ENter your action choice"))

if (action == 1):
    amount = int(input("Enter the amount:"))
    new_user.cashWithdrawal(amount)
    else: print("Enter a valid number")
elif (action == 2):
    new_user.balance()