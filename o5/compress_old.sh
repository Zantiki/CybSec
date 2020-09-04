#!/bin/bash

compression_limit=5

files=$(find  ~/oving3 -mtime +$compression_limit -size +10k -print)

echo $files

for value in $files
do
    gzip $value
    files=$(find  ~/oving3 -mtime +$compression_limit -print)
done
# ls -la -R pyprojects