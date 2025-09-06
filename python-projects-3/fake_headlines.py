import random

subjects=[
    'Erdogan',
    'Messi',
    'ronaldo',
    'vikings',
    'putin',
    'khabib'
]

actions=[
    'beats',
    'smashed',
    'dancing at party',
    'drinking tea at ',
    'laught at '
]

objects=[
    'Airport',
    'palace',
    'airplane',
    'computer',
    'woman',
    'donal trump'
]

while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    object=random.choice(objects)
    headline=f'Breaking news:{subject} {action} {object}'
    print('\n'+headline)
    user=input("Do you want another headline(yes\\no):").strip().lower()
    if user=='no':
        break
print("Gave over!")