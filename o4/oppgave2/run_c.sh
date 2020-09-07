#!/bin/bash
file_path=$@
echo "compiling "$file_path
gcc -o $file_path $file_path.c
echo "Making executable for "$file_path
# ld $file_path.o -o $file_path
echo "Program output: "
echo
./$file_path
sleep 3
# rm $file_path
