from db_config import connect
def create_account():
    name=input("enter you name:")
    email=input("enter you email:")
    balance=input("enter your opening balance:")
    db=connect()
    cursur=db.cursor()
    sql="INSERT INTO accounts(name,email,balance) VALUES (%s,%s,%s)"
    values=(name,email,balance)
    cursur.execute(sql,values)
    db.commit()
    print("Account created successfully name:",name)
    db.close()

def view_aacounts():
    db=connect()
    cursur=db.cursor()
    cursur.execute("SELECT * FROM accounts")
    accounts=cursur.fetchall()
    print("All accounts:")
    for acc in accounts:
        print(F"ID:{acc[0]},name:{acc[1]},email:{acc[2]},Balance:{3}")
    db.close()
#money deposite function
def deposite_money():
    acct_id=int(input("enter you account id:"))
    amount=float(input("enter deposite amount:"))
    db=connect()
    cursur=db.cursor()
    cursur.execute("UPDATE accounts SET balance=balance+%s WHERE id=%s",(amount,acct_id))
    db.commit()
    print(f"Money successfully deposited to id:{acct_id}.")
    db.close()
#withdraw_money function
def withdraw_money():
    acct_id=int(input("enter you account id:"))
    amount=float(input("enter withdraw amount:"))
    db=connect()
    cursur=db.cursor()
    cursur.execute("SELECT balance FROM accounts WHERE id=%s",(acct_id,))
    result=cursur.fetchone()
    if result and result[0]>= amount:
        cursur.execute("UPDATE accounts SET balance=balance-%s WHERE id=%s",(amount,acct_id))
        db.commit()
        print(f"Money successfully withdraw from id:{acct_id}.")
    else:
        print("Insuffient Balance:")
    db.close()
#check_balance() function
def check_balance():
    acct_id=int(input("enter you account id:"))
    db=connect()
    cursur=db.cursor()
    cursur.execute("SELECT name,balance FROM accounts WHERE id=%s",(acct_id,))
    result=cursur.fetchone()
    if result:
        print(f"acount holder:{result[0], result[1]}")
    else:
        print("account not found:")
    db.close()    




