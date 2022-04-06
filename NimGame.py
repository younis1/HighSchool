b = 1 
while b == 1:
    
    import random
    print("")
    number = eval(input("Please enter the number you want to begin with between 20 and 100 "))
    while number < 20 or number > 100:
        print(" invalid number ")
        print("")
        number = eval(input("Please enter the number you want to begin with between 20 and 100 "))
    print("")
    step = eval(input("Please enter the step you want between 3 and 15 ..  "))
    while step < 3 or step > 15:
        print("invalid number")
        step = eval(input("Please enter the step you want between 3 and 15 ..  "))
    while (step * 3 ) > number:
        print("number should be more than  3 times the step")
        number = eval(input("Please enter the number you want to begin with between 20 and 100 "))
        while number < 20 or number > 100:
            print(" invalid number ")
            number = eval(input("Please enter the number you want to begin with between 20 and 100 "))
        step = eval(input("Please enter the step you want between 3 and 15 ..  "))
        while step < 3 or step > 15:
            print("invalid number")
            step = eval(input("Please enter the step you want between 3 and 15 ..  "))

    print("")
    start = int(input(" Press 1 to let the pc first ... press 2 to go first  "))
    while start != 1 and start != 2:
        print("invalid number")
        start = int(input(" Press 1 to let the pc first ... press 2 to go first  "))
    mod = (number - 1) % (step + 1)
    turn = 1
    choose = 0
    while number >1 and mod != 0 and start == 1 :
        print("")
        if turn == 1:
            choose = mod
            print (" PC chooses : ", mod)
            number -= choose
            turn +=1
            print("Remainder is ",number ) 
        elif turn % 2 == 0 :
            choose = eval(input("Please enter a number"))
            while choose <1 or choose > step or choose >= number:
                print(" invalid number ")
                choose = eval(input("Please enter a number"))
            number -= choose
            turn+= 1
            print("Remainder is ",number )
        

        elif turn % 2 != 0:
            choose = (step + 1) - choose
            print (" PC chooses : ", choose)
            turn += 1
            number -= choose
            print("Remainder is ",number )
    if number == 1 and mod != 0 and start == 1:
        print("")
        print(" YOU LOST !  ")
        print("")
    while number > 1 and mod == 0 and start == 2:
        print("")
        if turn % 2 != 0 :
            choose = eval(input("Please enter a number"))
            while choose <1 or choose > step or choose >= number:
                print(" invalid number ")
                choose = eval(input("Please enter a number"))
            number -= choose
            turn+= 1
            print("Remainder is ",number )
        elif turn % 2 == 0:
            choose = (step + 1 ) - choose
            print (" PC chooses : ", choose)
            turn += 1
            number -= choose
            print("Remainder is ",number )
    if number ==  1 and mod == 0 and start == 2:
        print("")
        print(" YOU LOST ! ")
        print("")

    while number > 1 and mod != 0 and start == 2:
        print("")
        anmod = (number - 1) % (step + 1)    
        if turn % 2 != 0:
            choose = eval(input("Please enter a number"))
            while choose <1 or choose > step or choose >= number:
                print(" invalid number ")
                choose = eval(input("Please enter a number"))
            number -= choose
            turn+= 1
            print("Remainder is ",number )
        elif turn % 2 == 0:
            if anmod <= step and anmod >=1 :
                choose =  anmod 
                print("PC chooses ", choose)
                turn +=1
                number -= choose
                print("Remainder is ",number )
            else:
                choose = random.randrange(1,step + 1)
                while choose >= number :
                    choose = random.randrange(1,step + 1)
                print("PC chooses ", choose)
                turn +=1
                number -= choose
                print("Remainder is ",number )
    if turn % 2 == 0 and mod != 0 and start == 2:
        print("")    
        print("You Win ! ")
        print("")
    elif turn % 2 != 0 and turn != 1 and mod != 0:
        print("")    
        print("You LOST !")
        print("")
    while number > 1 and mod == 0 and start == 1:
        print("")
        anmod = (number - 1) % (step + 1)
        if turn == 1:
            choose = random.randrange(1,step + 1)
            print("PC chooses ", choose)
            turn +=1
            number -= choose
            print("Remainder is ",number )
        elif turn % 2 == 0 :
            choose = eval(input("Please enter a number"))
            while choose <1 or choose > step or choose >= number:
                print(" invalid number ")
                choose = eval(input("Please enter a number"))
            number -= choose
            turn += 1
            print("Remainder is ",number )
        else:
            if  anmod<= step and anmod>=1 :
                choose =  anmod
                print("PC chooses ", choose)
                turn +=1
                number -= choose
                print("Remainder is ",number )
            else:
                choose = random.randrange(1,step + 1)
                while choose >= number :
                    choose = random.randrange(1,step + 1)
                print("PC chooses  ", choose)
                turn +=1
                number -= choose
                print("Remainder is ",number )
    if turn % 2 == 0 and number ==1 and mod == 0 and start == 1:
        print("")
        print("YOU LOST!")
        print("")    
    elif turn % 2 != 0 and number ==1 and mod == 0 and start == 1:
        print("")
        print("YOU WIN !")
        print("")
    b = eval(input("Press 1 to continue , or any other key to break "))
