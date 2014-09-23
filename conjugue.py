#coding: utf-8
import requests
from bs4 import BeautifulSoup
import regex as re
import fileinput

url = "http://linguistica.insite.com.br/mod_perl/conjugue"

def get_text(word):
    page = requests.get(url,params={"verbo":word.encode("latin1")})
    soup = BeautifulSoup(page.text)
    return soup.ul.get_text()

def parse(text):
    ## WARNING: This is VERY sensitive to formating.
    verblist = text.split("\n")
    conj = re.compile(u"\xa0",re.U)

    def get_conj(s):
        x = conj.search(s)
        if x: return s

    verbs = [get_conj(s) for s in verblist if get_conj(s) is not None]
    words = [v.split()[-1] if i < 57 else v.split()[-2] for i,v in enumerate(verbs)]

    return set(words)

def print_words(target,result):
    for w in result:
        print w.encode("utf-8"), target,

for tgt in fileinput.input():
    txt = get_text(tgt.decode("utf-8"))
    result = parse(txt)
    print_words(tgt,result)

# verbose regex: r"\b(eu)|(tu)|(ele)|(nós)|(vós)|(eles)|(infinitivo)|(gerúndio)|(particípio)\b",

