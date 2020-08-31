#!/bin/bash
file_paths=$@
gcc -c -fPIC a_function.c more_functions.c                  # Create object files for the shared library
gcc -shared a_function.o more_functions.o -o libfunctions.so  # Create libfunctions.so from the object files
sudo cp libfunctions.so /usr/lib                              # Copy the library to the system library path
                                                              # You can delete /usr/lib/libfunctions.so after the exercise
