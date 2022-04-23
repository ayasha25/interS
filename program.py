def process(a,b):
    linear=0
    circular=0
    # len (a) == len (b)
    for i in range(len(a)):
        ascii_1=ord(a[i])
        ascii_2=ord(b[i])
        ascii_z=ord('z')
        ascii_a=ord('a')
        if ascii_1<=ascii_2:
            li=ascii_2-ascii_1
            cir=ascii_z-ascii_2+ascii_1-ascii_a+1
            if li<=cir:
                linear+=li
                circular+=li
            else:
                linear+=li
                circular+=cir
        else:
            li=ascii_1-ascii_2
            cir=ascii_z-ascii_1+ascii_2-ascii_a+1
            if li<=cir:
                linear+=li
                circular+=li
            else:
                linear+=li
                circular+=cir

    print(linear,circular)

# How to run->
# write this command in command line  "python3 python_assignment.py file.txt"
# and make sure that file.txt has input and is saved in the same folder as pyhton_assignment.py(this file)
import sys
with open(sys.argv[1], 'r') as f:
    contents = f.read()
# print (contents)
list=contents.split("\n")
for st in list:
    str=st.split(" ")
    a=str[0]
    b=str[1]
    process(a,b)
    # print(a,b) 
