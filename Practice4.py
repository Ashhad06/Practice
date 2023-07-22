A=int(input("Enter Your Computer number :"))
B=int(input("Enter Your Maths number :"))
C=int(input("Enter Your English number :"))
Obtained_marks=A+B+C
Total= 300
Percentage= Obtained_marks/Total*100
if Percentage>=90:
    print("Congratulations! You got A+ and your percentage is :", Percentage ,"%")
elif Percentage>=70:
    print("Congratulations! You got A and your percentage is :", Percentage,"%")
elif Percentage>=50:
    print("You got B and your percentage is :", Percentage,"%")
elif Percentage>=40:
    print("Sorry You got D. Better luck next time and your percentage is :", Percentage,"%")
elif Percentage<=40:
    print("Sorry You are fail . Better luck next time and your percentage is :", Percentage,"%")