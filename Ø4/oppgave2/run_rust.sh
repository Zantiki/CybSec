#!/bin/bash
file_path=$@
echo "compiling "$file_path
rustc $file_path.rs
echo "Program output: "
echo
./$file_path
rm $file_path