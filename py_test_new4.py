import subprocess as sub
import os, openpyxl
wb = openpyxl.load_workbook('resalt.xlsx')
sheet = wb.active
sheet['A1'].value = 'FIO'
sheet['E1'].value = "task_4"
print(sheet['A1'].value)

def print_rez(f_in_date, py_file):
    try:
        #print( py_file)
        k = sub.check_output(py_file, input=f_in_date, encoding='utf-8')
    # d=k.communicate(b"3")
    except:
        k='wrong'

    return k

list_prog = os.listdir("test_file")
stud_dic ={}
for i in list_prog:
    stud_dic[i]=[]
    list_p1 = os.listdir("test_file/" + i)
   # print(i)
    for j in list_p1:
        stud_dic[i].append(j)
#print(stud_dic)

task_out = ""
task_in=""
fi = open("case_test/case_4/input.txt", "r")
fo = open("case_test/case_4/output.txt", "r")

for j in fi:
    task_in = task_in + j
fi.close()
task_in = [task_in]
for j in fo:
    task_out = task_out + j
fo.close()
task_out = [task_out]
for i in range(1, 10):
    task_o = ""
    task_i = ""
    fi = open("case_test/case_4/input_" + str(i) + ".txt", "r")
    fo = open("case_test/case_4/output_" + str(i) + ".txt", "r")
    for j in fi:
        task_i = task_i + j
    fi.close()

    for j in fo:
        task_o = task_o + j
    fo.close()
    task_in.append(task_i)
    task_out.append(task_o)
stud_answer = {}
ls_answer = []
ex_i = 1
for i in stud_dic:
    ex_i += 1
    sheet['A'+str(ex_i)].value = i
    fg = os.listdir("test_file/" + i)
    if "task_4.py" in fg:

        inp = "python test_file/" + i + "/task_4.py"
        for date in task_in:
            ls_answer.append(print_rez(date, inp))
    else:
        print(i, "No file")

    if len(ls_answer) == 0:
        print(i, "No file")
        sheet['E' + str(ex_i)].value = "No file"
    else:
        count = 0
        for m in range(len(ls_answer)):
            if ls_answer[m] == task_out[m]:
                count += 1
        print(i, count*5)
        sheet['E' + str(ex_i)].value = count*5
    ls_answer = []
wb.save('resalt.xlsx')