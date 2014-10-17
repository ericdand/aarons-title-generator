#!/usr/bin/env python

import sys, re, random

titlenoun = ["regent", "programmer", "officer", "chief", "engineer", "overlord", "cowboy", "supervisor"]
adj = ["grand", "high", "master", "electronics", "firmware", "chief", "super", "head", "executive", "<adj> <adj>"]
ofnoun = ["bugs", "FWEE", "kings", "things", "<adj> <ofnoun>", "stuffed tortoises", "food"]
modifier = ["riding off into the night", "lover of <ofnoun>"]
nounphrase = ["<adj> <titlenoun>", "<titlenoun> of <ofnoun>", "<titlenoun>", "<adj> <nounphrase>", "<nounphrase>, <modifier>"]

modobj = sys.modules[globals()['__name__']]

def expand_title(asdf):
    parts = []
    for s in asdf.split():
        matchobj = re.search('<(\w*)>(.?)', s)
        if matchobj:
            l = getattr(modobj, matchobj.group(1))
            rstr = random.choice(l)
            parts.append(expand_title(rstr) + matchobj.group(2)) # recurse!
        else: parts.append(s)
    return ' '.join(parts) # Stick it all together again

if len(sys.argv) > 1: 
    for i in xrange(0, int(sys.argv[1])): print expand_title("<nounphrase>")
else: print expand_title("<nounphrase>")

