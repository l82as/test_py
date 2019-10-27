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
task_in = {}
task_out = {}
dir_test = os.listdir("case_test")
for i in dir_test:
    dir_test1 = os.listdir("case_test/" + i)
    fi=open( "case_test/"+ i +"/" + dir_test1[0],"r")
    fo = open( "case_test/"+ i +"/" + dir_test1[1],"r")
    task_in[i] = []
    task_out[i] = []
    for j in fi:
        task_in[i].append(j)
    fi.close()
    for j in fo:
        task_out[i].append(j)
    fo.close()
print(task_in["case_"+ str(1)])
#print(task_out)
stud_answer = {}
for i in stud_dic:
    stud_answer[i]=[]

    print(i)
    for j in stud_dic[i]:
        inp = "python test_file/"+i+"/"+j
        out  = task_in["case_"+j[-4]]
        for date in out:
            print(inp, date)

            print(print_rez(date, inp))