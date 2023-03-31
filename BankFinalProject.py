from random import randint


class Bank:
    def __init__(self):
        self.accounts = {}
        self.overdraft = 500

    def checkBalance(self, acct):
        print("Your balance is {}".format(self.accounts[acct]['balance']))

    def makeDeposit(self, acct):
        print("How much would you like to deposit?")
        dep = int(input())
        if dep > 0:
            self.accounts[acct]["balance"] = self.accounts[acct]["balance"] + dep
            print("Thank you, {}. Your deposit of {} was successful. Your balance is now {}.".format(
                self.accounts[acct]["name"], dep, self.accounts[acct]["balance"]))
        else:
            print("Please, deposit some money")

    def makeWithdrawal(self, acct):
        print("How much would you like to withdraw?")
        draw = int(input())
        if self.accounts[acct]["balance"] - draw >= 0:
            self.accounts[acct]["balance"] = self.accounts[acct]["balance"] - draw
            print("Thank you, {}. Your withdrawal of {} was successful. Your balance is now {}.".format(
                self.accounts[acct]["name"], draw, self.accounts[acct]["balance"]))
        elif self.accounts[acct]["balance"] - draw < 0:
            print(
                "You will be charged an overdraft fee of ${} if you continue. Are you sure you want to withdraw {}?".format(
                    self.overdraft, draw))
            print("Balance: {} | Withdrawal Request: {}".format(self.accounts[acct]["balance"], draw))
            print("Yes/No")
            choice = input()
            while choice not in ["Yes", "No"]:
                print("Please, type Yes or No.")
                choice = input()
            if choice == "Yes":
                self.accounts[acct]["balance"] = self.accounts[acct]["balance"] - draw - self.overdraft
                print("Withdrawal successful. Your new balance is {}.".format(self.accounts[acct]["balance"]))
            elif choice == "No":
                pass
        else:
            print("Please, select a numerical value")

    def menu(self, name, account):
        if account in self.accounts:
            if self.accounts[account]["name"] == name:
                while True:
                    print("Thank you for banking with us, {}.".format(name))
                    print("Please, select an option:")
                    print("1: Make a deposit")
                    print("2: Make a withdrawal")
                    print("3: Check your balance")
                    print("4: Logout")
                    choice = input()
                    if choice == '1':
                        self.makeDeposit(account)
                    elif choice == '2':
                        self.makeWithdrawal(account)
                    elif choice == '3':
                        self.checkBalance(account)
                    elif choice == '4':
                        break
                    else:
                        print("Pick a value shown above of 1 through 4 so this program runs properly!")

        else:
            print("Sorry, we cannot find your account. Please check the account number and name and try again.")

    def openAccount(self, name, deposit):
        if deposit <= 0:
            print("You need to provide money to open an account.")
        else:
            n = 5
            acctnum = ''.join(["{}".format(randint(0, 9)) for num in range(0, n)])

            while acctnum in self.accounts:
                acctnum = ''.join(["{}".format(randint(0, 9)) for num in range(0, n)])

            self.accounts[acctnum] = {"name": name,
                                      "balance": deposit}
            print("Thank you for depositing ${}. Your account has been opened, {}".format(deposit, name))
            print("Account Number: {} | Name on Account: {}".format(acctnum, name))


bank = Bank()

while True:
    print("1: Open an account")
    print("2: Login")
    print("3: Exit")
    choice = input()
    if choice == '1':
        print("What is your name and initial deposit?")
        print("Name:")
        name = input().title()
        print("Deposit:")
        dep = int(input())
        bank.openAccount(name, dep)
    elif choice == '2':
        print("What is your name and account number?")
        print("Name:")
        name = input().title()
        print("Account #:")
        acct = input()
        bank.menu(name, acct)
    elif choice == '3':
        exit()
    else:
        print("Pick a value shown above of 1 through 3 so this program runs properly!")
