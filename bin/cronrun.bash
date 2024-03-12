#!/bin/bash

#  cronrun
#
#  Designed to load the correct module and execute the daily commands
#
#  usage: cronrun module "script"
#
#  Created by Sean Morrison on 2/20/24.

function usage
{
    local execName=$(basename $0)
    (
    echo "usage: $execName module 'script'"
    echo " "
    ) >&2
    exit 1
}

while getopts "h" flag; do
case "$flag" in
    h) usage;;
esac
done

ARG1=${@:$OPTIND:1}
ARG2=${@:$OPTIND+1:1}

module purge ;
export MODULE="$ARG1"
module load "$ARG1"
eval "$ARG2"
