codingproblemtext1 = "aacabc"
secondvalue = 0
incrementer = 1
for x in range(1, 20):
    if codingproblemtext1[incrementer] == codingproblemtext1[secondvalue]:
        finalvalue = str(codingproblemtext1[secondvalue])
        print("we have stopped at " + finalvalue + " the length of the letters before a repetition is " + str(incrementer))
        break
    else:
        incrementer += 1
        secondvalue+=1
