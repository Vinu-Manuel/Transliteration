
from mal_to_eng import * # importing module
import string

def mte(sent):  # defining function
    punc = string.punctuation
    output = '' # defining output string
    for ltr in range(len(sent)):    # for each character, determining its output depending on its linguistic nature
        if sent[ltr] in VS: # for various signs
            output += VS[sent[ltr]]

        elif sent[ltr] in IV:   # for indepenent vowels
            output += IV[sent[ltr]]
    
        elif sent[ltr] in conso:    # for consonants
            if ltr+1 == len(sent):  # if it's the last character
                output += conso[sent[ltr]]
            elif sent[ltr+1] in DVS or sent[ltr+1] in TPVS or sent[ltr+1] == "്" :
                out = conso[sent[ltr]]
                output += out[:-1]
            else:
                output += conso[sent[ltr]]
    
        elif sent[ltr] in DVS:  # for dependent vowel signs
            output += DVS[sent[ltr]]

        elif sent[ltr] in TPVS: # for two-part dependent vowel signs
            output += TPVS[sent[ltr]]

        elif sent[ltr] in chillu: # for chillu consonants
            output += chillu[sent[ltr]]

        elif sent[ltr] in chandra: # for virama/chandrakala
            output += chandra[sent[ltr]]

        else: # for other characters
            output += sent[ltr]
    return output   # return output

