#!/bin/bash

mkdir -p winter/questions summer/questions
cat ${1} | grep --color "/question/" | cut -d '"' -f 2 | xargs -I{} curl -JO {}
ls -1 *.pdf | grep _s20_ | xargs -I{} mv {} summer/questions
ls -1 *.pdf | grep _w20_ | xargs -I{} mv {} winter/questions


mkdir -p winter/answers summer/answers
cat ${1} | grep --color "/answer/" | cut -d '"' -f 2 | xargs -I{} curl -JO {}
ls -1 *.pdf | grep _s20_ | xargs -I{} mv {} summer/answers
ls -1 *.pdf | grep _w20_ | xargs -I{} mv {} winter/answers