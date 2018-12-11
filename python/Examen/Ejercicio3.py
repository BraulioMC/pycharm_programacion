print("#### CALCULATOR 2000 ####")

count = 0.0


while True:
    try:
        print("R: " + count)
        num = input()
        if num.find("C") != -1 or num.find("c") != -1:
            count = 0
            print("R: " + count)
        elif num.find("+"):
            count = count + num
        elif num.find("-"):
            count = count - num
        elif count = coun
    except KeyboardInterrupt:
        print("Have a great day!!!")
