import subprocess as sub
import os

def print_rez(f_in_date, py_file):
    try:
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
task_i = []
task_out = []
task_in=[]
fi = open("case_test/case_1/input.txt", "r")
fo = open("case_test/case_1/output.txt", "r")

for j in fi:
    task_i.append(j)
fi.close()
for i in range(0, len(task_i),2):
    task_in.append(task_i[i]+task_i[i+1])
for j in fo:
    task_out.append(j)
fo.close()

#print(task_in)
#print(task_out)

stud_answer = {}
ls_answer = []
for i in stud_dic:
    count=0
    stud_answer[i]=[]

    #print(i)
    for j in stud_dic[i]:
        ls_answer = []
        try:
            inp = "python test_file/"+i+"/task_1.py"
            for date in task_in:
                #print(inp, date)
                ls_answer.append(print_rez(date, inp))
        except:
            print("NO file")
    #print(ls_answer)
    for m in  range(len(ls_answer)):
        if ls_answer[m] == task_out[m]:
            count += 1
    print(i, count*5)
