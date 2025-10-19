# Dan Obermiller and Tyson Radke
# 10/17/2025
# Assignment 7
# Create a specification test for the DSL Banking Application in Python.

# We pledge that all work in this program is our own and not obtained from anyone or any other source.
#
# References:
# "unittest — Unit testing framework." Python, https://docs.python.org/3/library/unittest.html.


import banking;
import unittest;

# Main function
def main():
    inLoop = True;
    # Enter main loop
    while inLoop:
        # Give user a list of options
        SpecTest.printOptions();
        userInput = int(input("Enter number: "));
        # Bulk test
        if userInput == 1:
            unittest.main(verbosity=2, exit=False);
        # Individual test
        elif userInput == 2:
            SpecTest.printTests();
            subInput = int(input("Enter number: "));
            IndividualTests.single_test(subInput);
        # Exit program
        elif userInput == 3:
            inLoop = False;
        # Input is not a number 1-3
        else:
            print("Unknown input. Please enter a valid number.");
            
##################################
##### BULK TEST BANK METHODS #####
##################################
class TestBankMethods(unittest.TestCase):
    # Deposit test method
    # Deposit 450 in an account with 400
    def test_deposit(self):
        interpreter1 = banking.Interpreter();
        preinput = ["create Tyson Radke TR500900 400", "enter TR500900", "deposit 450", "exit", "exit"];
        bank = interpreter1.run(preinput);
        account = bank.findAccount("TR500900");
        balance = account.getBalance();
        print("--------------------");
        print(f"Deposit test: {balance} = 850");
        print("--------------------");
        # Get output of testing
        self.assertEqual(balance, 850.0);
        # Clear all accounts from bank
        bank.clearAccounts();
        
    # Withdraw test method
    # Withdraw 140 from an account with 800
    def test_withdraw(self):
        interpreter2 = banking.Interpreter();
        preinput = ["create Sam Smith SS500900 800", "enter SS500900", "withdraw 140", "exit", "exit"];
        bank = interpreter2.run(preinput);
        account = bank.findAccount("SS500900");
        balance = account.getBalance();
        print("--------------------");
        print(f"Withdraw test: {balance} = 660");
        print("--------------------");
        # Get output of testing
        self.assertEqual(balance, 660.0);
        # Clear all accounts from bank
        bank.clearAccounts();
        
    # Name test method
    # Create an account with the first name of Dan
    def test_name(self):
        interpreter3 = banking.Interpreter();
        preinput = ["create Dan Obermiller DO500900 400", "enter DO500900", "exit", "exit"];
        bank = interpreter3.run(preinput);
        account = bank.findAccount("DO500900");
        firstName = account.getFirstName();
        print("--------------------");
        print(f"Name test: {firstName} = Dan");
        print("--------------------");
        # Get output of testing
        self.assertEqual(firstName, "Dan");
        # Clear all accounts from bank
        bank.clearAccounts();

###################################
##### INDIVIDUAL BANK METHODS #####
###################################
class IndividualTests():
    def single_test(num):
        # Deposit test method
        if num == 1:
            interpreter1 = banking.Interpreter();
            preinput = ["create Tyson Radke TR500900 400", "enter TR500900", "deposit 450", "exit", "exit"];
            bank = interpreter1.run(preinput);
            account = bank.findAccount("TR500900");
            balance = account.getBalance();
            print("--------------------");
            print(f"Deposit test: {balance} = 850");
            print("--------------------");
            if balance == 850:
                print("Passed");
            else:
                print("Failed");
        # Withdraw test method
        elif num == 2:
            interpreter2 = banking.Interpreter();
            preinput = ["create Sam Smith SS500900 800", "enter SS500900", "withdraw 140", "exit", "exit"];
            bank = interpreter2.run(preinput);
            account = bank.findAccount("SS500900");
            balance = account.getBalance();
            print("--------------------");
            print(f"Withdraw test: {balance} = 660");
            print("--------------------");
            if balance == 660:
                print("Passed");
            else:
                print("Failed");
        # Name test method
        elif num == 3:
            interpreter3 = banking.Interpreter();
            preinput = ["create Dan Obermiller DO500900 400", "enter DO500900", "exit", "exit"];
            bank = interpreter3.run(preinput);
            account = bank.findAccount("DO500900");
            firstName = account.getFirstName();
            print("--------------------");
            print(f"Name test: {firstName} = Dan");
            print("--------------------");
            if firstName == "Dan":
                print("Passed");
            else:
                print("Failed");
        bank.clearAccounts();
    
######################################
##### SPECIFICATION TEST OPTIONS #####
######################################
class SpecTest():
    
    def printOptions():
        print("1. Run all tests");
        print("2. Run a singular test");
        print("3. Exit program");

    def printTests():
        print("1. Deposit Test");
        print("2. Withdraw Test");
        print("3. Name Test");

if __name__ == "__main__":
    main();



