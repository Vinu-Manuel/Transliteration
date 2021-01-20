
from hin_to_eng import *    # importing module
import string

def hte(sent):  # defining function
    punc = string.punctuation
    output = '' # defining output string
    for ltr in range(len(sent)): # for each character, determining its output depending on its linguistic nature
        if sent[ltr] in VS: # for various signs
            output += VS[sent[ltr]]

        elif sent[ltr] in IV: # for indendent vowels
            output += IV[sent[ltr]]
    
        elif sent[ltr] in C: # for consonants
            if ltr+1 == len(sent): # if it's the last character
                out = C[sent[ltr]]
                output += out[:-1]
            elif sent[ltr+1] in punc or sent[ltr+1] in DVS or sent[ltr+1] in DVS2 or sent[ltr+1] == "्" or sent[ltr+1] == " " or sent[ltr+1] == "़" :
                out = C[sent[ltr]]
                output += out[:-1]
            else:
                output += C[sent[ltr]]

        elif sent[ltr] in AC: # for additional consonants
            if ltr+1 == len(sent): # if it is the last character
                out = C[sent[ltr]]
                output += out[:-1]
            elif sent[ltr+1] in punc or sent[ltr+1] in DVS or sent[ltr+1] in DVS2 or sent[ltr+1] == "्" or sent[ltr+1] == " " or sent[ltr+1] == "़" :
                out = AC[sent[ltr]]
                output += out[:-1]
            else:
                output += AC[sent[ltr]]

    
        elif sent[ltr] in DVS: # for dependent vowel signs
            output += DVS[sent[ltr]]

        elif sent[ltr] in DVS2: # for additional vowel signs
            output += DVS2[sent[ltr]]
        
        elif sent[ltr] in V: # for virama
            output += V[sent[ltr]]

        elif sent[ltr] in VS2: # for vowel signs
            output += ""

        else: # for other characters
            output += sent[ltr]
    return output   # return output
