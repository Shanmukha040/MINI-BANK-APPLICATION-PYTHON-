
print("WELCOME TO BAMK OF ANONYMUS")
print('1.CREATE A NEW ACCOUNT')
print('2.WITHDRAW')
x=eval(input('please enter your selection:'))
list=[1,2]
for i in list:
    if i==1:
        n=str(input(f"ENTER YOUR FULL NAME:"))
        s=int(input("ENTER YOUR ADHAAR NUMBER:"))
        from random import*
        z=randrange(10000000,100000000,4)
        print(f"yoyr account number is:{z}")
    else:
        int(input("PLEASE ENTER YOUR ACCOUNT NUMBER :"))
        print("YOUR ACCOUNT BALANCE IS:" )
        l=500000000
        print(f"{l}")
        p=int(input("ENTER YOUR WITHDRAW AMOUNT:"))
if p>l:
     print("YOU HAVE INSUFFECIENT BALANCE TO WITHDRAW  PLEASE CHECK YOUR ACCOUNT BALANCE ")
else:
    
    print("YOUR TRANSACTION IS BEING PROCESSED .....")
    z=print (f"YOUR REMAINING BALANCE IS:{l-p}")
    print("THANK YOU PLEASE VISIT AGAIN")


