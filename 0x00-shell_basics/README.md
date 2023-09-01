0. pwd: prints the absolute path name of the current working directory
1. ls: Display the contents list of your current directory
2. cd: changes the working directory to the user’s home directory
3. ls -l: Display current directory contents in a long format
4. ls -la: Display current directory contents, including hidden files (starting with .). Use the long format
5. ls -an: Display current directory contents
6. mkdir /tmp/my_first_directory/: Creates a directory named my_first_directory in the /tmp/ directory
7. mv /tmp/betty /tmp/my_first_directory: Move the file betty from /tmp/ to /tmp/my_first_directory
8. rm -r /tmp/my_first_directory/betty: delete the file betty in /tmp/my_first_directory
9. rm -r /tmp/my_first_directory: Delete the directory my_first_directory that is in the /tmp directory
10. cd -: Changes the working directory to the previous one
11. ls -al . .. /boot: Lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format
12. file /tmp/iamafile: Prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script
13. ln -s /bin/ls __ls__: Create a symbolic link to /bin/ls, named __ls__. The symbolic link should be created in the current working directory
