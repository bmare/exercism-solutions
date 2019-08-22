#!/usr/bin/env bash
main() {
        declare -i output=
        if (( ${#1} -ne ${#2} )) ; then
                echo "left and right strands must be of equal length"
                exit 1
        elif [[ -z "$@" ]] ; then
                echo "Usage: hamming.sh <string1> <string2>"
                exit 1
        fi
        for  ((i=0 ; i < ${#1} ; i++)) ; do
                if [[ ${1:i:1} != ${2:i:1} ]] ; then
                        output+=1
                fi
        done
        echo "$output"
}
main "$@"
