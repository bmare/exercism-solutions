#!/usr/bin/env bash
shopt -s extglob
IFS=$'\n'
set -f

main () {
        current_dir="./"
        touch notes.md ; chmod a=r, u+w notes.md
        # Lists all files in current directory
        for i in $( find "$current_dir" -maxdepth 2 -name '*.py' ! -name '*test*' ) ; do
                {
                        echo "$i" 
                        echo "\`\`\`" ; cat "$i"
                        echo "\`\`\`" 
                } >> notes.md
        done
        cat ./notes.md  
}
main "$@"


