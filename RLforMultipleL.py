# for reading multiple lines by using readline()method we need to use loop

# f = open ("myfile.txt","r")
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)

# f = open("myfile3.txt","r")
# while True:
#     line=f.readline()
#     print(line)
#     if not line:
#         print(line,type(line))
#         break



f = open("myfile.txt","r")
while True:
    line = f.readline()
    print(line)
    if not line:
        print(line, type(line))
        break



