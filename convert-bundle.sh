#!/bin/bash
set -euo pipefail

curl https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz > lab3-bundle.tar.gz
tar -xzvf lab3-bundle.tar.gz

awk '!/^[[:space:]]*$/' lab3_data.tsv > cleaned_lab3_data.tsv
tr '\t' ',' < cleaned_lab3_data.tsv > lab3_data.csv
WORDCOUNT=$(wc -l <  lab3_data.csv)
DATACOUNT=$((WORDCOUNT - 1))
echo "$DATACOUNT"
tar -czvf converted-archive.tar.gz lab3_data.csv
