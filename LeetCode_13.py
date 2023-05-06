def romanToInt(s):
        num = 0
        s = s + " "
        i = 0
        flag = False
        while i < len(s):
            if s[i] == "I":
                    if  s[i + 1] == "V":
                        num += 4
                        flag = True

                    elif s[i + 1] == "X":
                        num += 9
                        flag = True
                    else:
                        num += 1


            if s[i] == "X":
                    if s[i + 1] == "L":
                        num += 40
                        flag = True
                    elif s[i + 1] == "C":
                        num += 90
                        flag = True
                    else:
                        num += 10


            if s[i] == "C":
                if s[i + 1] == "D":
                    num += 400
                    flag = True
                elif s[i + 1] == "M":
                    num += 900
                    flag = True
                else:
                    num += 100



            if s[i] == "L": num += 50
            if s[i] == "D": num += 500
            if s[i] == "M": num += 1000
            if s[i] == "V": num += 5

            print(num, ",",  i)
            if flag == True: i = i + 2
            if flag == False: i = i + 1
            flag = False
        return num

print(romanToInt("MCMXCVI"))