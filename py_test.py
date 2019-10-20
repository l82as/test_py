import subprocess as sub

def print_rez(f_in_date):
    try:
        k = sub.check_output("python programs_testing_python/prog_1.py", input=f_in_date, encoding='utf-8')
    # d=k.communicate(b"3")
    except:
        k='wrong'
    return k
f_in = open("case_test/case_1/input.txt","r")
f_out = open("case_test/case_1/output.txt","r")
l_answer=[]
for i in f_out:
    l_answer.append(i.replace(" ","\n"))
print(l_answer)
l_test=[]
for i in f_in:
    s=i.replace(" ","\n")
    l_test.append(print_rez(s))
#f_out = open("case_test/case_1/output.txt","r")

print(l_test)
count = 0
for i in range(len(l_test)):
    if l_test[i] == l_answer[i]:
        count+=1
    else:
        print('wrong answer-\n',l_test[i], 'rigth answer-\n', l_answer[i])
print('count rigth tests',count,'\nwrong tests', len(l_answer) - count)
f_in.close()
f_out.close()


