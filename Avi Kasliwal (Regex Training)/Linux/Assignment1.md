# Assignment 1 [Linux] [Avi Kasliwal]

## 1. When we create a user, some hidden files are generated in the directory of the same user at that time. How is it done ?
UNIX allows users to have files which are not listed, by default, by the ls command.
These are called hidden files and are distinguishable from other files by the fact that their 
filenames begin with a dot `(.)`. Such a file is .profile which is executed every time you log in 
to the system.           
Hidden files are listed by adding the -a option to the ls command.The useradd is a low level 
utility for adding users.           
Also adduser is a friendlier frontend to useradd and will do things like create user 
directories by default.                
This is why it dosen't show on frontend utility and therefore kept hidden i.e in the home directory.        
              
## 2. Make subdirectories inside a parent directory by using single mkdir command (refer to the figure given)

`mkdir -p A/{dir1,dir2,B/{C/dir3}}`
   
## 3.tac command vs cat command
**Cat** command, acronym for Concatenate, is one of the most used commands in *nix systems. 
The most basic usage of the command is to read files and display them to stdout, meaning to display 
the content of files on your terminal.
On the other hand, a lesser known and less used command in *nix systems is tac command.        
**Tac** is practically the reverse version of cat command (also spelled backwards) which prints each line 
of a file starting from the bottom line and finishing on the top line to your machine standard output.




