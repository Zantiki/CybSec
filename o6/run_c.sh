#!/bin/bash
file_path=testing/fuzz_test
echo "compiling "$file_path
# gcc -fsanitize=address -ggdb -o test test.c
clang -fsanitize=fuzzer -ggdb -o $file_path $file_path.c
echo "Making executable for "$file_path
# ld $file_path.o -o $file_path
echo "Program output: "
echo
./$file_path -max_total_time=20
sleep 3
# rm $file_path
