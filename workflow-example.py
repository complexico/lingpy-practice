# ALT + SHIFT + E for line execution
from lingpy import *

# load the .qlc data
lex = LexStat("data/KSL.qlc")
lex

# check the content of `lex`
## the concept
lex.rows ## all
lex.rows[0:3]

# cognates search
lexcog = LexStat('data/KSL.qlc', check=True)

# cognate judgement
lex.get_scorer()

# compute cognate sets
lex.cluster(method = "lexstat", threshold = 0.6, ref = "cognates")

# save output
lex.output('tsv', filename="data/KSL_new", ignore="all", prettify=False)

alm = Alignments(lex, ref="cognates")
alm.align()

alm.output('html', filename="KSL")