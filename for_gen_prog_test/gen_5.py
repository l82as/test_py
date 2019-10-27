import random
import subprocess as sub
import os

def print_rez(f_in_date, py_file):
    k = sub.check_output(py_file, input=f_in_date, encoding='utf-8')
    # d=k.communicate(b"3")

    return k

f = open("../case_test/case_5/input.txt", "w")
f_o = open("../case_test/case_5/output.txt", "w")
adr_py = "python ../original_programs/prog_5.py"
for i in range(8):
    k = random.randint(100, 200)
    r = int(random.gauss(k, 15))
    g = int(random.gauss(k, 15))
    b = int(random.gauss(k, 15))
    f.write(str(r) + " " + str(g) +" "+ str(b) +"\n")
    strBin = str(r) + " " + str(g) +" "+ str(b) +"\n"

    f_o.write(str(print_rez(strBin, adr_py)))

f.close()
f_o.close()
