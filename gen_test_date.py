import random
import os
for i in range(1, 11):
    #os.mkdir("case_test/case_"+str(i)+"/")
    f = open("case_test/case_"+str(i)+"/input.txt", "w")
    f_o = open("case_test/case_"+str(i)+"/output.txt", "w")
    for j in range(10):
        a = random.randint(2, 10)
        b = random.randint(4,12)
        f.write(str(a) +" "+str(b) + "\n")
        f_o.write(str(a * b) + " " + str(a+b)+"\n")
    f.close()
    f_o.close()
