
file=open('Manish.txt','r')
data=file.readlines()  #list of lines
print(data)
file.close()
file=open('Manish.txt','a')
file.write("Hello Regex--")
file.close()
