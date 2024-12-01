with open("wndmsg.txt",'r') as file :
    with open("registerpair.txt",'a') as file2 :
        i = 3
        inext = i + 2
        for line in file:
            if (i == inext) :
                file2.write(f"REGISTER_PAIR({line.strip()}),\n")
                inext = inext + 5
            i = i + 1