#!/bin/bash
## Applies all the lemmatization in a word count csv (arg $1, format: "[word]",[count]\n).
## Relies on a substitution script, a file with the word substitutions, a transformation script and a file with the white-list of the transformations.
## Outputs a csv with format "[lemmatized word]","[original word]",[count]\n.


cut -f 1 -d , $1  \
    | sed 's/"//g' \
    | python substitute.py data/verb_substitutions.txt \
    | python transform.py \
    | sed 's/^\(.*\)$/"\1"/g' \
    | paste -d , - $1
