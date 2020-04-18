file=open('Sharma.txt','r')
data=file.readlines()  #list of lines
print(data)
file.close()
file=open('Sharma.txt','a')
file.write(" Manish  Learning good from Regex.")
file.close()
