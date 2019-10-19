from subprocess import*
import time
import os
def start_program(f_input):
    k = Popen(["programs_testings\\testing.exe"], stdin=PIPE, stdout=PIPE, shell=True)

    start_time = time.perf_counter()
    h = k.communicate(input=f_input)[0].split()
    stop_time = time.perf_counter()
    print(int(h[0]), int(h[1]))
    print("time: ", round(stop_time - start_time, 10))
    #return h, start_time, stop_time

#start_program()
list_dir = os.listdir("case_test")
for i in list_dir:
    f_in = open("case_test/" + i + "/input.txt", "r")
    f_expected = open("case_test/" + i + "/output.txt", "r")
    list_case_in = []
    #start_program(f_in)

    for i in f_in:
        start_program(i.encode())



    f_in.close()
    f_expected.close()
'''


f_er = open("error.txt", "w")


f_er.close()
'''

