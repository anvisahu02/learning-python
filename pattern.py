# n=5
# i=1
# while(i<=n):
#     j=1
#     while(j<=n):
#         print(i,end=" ")
#         j+=1

#     print()
#     i+=1



# n=5
# i=1
# while(i<=n):
#     j=1
#     while(j<=n):
#         print(j,end="  ")
#         j+=1
        
#     print()
#     i+=1


# n=5
# i=1
# while(i<=n):
#     j=1
#     while(j<=n):
#         print("*",end="  ")
#         j+=1
        
#     print()
#     i+=1


# n=5
# i=1
# c=1
# while(i<=n):
#     j=1
#     while(j<=n):
#         print(c,end="  ")
#         c+=1
#         j+=1
        
#     print()
#     i+=1


# 
# n=5
# i=1
# while(i<=n):
#     j=1
#     while(j<=i):
#         print("*",end="  ")
#         j+=1
        
#     print()
#     i+=1

# n=5
# i=1
# while(i<=n):
#     j=1
#     while(j<=i):
#         print(i,end="  ")
#         j+=1
        
#     print()
#     i+=1


# n=5
# i=1
# while(i<=n):
#     j=1
#     while(j<=n-i+1):
#         print(j,end="  ")
#         j+=1
        
#     print()
#     i+=1

# n=5
# i=1
# while(i<=n):
#     j=1
#     while(j<=n):
#         if(i==1 or i==5 or j==1 or j==5):
#             print("*",end=" ")
#         else:
#             print(" ", end=" ")
#         j+=1
#     print()
#     i+=1




n=5
i=1
while(i<=n):
    j=1
    while(j<=n):
        if(i==1 or i==5 or j==1 or j==5):
            print("*",end=" ")
        elif(i==j or (i==2 and j==4)or (i==4 and j==2)):
            print("*" , end=" ")
        else:
            print(" ", end=" ")
        j+=1
    print()
    i+=1