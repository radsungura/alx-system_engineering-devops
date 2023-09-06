0. alias ls="rm *" : Create a script that creates an alias.Name: ls ;Value: rm *
1. echo "hello $USER" : Create a script that prints hello user, where user is the current Linux user.
2. PATH=$PATH:/action : Add /action to the PATH. /action should be the last directory the shell looks into when looking for a program
3. echo $PATH | tr ':' '\n' | wc -l : counts the number of directories in the PATH.
4. printenv :  Lists environment variables
5. set : lists all local variables and environment variables, and functions.
6. BEST="School" : Create a script that creates a new local variable.
7. export BEST="School" : Create a script that creates a new global variable.
8. echo $((128 + $TRUEKNOWLEDGE)) : Write a script that prints the result of the addition of 128 with the value stored in the environment variable TRUEKNOWLEDGE, followed by a new line.
9. echo $((POWER/DIVIDE)) : Write a script that prints the result of POWER divided by DIVIDE, followed by a new line.
10. echo $((BREATH**LOVE)) : Write a script that displays the result of BREATH to the power LOVE
11. echo $((2#$BINARY)) : Write a script that converts a number from base 2 to base 10.
12. echo {a..z}{a..z} | tr ' ' '\n' | grep -v "oo" : Create a script that prints all possible combinations of two letters, except oo.
13. printf '%.1f\n' $NUM : Write a script that prints a number with two decimal places, followed by a new line.
100. printf '%x\n' $DECIMAL : Write a script that converts a number from base 10 to base 16.
101. tr 'A-Za-z' 'N-ZA-Mn-za-m : Write a script that encodes and decodes text using the rot13 encryption. Assume ASCII.


