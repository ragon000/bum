#!/bin/bash
convert  $1 -level 0%,100%,0.2  $1
printf "\e]20;$1;\a"
