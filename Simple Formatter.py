Spa = 0
while True:
    Desc = input()
    Res = ""
    if Desc == "e":
        break
    
    for x in Desc:
        if Spa > 0:
            Spa += 1
            Spa -= 2
        if Spa == 1:
            if x == " ":
                Res += "\n \n"
            else:
                Res += str(x)
        else:
            Res += str(x)
        if x == ".":
            Spa += 2
        elif x == "?":
            Spa += 2
        elif x == "!":
            Spa += 2
            
    print(Res)
    
