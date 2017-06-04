#!/bin/bash
for oldname in $(cd /vagrant_data/python-scripts/scripts/ && ls -lthr practice_*|awk '{print $NF}'); do 
    newname=$(echo ${oldname}|sed  "s#practice_##g")
    mv ${oldname}  ${newname}
done
