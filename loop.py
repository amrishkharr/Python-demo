runtime=1
while(True):
    runtime=+1
    print("Enter your marks")
    tamil=int(input("Enter Tamil Marks:"))
    english=int(input("Enter English Marks:"))
    maths=int(input("Enter Maths Marks:"))
    C_programming=int(input("Enter C Programming Marks:"))
    DBMS=int(input("Enter DBMS Marks:"))
    total=tamil+ english+ maths+ C_programming+ DBMS
    print("Total marks:",total)
    value=input("Do you want to continue:")
    if(value=='y'):
        continue
    else:
        print("Loop count:5",runtime)
        break