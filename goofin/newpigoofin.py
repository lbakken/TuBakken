n = input ('need math help?\n')
if n == 'yes':
    w = input('what kind of math?\n')
    if w == '+':
        x = float(input('sweet, what are you adding?: \n'))
        y = float(input('and?:\n'))
        z = x + y
        print ('{} + {} = {}'.format(x,y,z))
    elif w == '-':
        x = float(input('sweet, what are you subtracting?: \n'))
        y = float(input('what else: \n'))
        z = x - y
        print ('{} - {} = {}'.format(x,y,z))
    elif w == '/':
        x = float(input('yeet, what are you dividing?: \n'))
        y = float(input('what else bro?:\n'))
        if y == 0:
            print ('not so fast, you cannot divide by 0... nerd')
        else:
            z = x / y
            print ('{} / {} = {}'.format(x,y,z))
    elif w == '*':
        x = float(input('sko, what are you muliplying?: \n'))
        y = float(input('and?: \n'))
        z = x * y
        print ('{} * {} = {}'.format(x,y,z))
else:
    print ('oofv screw me i guess')