#! /usr/bin/env bash

main () {
        IFS=$'- ' read -a split_string <<< "$@"
        for word in "${split_string[@]}" ; do
               acronym+=${word:0:1}
        done                
        echo "${acronym^^}"
}
main "$@"
