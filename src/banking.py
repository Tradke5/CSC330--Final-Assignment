from enum import Enum;
import re;


def main():
    input = ["create Dan Obermiller DO617889 500"];
    tokens = Lexer.GetTokens(input);
    try:
        tokens = Lexer.GetTokens(input);
 #       program = Parse(tokens);
 #       rez = program.TopExpression.Evaluate();
 #       Console.WriteLine(rez + Environment.NewLine);
    
    except:
        print("Unable to process input");

class BankAccount:
    def __init__(self, fname, lname, accNumber, balance):
        self.firstName = fname;
        self.lastName = lname;
        self.accNumber = accNumber;
        self.balance = balance;

    def deposit(self, val):
        self.balance += val;

    def withdraw(self, val):
        if (self.balance >= val):
            self.balance -= val;

    


    
class Lexer:
    def GetTokens(lines):
        tokenList = [];
        inAccount = False;
        for line in lines:
            
            if re.match(line, "^create|enter") and inAccount == True:
                raise Exception("You must exit the current account before creating or accessing another account.");

            match = re.match(r"^(?P<create>create) (?P<fname>(?P<fini>[a-zA-z])[a-zA-Z']+) (?P<lname>(?P<lini>[a-zA-Z])[a-zA-Z']+) (?P<accNum>\3\5[0-9]{6}) (?P<bal>[0-9]+(\.[0-9]+)?)$", line);
            if match:
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
                continue;
            
            match = re.match(r"^(?P<enter>enter) (?P<accNum>[a-zA-Z]{2}[0-9]{6})$", line);
            if match:
                enter = match.group('enter');
                accountNumber = match.group('accNum');
                
                tokenList.append(TokenType(Token.ENTER, Token.ENTER, 1));
                tokenList.append(TokenType(Token.ACCNUMBER, accountNumber, 7));
                inAccount = True;
                continue;

            match = re.match(r"^(?P<exit>exit)$", line);
            if match:
                ex = match.group('exit');
                
                tokenList.append(TokenType(Token.EXIT, Token.EXIT, 1));
                if inAccount:
                    inAccount = False;
                continue;
            
            match = re.match(r"^(?P<balance>balance)$", line);
            if match:
                bal = match.group('balance');
                
                tokenList.append(TokenType(Token.BALANCE, Token.BALANCE, 1));
                continue;

            match = re.match(r"^(?P<deposit>deposit) (?P<num>[0-9]+(\.[0-9]{2})?)$", line);
            if match:
                deposit = match.group('deposit');
                num = match.group('num');

                tokenList.append(TokenType(Token.DEPOSIT, Token.DEPOSIT, 1));
                tokenList.append(TokenType(Token.NUMBER, num, 9));
                continue;

            match = re.match(r"^(?P<withdraw>withdraw) (?P<num>[0-9]+(\.[0-9]{2})?)$", line);
            if match:
                withdraw = match.group('withdraw');
                num = match.group('num');

                tokenList.append(TokenType(Token.WITHDRAW, Token.WITHDRAW, 1));
                tokenList.append(TokenType(Token.NUMBER, num, 10));
                continue;
        
        return tokenList;




                

            
    
class Parser:
    def __init__(self):
        print(1);
    
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

class TokenType:
    def __init__(self, type, value, position):
        self.type = type;
        self.value = value;
        self.position = position;
    
        
    
class ASTNode:
    def __init__(self):
        print(1);
    
class Interpreter:
    def __init__(self):
        print(1);
    

if __name__ == "__main__":
    main()
