s=()
while(True):
    print('''
press 1 for add:
press 2 for read:
press 3 for update:
press 4 for delete:
press 5 for close the program:

''')
    ch=int(input("Enter your choice:"))
    if(ch==1):
        print("Data added here")
        ndata=int (input("Enter the no of data you want to add:"))
        for i in range (ndata):
            print(f"Enter the {i+1} data:")
            data=input("Enter the data:")
            s.add(data)
    elif(ch==2):
        print("data read")
        print(s)