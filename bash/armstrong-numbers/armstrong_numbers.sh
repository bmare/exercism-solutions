#!/usr/bin/env bash
main () {
        for ((digit=0; digit <  "${#1}"; digit++)); do
                (( armnum+=$((${1:digit:1} ** ${#1})) ))
        done
        if (( $armnum == "$1" )); then
                echo "true"
        else
                echo "false"
        fi
}
main "$@"
