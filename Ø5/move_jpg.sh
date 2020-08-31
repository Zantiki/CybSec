#!/bin/bash
JPGDIR=`dirname $1`/jpgs
#Opprett hvis den ikke fins fra før
if [ ! -d $JPGDIR ] ; then mkdir $JPGDIR ; fi
#Flytt filen
mv $1 $JPGDIR