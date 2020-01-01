#!/usr/bin/env bash
shopt -s extglob 
input="${1##*( )}"
input="${1%%*( )}" 
main () {
        case "$input" in
                *\?) echo "question" ;;
                !([[:alnum:]])) echo "silence" ;;
                [[:upper::]]) echo "shouting" ;;
                *) echo "Not question." ;;
                #+([[:space:]]|)) echo "Fine. Be that way!" ;;
                #[[:lower:]]{\?,\?[[:space:]]}) echo "Sure." ;;
                #[[:upper:]]+(\?|\?[[:space:]])) echo "Calm down, I know what I'm doing!" ;;
                #*[[:upper:]]+(!|)) echo  "Whoa, chill out!" ;;
                #*) echo "Whatever." ;; 
        esac
}
main "$@"



# Questions and Comments
# shopt -s extglob allows extended globs, important that this is outside main()
#string="${1##*( )}" string="${1%%*( )}" #strip leading, trailing whitespace
# With the case statement, does order matter like in an if...else statement?
# does [[:upper:]] match a single upper-case character or only upper case characters? 
# Might be easier to match only upper-case, by barring out only lower-case
