import random
import subprocess as sub
import os

def print_rez(f_in_date, py_file):
    k = sub.check_output(py_file, input=f_in_date, encoding='utf-8')
    # d=k.communicate(b"3")

    return k

adr_py = "python ../original_programs/prog_3.py"
f = open("../case_test/case_3/input.txt", "w")
f_o = open("../case_test/case_3/output.txt", "w")
so =""
for i in range(6):
    a = random.randint(100, 1100000000)
    f.write(str(a)+"\n")
    strBin = (str(a))
    so = so + str(print_rez(strBin, adr_py))
f_o.write(so)

f.close()
f_o.close()
