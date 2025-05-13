print("Enter your marks")
tamil=input("Enter Tamil Marks:")
english=input("Enter English Marks:")
maths=input("Enter Maths Marks:")
C_programming=input("Enter C Programming Marks:")
DBMS=input("Enter DBMS Marks:")
tamil=int(tamil)
english=int(english)
maths=int(maths)
C_programming=int(C_programming)
DBMS=int(DBMS)
total=tamil+ english+ maths+ C_programming+ DBMS
print("Total marks:",total)  
if(total==200):
    print("Result: Pass")
else:
    print("Result: Fail")
