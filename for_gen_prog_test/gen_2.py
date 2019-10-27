import random as r
fi = open("../case_test/case_2/output.txt", "w")
fo = open("../case_test/case_2/input.txt", "w")
sout = ""
sin = ""
for i in range(5):
    a = r.randint(2, 1000)
    b = r.randint(2, 1000)
    sin = sin + str(a) + " " + str(b) + "\n"
    sout = sout + str(a + b) + " " + str(a * b) + "\n"
fi.write(sin)
fo.write(sout)
fi.close()
fo.close()


