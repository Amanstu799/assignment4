try :
    with open("sample.txt","rt")as fh:
        l1 = fh.readline()
        l2 = fh.readline()
        print("reaading the file content")
        print("Line1 :",l1 )
        print("Line2 :",l2 )
except FileNotFoundError  :
    print("Frror : The file 'sample.txt' does not exist ")
    
