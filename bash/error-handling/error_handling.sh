#!/usr/bin/env bash
main() {
        if [[ $# -gt 1 ]] ; then
                exit 1
        fi
        if [[ -z "$1" ]] ; then
                echo "Usage: ./error_handling <greetee>" 
                exit 1
        fi
        echo "Hello, "$1""
}
main "$@"
