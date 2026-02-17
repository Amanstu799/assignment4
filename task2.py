st = input("Enter the data you want to write :")
with open("assignment4/output.txt",'xt') as fh:
    fh.write(st+"\n")
    print("Data is successfully written in output.txt")

st1 = input("enter the data to append to the file")    
with open("assignment4/output.txt",'at') as ap:
    ap.write(st1)
    print("Data is successfully append in output.txt")

with open("assignment4/output.txt",'rt') as rt:  
    l1 = rt.readline()
    l2 = rt.readline()
    print("reaading the file content")
    print("Line1 :",l1 )
    print("Line2 :",l2 )