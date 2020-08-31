#!/bin/bash
find imgs  ! -path "*/jpgs/*" -name "*.jpg" -exec ./move_jpg.sh {} \;