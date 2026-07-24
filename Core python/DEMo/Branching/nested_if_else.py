gender = (input('Enter gender(m/f):'))
age = int(input('Enter age:'))

if(gender == 'f'):
    if(age >= 18):
        print('Girl is eligibal for marriage.')
    else:
        print('Pehle Padhai kar lo.')
else:
    if(age >= 21):
        print('boy are eligible for marriage.')
    else:
        print('kuch kam lo yr.')
