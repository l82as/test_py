import random
import subprocess as sub
import os

def print_rez(f_in_date, py_file):
    k = sub.check_output(py_file, input=f_in_date, encoding='utf-8')
    # d=k.communicate(b"3")

    return k


adr_py = "python ../original_programs/prog_4.py"

for i in range(1, 11):
    #os.mkdir("case_test/case_"+str(i)+"/")
    f = open("../case_test/case_4/input_"+str(i)+".txt", "w")
    f_o = open("../case_test/case_4/output_"+str(i)+".txt", "w")

    s = random.randint(2, 6)*10
    n = random.randint(5, 15)
    strBin = str(s) + "\n" + str(n) + "\n"
    for i in range(n):
        strBin = strBin + str(random.randint(3, 20)) + "\n"
    f.write(strBin)


    f_o.write(str(print_rez(strBin, adr_py)))

    f.close()
    f_o.close()
