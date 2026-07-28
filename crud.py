ls=[]
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
            ls.append(data)
    elif(ch==2):
        print("data read")
        print(ls)
    elif(ch==3):
        print("data udate here")
        ndata=int (input("Enter the no of data you want to update:"))
        for i in range (ndata):
            try:
                print(f"Enter the {i+1} data:")
                fdata=input("Enter the data:")
                ind=ls.index(fdata)
                udata=input("enter the data to update:")
                ls[ind]=udata
            except:
                  print("data not found")
    elif(ch==4):
          print("data delete here")
    elif(ch==5):
          print("program closed")
          break
    else:
          print("choice is wrong")
          continue
               
                
                


            

