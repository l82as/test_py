import random
import subprocess as sub
import os

def print_rez(f_in_date, py_file):
    k = sub.check_output(py_file, input=f_in_date, encoding='utf-8')
    # d=k.communicate(b"3")

    return k

adr_py = "python original_programs/prog_2.py"
for i in range(1, 5):
    #os.mkdir("case_test/case_"+str(i)+"/")
    f = open("case_test/case_2/input_"+str(i)+".txt", "w")
    f_o = open("case_test/case_2/output_"+str(i)+".txt", "w")

    a = random.randint(2, 100)
    b = random.randint(100, 110000)
    f.write(str(a) + " " + str(b) + "\n")
    strBin = (str(a) + " " + str(b))

    f_o.write(str(print_rez(strBin, adr_py)))

    f.close()
    f_o.close()
