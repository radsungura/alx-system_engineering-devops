0. alias ls="rm *" : Create a script that creates an alias.Name: ls ;Value: rm *
1. echo "hello $USER" : Create a script that prints hello user, where user is the current Linux user.
2. PATH=$PATH:/action : Add /action to the PATH. /action should be the last directory the shell looks into when looking for a program
3. echo $PATH | tr ':' '\n' | wc -l : counts the number of directories in the PATH.
4. printenv :  Lists environment variables
5. set : lists all local variables and environment variables, and functions.
6. BEST="School" : Create a script that creates a new local variable.
7. export BEST="School" : Create a script that creates a new global variable.
8. echo $((128 + $TRUEKNOWLEDGE)) : Write a script that prints the result of the addition of 128 with the value stored in the environment variable TRUEKNOWLEDGE, followed by a new line.
