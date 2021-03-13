print('''
   _____      _            _       _             
  / ____|    | |          | |     | |            
 | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
 | |___| (_| | | (__| |_| | | (_| | || (_) | |   
  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|  by: akayo-san
    ''')

print("1.Multipication(*)\n2.division(/)\n3.sum(+)\n4.taking away(-)")
a = int(input("Choose this option: "))
if a == 1:
    num_1 = int(input("enter first number: "))
    num_2 = int(input("enter second number: "))
    print("Result: ", num_1 * num_2)
elif a == 2:
    num_1 = int(input("enter first number: "))
    num_2 = int(input("enter second number: "))
    print("Result: ", num_1 / num_2)
elif a == 3:
    num_1 = int(input("enter first number: "))
    num_2 = int(input("enter second number: "))
    print("Result: ", num_1 + num_2)
elif a == 4:
    num_1 = int(input("enter first number: "))
    num_2 = int(input("enter second number: "))
    print("Result: ", num_1 - num_2)
else:
    print("incorrect unswer\n Please try again")