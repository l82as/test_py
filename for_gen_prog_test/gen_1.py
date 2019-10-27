import random
import subprocess as sub
import os

def print_rez(f_in_date, py_file):
    k = sub.check_output(py_file, input=f_in_date, encoding='utf-8')
    # d=k.communicate(b"3")

    return k
f = open("../case_test/case_1/input.txt", "w")
f_o = open("../case_test/case_1/output.txt", "w")
adr_py = "python ../original_programs/prog_1.py"
for i in range(1, 5):
    #os.mkdir("case_test/case_"+str(i)+"/")

    k = random.randint(2, 1000)
    t = random.randint(100, 110000)
    strBin = (str(k) + "\n" + str(t) + "\n")
    f.write(strBin)


    f_o.write(str(print_rez(strBin, adr_py)))

f.close()
f_o.close()
