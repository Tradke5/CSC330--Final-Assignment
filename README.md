Banking DSL Project
Dan Obermiller and Tyson Radke  
October 19th 2025  
CSC330  Language Design and Implementation 

---

## Overview
This project implements a Domain-Specific Language (DSL) for basic banking operations using Python.  
The system includes three main components: a lexer, a parser, and an interpreter, which together process user commands for creating and managing bank accounts.

The DSL allows users to perform operations such as creating new accounts, depositing or withdrawing funds, checking balances, entering specific accounts, and exiting the system. The goal of this assignment is to demonstrate the ability to design and interpret a simple textual language that executes meaningful actions in a banking context.

---

## Program Structure

### Main Components

| Component | Description |
|------------|--------------|
| **BankAccount** | Represents a customer’s bank account for first name, last name, account number, and balance. Includes deposit and withdrawal methods. |
| **Lexer** |Uses input strings (such as `create`, `deposit`, `withdraw`, etc.) using regular expressions and generates a list of tokens. |
| **Parser** | Builds an Abstract Syntax Tree (AST) from the token list. Each node in the AST represents a banking command. |
| **Interpreter** | Executes parsed commands by manipulating `BankAccount` objects and printing transaction results. |
| **Program** | Stores and manages all active `BankAccount` objects, allowing account lookup and modification. |

---

## How It Works

1. The `main()` function initializes the interpreter with a few pre-loaded accounts.  
   Example:
   ```python
   preInput = ["create Dan Obermiller DO300200 500", 
               "create Tyson Radke TR500900 400"]
   Interpreter.run(preInput)
   
2. The Lexer converts user input (e.g., deposit 100) into tokens.

3. The Parser organizes these tokens into meaningful command structures (AST nodes).

4. The Interpreter reads and executes the AST commands by interacting with the account data.


   
