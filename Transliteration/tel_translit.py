
from tel_to_eng import *    # importing module
import string

def tte(sent):  # defining function
    output = '' # defining empty string
    punc = string.punctuation
    
    for ltr in range(len(sent)):    # for each character, determining its output depending on its linguistic nature
        if sent[ltr] in VS: # for various signs
            output += VS[sent[ltr]]

        elif sent[ltr] in IV:   # for independent vowels
            output += IV[sent[ltr]]
    
        elif sent[ltr] in C:    # for consonants
            if ltr+1 == len(sent): # if its the last character
                output += C[sent[ltr]]
            elif sent[ltr+1] in DD or sent[ltr+1] == "్" :
                out = C[sent[ltr]]
                output += out[:-1]
            else:
                output += C[sent[ltr]]
    
        elif sent[ltr] in DD: # for dependent vowel signs
            output += DD[sent[ltr]]

        elif sent[ltr] in V: # for virama
            output += V[sent[ltr]]

        else:   # for other characters
            output += sent[ltr]
    return output   # return output

