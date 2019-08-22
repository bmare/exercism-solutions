#!/usr/bin/env bash

main() {
        alphabet="abcdefghijklmnopqrstuvwxyz"
        input="${1,,}"
        for (( i=0 ; i  < 26 ; i++ )) ; do
                if [[ "${input}"  != *"${alphabet:i:1}"* ]] ; then
                        echo "false"
                        exit 0 
                fi
        done
        echo "true"
}
main "$@"
