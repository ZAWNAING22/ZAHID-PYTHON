import os 
history_file='history.txt'

def show_history():
    # if not os.path.exists(history_file):
    #     return 'hostory file not exit'
    with open(history_file,'r') as f:
        lines=f.readlines()
        if len(lines)==0:
            print("No history found")
        return
        #from recent to oldest history line ->reversed
        for line in reversed(lines):
            print(line.strip())
def clear_history():
    f=open(history_file,'w')
    f.close()
    print("the history is cleared!")

def save_history(equation,result):
    with open(history_file,'a') as f:
        f.write(f'{equation}={str(result)} \n')  
def calculate(user):
    parts=user.split()
    if len(parts)!=3:
        print(parts)
        print("the expression have to be eg: A+B")  
        return
    n1=float(parts[0])
    op=parts[1]
    n2=float(parts[2])

    if op=='+':
        result=n1+n2
    elif op=='-':
        result=n1-n2
    elif op=='*':
        result=n1*n2
    elif op=='/':
        if n2==0:
            print("cant not devide by zero")
            return
        else:
            result=n1/n2
    else:
        print("please enter valide operator :(+-*/)")
        return
    print(user,'=',result)
    save_history(user,result)

def main():
    print("----------- SIMPLE CALCATOR WITH HISTORY ------------------")
    while True:

        user_input=input("enter calculatin(+-*/) or comand(history,clear or exit:")
        if user_input=='exit':
            print("good bye")
            break
        elif user_input=='history':
            show_history()
        elif user_input=='clear':
            clear_history()
        else:
            calculate(user_input)
main()
