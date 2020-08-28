#!/bin/bash
file_path=$@
echo "compiling "$file_path
g++ $file_path.cpp -o $file_path
echo "Making executable for "$file_path
echo "Program output: "
echo
./$file_path
rm $file_path