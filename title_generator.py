#!/usr/bin/env python

import sys, re, random

noun = ["regent", "officer", "chief", "engineer", "overlord"]
adj = ["grand", "high", "master", "electronics", "firmware", "chief", "super", "<adj> <adj>"]
ofnoun = ["FWEE", "kings", "things", "<adj> <ofnoun>", "stuffed tortoises"]
nounphrase = ["<adj> <noun>", "<noun> of <ofnoun>", "<noun>", "<adj> <nounphrase>"]

modobj = sys.modules[globals()['__name__']]

def expand_title(asdf):
    parts = []
    for s in asdf.split():
        matchobj = re.search('<(\w*)>', s)
        if matchobj:
            l = getattr(modobj, matchobj.group(1))
            rstr = random.choice(l)
            parts.append(expand_title(rstr)) # recurse!
        else: parts.append(s)
    return ' '.join(parts) # Stick it all together again

print expand_title("<nounphrase>")

