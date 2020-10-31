N = int(input())
num1 = 0
name = list(range(N))

for i in range(N):
    name[num1] = str(input())
    num1 += 1
    
t=0

for x in range(len(name)):
    length = name[t]
    leng = len(length)
    y = 0
    while y < leng:
        if length[y]=="a" or length[y]=="A":
            print("Hi! ", end = "")
        elif length[y]=="e" or length[y]=="E":
            print("Bye! ", end = "")
        elif length[y]=="i" or length[y]=="I":
            print("How are you? ", end = "")
        elif length[y]=="o" or length[y]=="O":
            print("Follow me! ", end = "")
        elif length[y]=="u" or length[y]=="U":
            print("Help! ", end = "")
        elif length[y]=="0" or length[y]=="1" or length[y]=="2" or length[y]=="3" or length[y]=="4" or length[y]=="5" or length[y]=="6" or length[y]=="7" or length[y]=="8" or length[y]=="9":
            print("Yes! ", end = "")
        else: 
            pass
        y+=1
    print("")
    t += 1
