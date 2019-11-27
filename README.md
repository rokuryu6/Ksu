# Ksu
 
a = float(input())
b = float(input())
op = input()
if(b == 0 and (op == "mod" or op == "/" or op == "div")):
    print("Деление на 0!")
elif(op == '+'):
    print(a + b)
elif(op == '-'):
    print(a - b)
elif(op == '*'):
    print(a * b)
elif(op == '/'):
    print(a / b)
elif(op == 'mod'):
    print(a % b)
elif(op == 'pow'):
    print(a ** b)
elif(op == 'div'):
    print(a // b)
else: print("Unknown operator")
