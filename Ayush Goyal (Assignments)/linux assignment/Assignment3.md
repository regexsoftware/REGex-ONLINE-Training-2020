# Assignment 3 [Linux] [Ayush Goyal]

## 1. Create & compress the file with bzip2.
Bzip2 is a well known compression tool and it’s available on most if not all the major Linux distributions.             
```
	sudo apt install bzip2
	bzip2 option(s) filenames		#Creation
	bzip2 -z filename			#Compress
	bzip2 -z linux.tar			#Compress a tar file.
```

## 2. What should be the argument to be given to unzip that file.
**Use unzip:**             
```
	sudo apt install unzip
	unzip backup.zip
```

## 3. Read a file & show the data on terminal using file input & output redirection
```
	gedit information.txt		#Type the required info
	cat information.txt
	echo Name >>information.txt
```


## 4. How to change the shell of user to “/bin/sh” at the time of adding the user
```
	useradd -s /bin/sh <username>
Eg	useradd -s /bin/sh Matt
```
