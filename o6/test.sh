#!/bin/bash
echo I am a test
exit_code=1
file_path=o6/testing/string_test
echo "compiling "$file_path
gcc -o $file_path $file_path.c
echo "Making executable for "$file_path
# ld $file_path.o -o $file_path
echo "Program output: "
echo
./$file_path
exit_code=$?
rm $file_path
sleep 3
exit $exit_code