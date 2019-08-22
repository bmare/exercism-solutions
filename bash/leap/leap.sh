# Regular expression for positive integers
number='^[0-9]+$'

if [[ -z "$1" ]]; then
        echo "Usage: leap.sh <year>"
        exit 1
elif ! [[ $1 =~ $number ]] ; then
        echo "Usage: leap.sh <year>"
        exit 1
elif  [[ $# -gt 1 ]] ; then
        echo "Usage: leap.sh <year>"
        exit 1
elif  (( $1 % 400 == 0 ))  ; then
        echo 'true'
elif  (( $1 % 4 == 0 )) && (( $1 % 100 != 0 )) ; then
        echo 'true'
else 
        echo 'false'
fi

