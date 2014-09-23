# -*- coding: utf-8
import regex 
import fileinput 

transformations = [
    (r"(.*)s\b",   r"\1\b"), 	# -S > [excluir]
    (r"(.*)ndo\b", r"\1r\b"), 	# -NDO > -R
    (r"(.*)ado\b", r"\1ar"),	# -ADO > -AR 
    (r"(.*)ido\b", r"\1er"),	# -IDO > -ER 
    (r"(.*)ou\b",  r"\1ar"),	# -OU > -AR 
    (r"(.*)eu\b",  r"\1er"),	# -EU > -ER 
    (r"(.*)iu\b",  r"\1ir"),	# -IU > -IR 
    (r"(.*)ram\b", r"\1r"),	# -RAM > -R 
    (r"(.*)vam\b", r"\1r"),	# -VAM > -R 
    (r"(.*)va\b",  r"\1r"),	# -VA > -R 
    (r"(.*)sse\b", r"\1r"),	# -SSE > -R 
    (r"(.*)ssem\b",r"\1r"),	# -SSEM > -R 
    (r"(.*)ada\b", r"\1ar"),	# -ADA > -AR 
    (r"(.*)ida\b", r"\1er"),	# -IDA > -ER 
    (r"(.*)çõe\b", r"\1ção"),	# -ÇÕE > -ÇÃO 
    (r"(.*)vei\b", r"\1vel"),	# -VEI > -VEL 
    (r"(.*)am\b",  r"\1ar"),	# -AM > -AR
    (r"(.*)uma\b", r"\1um"),	# -UMA > -UM 
    (r"(.*)uns\b", r"\1um"),	# -UNS > -UM 
    (r"(.*)un\b",  r"\1um"),	# -UN > -UM  
    (r"(.*)rem\b", r"\1r"),	# -REM > -R 
    (r"(.*)ore\b", r"\1or"),	# -ORE > -OR 
    (r"(.*)ai\b",  r"\1al"),	# -AI > -AL 
    (r"(.*)ei\b",  r"\1ar"),	# -EI > -AR 
    (r"(.*)mo\b",  r"\1r"),	# -MO > -R
    (r"(.*)õe\b",  r"\1ão"),	# -ÕE > -ÃO 
    (r"(.*)ria\b", r"\1r"),	# -RIA > -R 
    (r"(.*)are\b", r"\1ar"),	# -ARE > -AR 
    (r"(.*)rá\b",  r"\1r"),	# -RÁ > -R 
    (r"(.*)ica\b", r"\1ico"),	# -ICA > -ICO 
    (r"(.*)osa\b", r"\1oso"),	# -OSA > -OSO 
    (r"(.*)eira\b",r"\1eiro"),	# -EIRA > -EIRO 
    (r"(.*)ze\b",  r"\1z"),	# -ZE > -Z 
    (r"(.*)ído\b", r"\1ir"),	# -ÍDO > -IR 
    (r"(.*)ída\b", r"\1ir"),	# -ÍDA > -IR 
    (r"(.*)ere\b", r"\1er"),	# -ERE > -ER 
    (r"(.*)ãe\b",  r"\1ão"),	# -ÃE > -ÃO 
]

substitute = regex.sub
for line in fileinput.input():
    for target, replace in transformations:
        line = substitute(target,replace,line)
    print line, # fileinput also gets the newline

