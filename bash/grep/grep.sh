#! /usr/bin/env bash
#grep [OPTIONS] PATTERN [FILE...]
main () {
        output_lines=""
        mapfile -t input_lines < "$3"
        for line in "${input_lines[@]}"; do
                if [[ ${input_lines[line]}  == *"$2"* ]]; then
                        outputlines+=("${input_lines[line]}")
                fi
        done

        while :; do
                case $1 in
                        -n) #print line numbers
                                declare -i number=1
                                for line in "${input_lines[@]}" ; do
                                        input_lines[line]="${input_lines/#/"$number"}"
                                        number++
                                done
                                echo "${input_lines[0]}"
                                ;;
                        -l) #file names
                                output="$3"
                                ;;
                        -i) #case-insensitive
                                ;;
                        -v) #fail to match
                                ;;
                        -x) #entire line
                                ;;
                        *)
                                break
                esac
                shift
        done
        IFS=$'\n'
        echo "${input_lines[*]}" # expand array as a single word, with IFS as separator
                
}
main "$@"
