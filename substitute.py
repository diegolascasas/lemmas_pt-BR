import sys

def create_mapping(infile):
    mapping = {}
    for line in infile:
        word, sub = line.split()
        mapping[word] = sub
    return mapping

m = create_mapping(open(sys.argv[1]))
for line in sys.stdin:
    line = line.strip()
    try:
         print m[line]
    except KeyError:
         print line
