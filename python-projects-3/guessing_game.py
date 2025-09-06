import random

easy_words=['king','queen','wow','you']
medium_words=['mrzahid','misssumaiya','bellahid']
hard_words=['mrfaisu07','captain911','biology']

print("--------- wellcome to guessing game --------------")
option=input('choose the guessing word level(easy,medium,hard:')
if option.lower() =='easy':
    secret=random.choice(easy_words)
elif option.lower() =='medium':
    secret=random.choice(medium_words)
elif option.lower() =='hard':
    secret=random.choice(hard_words)
else:
    print("invalid level","Default to easy words")
    secret=random.choice(easy_words)
attempt=0
print(secret)
while True:
    attempt+=1
    user=input('enter the guessing word:')
    if user==secret:
        print(f'congratulation matched in {attempt} attempts')
        break
    else:
        hint=''
        for i in range(len(secret)):
            if i<len(user) and user[i]==secret[i]:
                hint+=user[i]
            else:
                hint+='-'
        print('hint:',hint)

    
