#!/bin/bash
file_path=o6/testing/fuzz_test

echo "compiling "$file_path
clang -g -O1 -fsanitize=fuzzer,address -o $file_path $file_path.c
echo "Making executable for "$file_path
echo "Program output: "
echo
exec ./$file_path -max_total_time=20
exit_code=$?
sleep 3
rm $file_path
exit $exit_code
