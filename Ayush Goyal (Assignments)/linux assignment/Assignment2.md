# Assignment 2 [Linux] [Ayush Goyal]

## 1.Change the Umask value for any user permanently.
Linux is a multiuser network operating system where same Shell is being accessed by several users. 
To provide a customized version of same Shell to everyone (user, script or process), a layer is inserted between 
actual shell and end user. In this layer several configuration files are used to create a user specific environment. 
Permanent umask setting is also configured in this layer. Based on requirement, umask setting can be configured 
in multiple levels. In order to configure umask setting correctly, we have to understand how shell is being accessed. 
A shell can be accessed in two ways; login and non-login.               

**Login shell**
This is the shell environment which user receives just after the login. It provides a customized interface to interact with system. 
It takes input command from user and display the result on standard output device. The command prompt which user receives 
just after the login is example of login shell.                

**Non-login shell**
This is the additional Shell interface which user accesses from login shell to perform a specific task. 
Since it is accessed from a login shell, it inherits all customized properties of parent (logged in) shell. 
But at the same time it is also a separate shell which allows us to override the default properties.
 Any terminal which we open in GUI to execute the command is the example of non-login shell.               

Based on targeted user and shell access type, permanent umask setting can be configured in four files.               

```grep umask /etc/bashrc		// This sets for non login shell.
umask 002```

```grep umask /etc/profile		// This sets it for login shell.
umask 002```

## 2.Add a new user without using adduser & useradd command

The one possible way is,            

Add an entry for the user in `/etc/passwd` file.            
Add an entry for the group in `/etc/group` file.             
Create the home directory for the added user.              
Set the new user password using the passwd command.                       

## 3.Can we change the Umask value to 0888. If yes, then how. If not then why ?
We can setup umask in `/etc/bashrc` or `/etc/profile` file for all users.               
By default most Linux distro set it to 0022 (022) or 0002 (002).            
Open `/etc/profile` or `~/.bashrc` file, enter:           
`vi /etc/profile`            
`umask 022`           
Save this file. Changes will take effect in the **next login**.                

## 4. How to add a new user with a Unique user id (e.g 1345) & check out the unique
Id of that user.               
We can use :                           
	``` sudo useradd -u 1345 <username>
               To check the ID we  can use :
	id -u <username>```

## 5. How to change the group of any folder. After this checkout the group name of the files present in that folder. Try to change the group of the folder & the files present in the same folder using a single command
The chgrp command changes the group ownership of given files.          
```chgrp [OPTIONS] GROUP FILE```             
GROUP, name of the new group or the group ID (GID).                                  
Numeric GID must be prefixed with the + symbol. FILE.., name of one or more files.             
To checkout the group name:                
```
	users <username>
eg:	users matt
	id -g -n matt	primary group
	id -G -n matt	secondary group
```
Also we can use:                    
```
	grep <username> /etc/group
eg:	grep matt /etc/group
```

To change group with a single command use :                   
```
	chgrp <options>  <group>  <file or fies>  
```
