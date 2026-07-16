# loop in python
# WAP tp find a sum to first N natural no. input taken from user
# n= int(input("Enter a number="))
# if n<=0:
#     print("please enter the number greater then 0")
# else:
#     i=1
#     ans=0
#     while(i<=n):
#         ans=ans+i
#         #print(ans)
#         #print(i)
#         i+=1
#     print(ans)
    # print("i=",i)

# WAP write name 100 times
            # WAP to find the even sum and odd sum seperatly input taken from user

# m=int(input("please enter the number\n"))
# a=1
# esum=0
# osum=0
# while(a<=n):
#     if(a%2==0):
#         esum=esum+a
#     else:
#         osum=osum+a
#     a+=1
#     print(f" even sum={esum} and odd sum={osum}")

#           find the fectorial

# n=int(input("please enter the number \n"))
# i=1
# fact=1
# while(i<=n):
#     fact=fact*i
#     i+=1
# print(f"factorial={fact}")


            # WAP to find the no. is prime or not input taken from user 

# n= int(input("please enter the number="))
# i=2
# cnt=0
# while(i<n):
#     if n%i==0:
#         cnt+=1
#     i+=1
# if(cnt==0):
#     print("prime")
# else:
#     print("not prime")


# prime no. range

# n1=1
# n2=10

# while(n1<=n2):
#     i=1
#     cnt=0
#     while(i<=n1):
#         if(n1%i==0):
#             cnt+=1
#         i+=1
#     if(cnt==2):
#         print(n1)
#     n1+=1


#             WAP to check the reverse of an given input
# n1=12345656
# rev= 0
# while(n1!=0):
#     r=n1%10
#     rev =rev*10+r
#     n1=n1//10
# print(rev)


        # WAP to find the no. is palendrom or not input taken from user
# n1=121
# k=n1
# rev= 0
# while(n1!=0):
#     r=n1%10
#     rev =rev*10+r
#     n1=n1//10
# if(rev==k):
#     print("palendrom")
# else:
#     print("not palendrom")

# # WAP to find the no. is armstrong or not

# n1=153
# k=n1

# digit =0
# while(n1!=0):
#     digit+=1
#     n1=n1//10
# print(f"digit={digit}")

# arm=0
# m=k
# while(k!=0):
#     r=k%10
#     arm=arm+r**digit
#     k=k//10
# if(arm==m):
#     print("Armstrong",arm )
# else:
#     print("not Armstrong",arm)


# find the LCM and HCF of two no. ITFU
# WAP to print the fibonaci series
# i=1
# n=8
# a=-1
# b=1
# while(i<=n):
#     c=a+b
#     a=b
#     b=c
#     print(c)
#     i+=1


# WAP to find the multiplication of two no. using russian mathematics
# WAP to find the sum of an factorial of a no. ITFU
# WAP to find the no. is happy or not ITFU


# lcm
# n1=12
# n2=15
# mx=n1 if n1>n2 else n2
# while(True):
#     if(mx%12==0 and mx%15==0):
#         break
#     mx+=1
# print(f"lcm={mx}")

# hcf
# n1=12
# n2=15
# mx=n1 if n1<n2 else n2
# while(True):
#     if(n1%mx==0 and n2%mx==0):
#         break
#     mx-=1
# print(f"hcf={mx}")

# quadratic equ loop 

# no. of factor
# n=120
# k=1
# while(k<=n):
#     if(n%k==0):
#         print(k)
#     k+=1


# nested while loop
i=1
while(i<=5):
    j=1
    while(j<=5):
        print(i,end="  ")
        j+=1
    print()
    i+=1 