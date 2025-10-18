# Dan Obermiller and Tyson Radke
# 10/17/2025
# Assignment 7
# Create a DSL Banking Application using a lexer, parser, and interpreter in Python.

# We pledge that all work in this program is our own and not obtained from anyone or any other source.

# References:
#


from enum import Enum;
import re;

# Main function
def main():
    # Preinput allows for the entering of any banking code before the program enters the while loop
    preInput = ["create Dan Obermiller DO300200 500", "create Tyson Radke TR500900 400"];
    # Run the interpreter using this preinput
    Interpreter.run(preInput);
    
########################
##### BANK ACCOUNT #####
########################

class BankAccount:
    # Create Bank Account with First Name, Last Name, Account Number, and starting Balance
    def __init__(self, fname, lname, accNumber, balance):
        self.firstName = fname;
        self.lastName = lname;
        self.accNumber = accNumber;
        self.balance = float(balance);

    # Deposit value
    def deposit(self, val):
        valFloat = float(val);
        self.balance += valFloat;

    # Withdraw value from account
    def withdraw(self, val):
        valFloat = float(val);
        # If user has enough money, then proceed with withdrawal. Otherwise, don't do it
        if (self.balance >= valFloat):
            self.balance -= valFloat;
        else:
            print("Could not withdraw that amount.");

    # Getter and setter methods for all variables in Bank Account
    def getBalance(self):
        return self.balance;

    def getAccNumber(self):
        return self.accNumber;

    def getFirstName(self):
        return self.firstName;

    def getLastName(self):
        return self.lastName;

    def setBalance(self, val):
        self.balance = val;

    def setAccNumber(self, val):
        self.accNumber = val;

    def setFirstName(self, fName):
        self.firstName = fName;

    def setLastName(self, lName):
        self.lastName = lName;

    

#################
##### LEXER #####
#################
    
class Lexer:
    def GetTokens(lines):
        # Create running token list
        tokenList = [];
        inAccount = False;
        # Iterate over each line given from input
        for line in lines:
            # If the user is already in an account and tries to create or enter another, raise an exception.
            if re.match(line, "^create|enter") and inAccount == True:
                raise Exception("You must exit the current account before creating or accessing another account.");

            # Regex match for create account
            match = re.match(r"^(?P<create>create) (?P<fname>(?P<fini>[a-zA-z])[a-zA-Z']+) (?P<lname>(?P<lini>[a-zA-Z])[a-zA-Z']+) (?P<accNum>\3\5[0-9]{6}) (?P<bal>[0-9]+(\.[0-9]+)?)$", line);
            if match:
                # Assign token values from regex match
                create = match.group('create');
                firstName = match.group('fname');
                lastName = match.group('lname');
                accountNumber = match.group('accNum');
                balance = match.group('bal');

                tokenList.append(TokenType(Token.CREATE, Token.CREATE, 1));
                tokenList.append(TokenType(Token.FNAME, firstName, 8));
                tokenList.append(TokenType(Token.LNAME, lastName, 8 + len(firstName)));
                tokenList.append(TokenType(Token.ACCNUMBER, accountNumber, 8 + len(firstName) + len(lastName)));
                tokenList.append(TokenType(Token.NUMBER, balance, 8 + len(firstName) + len(lastName) + len(accountNumber)));
            
            # Regex match for enter account
            match = re.match(r"^(?P<enter>enter) (?P<accNum>[a-zA-Z]{2}[0-9]{6})$", line);
            if match:
                # Assign token values from regex match
                enter = match.group('enter');
                accountNumber = match.group('accNum');
                
                tokenList.append(TokenType(Token.ENTER, Token.ENTER, 1));
                tokenList.append(TokenType(Token.ACCNUMBER, accountNumber, 7));
                # Enter account
                inAccount = True;

            # Regex match for exiting account or program
            match = re.match(r"^(?P<exit>exit)$", line);
            if match:
                # Create an exit token
                ex = match.group('exit');
                
                tokenList.append(TokenType(Token.EXIT, Token.EXIT, 1));
                if inAccount:
                    inAccount = False;
            
            # Regex match for balance
            match = re.match(r"^(?P<balance>balance)$", line);
            if match:
                # Create balance token
                bal = match.group('balance');
                
                tokenList.append(TokenType(Token.BALANCE, Token.BALANCE, 1));

            # Regex match for deposit 
            match = re.match(r"^(?P<deposit>deposit) (?P<num>[0-9]+(\.[0-9]{2})?)$", line);
            if match:
                # Create deposit and number token for the money value
                deposit = match.group('deposit');
                num = match.group('num');

                tokenList.append(TokenType(Token.DEPOSIT, Token.DEPOSIT, 1));
                tokenList.append(TokenType(Token.NUMBER, num, 9));

            # Regex match for withdraw
            match = re.match(r"^(?P<withdraw>withdraw) (?P<num>[0-9]+(\.[0-9]{2})?)$", line);
            if match:
                # Create withdraw and number token for the money value
                withdraw = match.group('withdraw');
                num = match.group('num');

                tokenList.append(TokenType(Token.WITHDRAW, Token.WITHDRAW, 1));
                tokenList.append(TokenType(Token.NUMBER, num, 10));
        # If line doesn't match any correct syntax, raise an error.
        if not tokenList:
            raise("Unable to process input.");
        return tokenList;




                

##################
##### PARSER #####
##################           
    
class Parser:
    current = None;

    def Parse(tokens):
        # Create a running AST Node
        node = ASTNode();
        node.clearStatementList();

        # Iterate over each token
        for token in tokens:
            # If the token is a starting keyword, then create that specific class
            if token.type == Token.CREATE:
                current = Create();
            elif token.type == Token.ENTER:
                current = Enter();
            elif token.type == Token.EXIT:
                current = Exit();
                node.addStatement(current);
                current = None;
            elif token.type == Token.DEPOSIT:
                current = Deposit();
            elif token.type == Token.WITHDRAW:
                current = Withdraw();
            elif token.type == Token.BALANCE:
                current = Balance();
                node.addStatement(current);
                current = None;
            # Find tokens associated with starting keyword (EX: Create has First Name, Last Name, Account Number, and Balance tokens)
            elif type(current) is Create:
                if token.type == Token.FNAME:
                    current.firstName = token.value;
                elif token.type == Token.LNAME:
                    current.lastName = token.value;
                elif token.type == Token.ACCNUMBER:
                    current.accNumber = token.value;
                elif token.type == Token.NUMBER:
                    current.balance = token.value;
                    node.addStatement(current);
                    current = None;
            
            elif type(current) is Enter:
                if token.type == Token.ACCNUMBER:
                    current.accNumber = token.value;
                    node.addStatement(current);
                    current = None;
            
            
            elif type(current) is Deposit:
                if token.type == Token.NUMBER:
                    current.value = token.value;
                    node.addStatement(current);
                    current = None;
            
            elif type(current) is Withdraw:
                if token.type == Token.NUMBER:
                    current.value = token.value;
                    node.addStatement(current);
                    current = None;
        # Return AST Node
        return node.getStatementList();
                    
    
###########################
##### PARSING CLASSES #####
###########################
# These are created from the lexer tokens
class Create:
    def __init__(self):
        firstName = None;
        lastName = None;
        accNumber = None;
        balance = None;

class Balance:
    def __init__(self):
        value = None;

class Withdraw:
    def __init__(self):
        value = None;

class Deposit:
    def __init__(self):
        value = None;

class Exit:
    def __init__(self):
        value = None;

class Enter:
    def __init__(self):
        accNumber = None;

##################################
##### TOKEN ENUMERATOR CLASS #####
##################################
# All tokens within program
class Token(Enum):

    CREATE = 1;
    FNAME = 2;
    LNAME = 3;
    ACCNUMBER = 4;
    NUMBER = 5;
    EXIT = 6;
    ENTER = 7;
    DEPOSIT = 8;
    WITHDRAW = 9;
    BALANCE = 10;

########################
##### TOKEN CLASS ######
########################
# Base token has a type, value, and position
class TokenType:
    def __init__(self, type, value, position):
        self.type = type;
        self.value = value;
        self.position = position;
    
########################
##### AST NODE #########
########################    
# AST Node keeps a running command list and appends all of them together
class ASTNode:
    statementList = [];

    def addStatement(self, line):
        self.statementList.append(line);

    def getStatementList(self):
        return self.statementList;

    def clearStatementList(self):
        self.statementList.clear();

########################
##### INTERPRETER ######
########################
# Runs preinput and user input
class Interpreter:
    # Run program
    def run(preInput):
        # Create bank program
        bank = Program();
        userInput = [];
        inProgram = True;
        selAccount = None;
        # Evaluate preinput
        # Get tokens, parse those tokens, then evaluate the AST Structure
        try:
            tokens = Lexer.GetTokens(preInput);
            code = Parser.Parse(tokens);
            inProgram, selAccount = Interpreter.Evaluate(bank, code, selAccount);
        # If there is an error, raise an exception
        except:
            print("Unable to process input");

        # Enter loop for user input
        while (inProgram):
            # If not within account, print available commands
            if selAccount == None:
                tempInput = input("Commands: create <First Name> <Last Name> <Account Number> <Balance> OR enter <Account Number> OR exit\n");
                userInput.append(tempInput);
            # If within account, print available commands
            else:
                tempInput = input("Commands: balance OR withdraw <Amount> OR deposit <Amount> OR exit\n");
                userInput.append(tempInput);
            # Process user input
            try:
                tokens = Lexer.GetTokens(userInput);
                code = Parser.Parse(tokens);
                inProgram, selAccount = Interpreter.Evaluate(bank, code, selAccount);
            except:
                print("Unable to process input");
            # Clear user input list
            userInput.clear();
    
    # Evaluate AST Structure
    def Evaluate(bank, code, selAccount):
        # Iterate over each object
        for line in code:
            # Create object
            if type(line) is Create:
                # If not within an account and the account number is not the same as another account, then proceed with creation.
                if selAccount == None:
                    if bank.findAccount(line.accNumber) == None:
                        # Create account and add to list
                        acc = BankAccount(line.firstName, line.lastName, line.accNumber, line.balance);
                        bank.addAccount(acc);
                        print(f"{line.firstName}'s account has been created.");
                    else:
                        print("Error: account number already in system.");
                else:
                    print("You must exit the current account before creating or accessing another account.");
            # Enter object
            elif type(line) is Enter:
                if selAccount == None:    
                    selAccount = bank.findAccount(line.accNumber);
                    # If not within an account, then find bank account and enter it
                    if selAccount != None:
                        print(f"Entering {selAccount.getFirstName()}'s account.");
                    else:
                        print("Could not find that account.");
                else:
                    print("Please exit the current account before entering another one.");
            # Balance object - prints balance of current account
            elif type(line) is Balance:
                print(f"{selAccount.firstName}'s balance: ${selAccount.getBalance()}");
            # Deposit money into current account
            elif type(line) is Deposit:
                selAccount.deposit(line.value);
                print(f"${line.value} successfully deposited into {selAccount.getFirstName()}'s account.");
            # Withdraw money from current account
            elif type(line) is Withdraw:
                selAccount.withdraw(line.value);
                print(f"${line.value} successfully withdrawn from {selAccount.getFirstName()}'s account.");
            # Exit current account or exit program
            elif type(line) is Exit:
                if selAccount != None:
                    print(f"Exiting {selAccount.getFirstName()}'s account.");
                    selAccount = None;
                else:
                    return False, selAccount;
        return True, selAccount;
                
                
            
########################
##### PROGRAM ##########
########################
        
class Program:
    accounts = [];

    # Iterate over bank accounts and match account number with input
    def findAccount(self, accNumber):
        selected = None;
        for account in self.accounts:
            if account.getAccNumber() == accNumber:
                selected = account;
        return selected;

    def getAccountList(self):
        return self.accounts;

    def addAccount(self, account):
        self.accounts.append(account);
        
# Run main program
if __name__ == "__main__":
    main()
