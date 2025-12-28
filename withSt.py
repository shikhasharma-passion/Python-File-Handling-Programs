with open("myfile.txt","r") as file:
    data=file.read()
    print(data)

with open("myfile2.txt","w") as file:
    file.write("hye")

with open("myfile2.txt","a") as file:
    file.write("\nPython IsAmazing Programming Lang.")

# with open("file.txt","w") as file:
#     file.write("whatsup!!!")

with open("file.txt","r") as file:
    text = file.read()
    print(text)

with open("file.txt","w") as file:
    file.write("whatsup!!!")



with open("file.txt","a") as file:
    file.write("\nall good.")