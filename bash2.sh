# This bash file counts the number of files and subdirectories in the current directory

ls -l | grep -v ^d | wc -l
