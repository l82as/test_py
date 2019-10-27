import subprocess as sub
import os, openpyxl
wb = openpyxl.load_workbook('resalt.xlsx')
sheet = wb.active
sheet['A1'].value = 'FIO'
sheet['D1'].value = "task_3"
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

task_out = []
task_in=[]
fi = open("case_test/case_3/input.txt", "r")
fo = open("case_test/case_3/output.txt", "r")

for j in fi:
    task_in.append(j)
fi.close()

for j in fo:
    task_out.append(j)
fo.close()

#print(task_in)
#print(task_out)

stud_answer = {}
ls_answer = []
ex_i = 1
for i in stud_dic:
    ex_i += 1
    sheet['A'+str(ex_i)].value = i
    fg = os.listdir("test_file/" + i)
    print(fg)
    if "task_3.py" in fg:
        inp = "python test_file/" + i + "/task_3.py"
        for date in task_in:
            ls_answer.append(print_rez(date, inp))
    else:
        print(i, "No file")
    count = 0
   # print(ls_answer)
    for m in range(len(ls_answer)):
        if ls_answer[m] == task_out[m]:
            count += 1

    if len(ls_answer)==0:
        print(i, "No file")
        sheet['D' + str(ex_i)].value = "No file"

    else:
        print(i, count*5)
        sheet['D' + str(ex_i)].value = count*5
    ls_answer = []
wb.save('resalt.xlsx')