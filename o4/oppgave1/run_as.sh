#!/bin/bash
file_path=$@
echo "compiling "$file_path
nasm -f elf64 $file_path.s
echo "Making executable for "$file_path
ld $file_path.o -o $file_path
echo "Program output: "
echo
echo
./$file_path
rm $file_path.o
rm $file_path