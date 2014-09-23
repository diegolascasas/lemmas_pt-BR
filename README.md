
Python/Bash scripts to apply lemmatization methods to brazilian portuguese texts.
Rules and substitutions are still under development.

scripts:
- **apply_lematization.sh:** Main script, built to work in a word-count csv.
- **substitute.py:** Takes a file with a list of (target, substitution) word pairs as argument and executes these substitutions in a list of words given as stdin. 
- **transform.py:** Executes rule-based transformations on regular forms
- **conjugue.py:** Uses the [conjugue API](http://linguistica.insite.com.br/mod_perl/conjugue) to get word pairs realted to verb conjugations.


data:
- **data/verb_substitutions.txt:** the (target, substitution) list fed to *substitute.py* in the *apply_lematization.sh* script.
