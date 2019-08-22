# regular expression solution - lifted from the internet
# echo "$@" | sed $'s/./&\\\n/g' | sed -ne $'x;H;${x;s/\\n//g;p;}'

# Lessons
# ${#string} gives length in characters
# parameter expansion - ${PARAMTER:OFFSET:LENGTH}
#        - OFFSET counts from beginning, unless negative
# += appends value to string


if [[ -z "$@" ]] ; then
        echo ""
        exit 0
else
        input=$@
        length=-${#input}
        for ((i=-1;i>=$length;i--)) ; do
                output+=${input:$i:1}
        done
        echo $output
fi
