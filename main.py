from sympy import symbols, Eq, solve
def main():
    print("""Welcome to the homework speed booster app!
          Please type the number of the option that you would like to do:
          1. Cheat I MEAN ENHANCE THE HOMEWORK EXPERIENCE
          2. Quit""")
    mainmenuinput=input("Please enter your option here: ")
    if mainmenuinput=="1":
        print("The variable that you will be solving for is X.")
        print("""Please enter the equation with the following in consideration:
              / means Divide
              * means Multiply
              + means Add
              - means Subtract
              DO NOT ADD THE EQUAL SIGN, OR ANYTHING AFTER THAT""")
        input=input("Please enter your input here: ")
        print("""Please add the answer to the equation
              Example: 5 would be what to write in x+4
              DO NOT WRITE THE EQUAL SIGN""")
        input2=input("Enter your input here: ")
        print("Please give us some time to process the request.")