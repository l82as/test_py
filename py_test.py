import subprocess as sub

f_in = open("../input.txt","r")
f_out = open("../output.txt","w")
f_er = open("../error.txt", "w")
k= sub.Popen("../testing.exe",stdin=sub.PIPE, stdout=f_out, shell = True)
#k = call("testing.exe", stdin=f_in, stdout=f_out, shell=True)

#print(k.communicate(input=b'7\n'))


f_in.close()
f_out.close()
f_er.close()

