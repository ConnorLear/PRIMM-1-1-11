"""
PRIMM: 1+1 = 11
Description of program here
Name - Date
"""

#defines main

def main():
  #combines the two numbers the user puts in and prints them
    num1: int = input("Enter a number: ")
    num2: int = input("Enter another number: ")
    total: int = int(num1)%int(num2)

    print(f"{num1} + {num2} = {total}")

if __name__ == "__main__":
  main()
