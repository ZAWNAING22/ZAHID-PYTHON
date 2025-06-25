from account_operation import * # * mean all
def menu():
    while True:
        print("\n")
        print("\n Bank Mangemnet System:")
        print("1. create account.")
        print("2. view accounts.")
        print("3. Deposite money.")
        print("4. withdraw money .")
        print("5. check balance.")
        print("6. exit")

        userChoice=input("enter you choice:")
        if(userChoice=="1"):
            create_account()
        elif(userChoice=="2"):
            view_aacounts()
        elif(userChoice=="3"):
            deposite_money()
        elif(userChoice=="4"):
            withdraw_money()
        elif(userChoice=="5"):
            check_balance()
        elif(userChoice=="6"):
            print("exiting ,thank you!.")
            break
        else:
            print("invalide number, try again..")
    