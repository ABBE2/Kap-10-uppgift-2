a = int(input('vilken storlek ska boxen ha?'))

def box(a):
    print(a*'==='+'======')
    for i in range(a):
             print("||",a*"   ", "||")
    print(a*'==='+'======')

box(a)