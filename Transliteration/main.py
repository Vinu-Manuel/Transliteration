
from flask import Flask     # importing modules
from flask import render_template, request, redirect
from mal_translit import *
from hin_translit import *
from tel_translit import *
import re

app = Flask(__name__)   # creating a webpage

@app.route("/", methods=["POST","GET"]) # providing route
def home():     # defining the page
    if request.method == "POST":    # if request already provided
        itext = request.form["ilan"]    # collect text and language input 
        ilang = request.form["language"]
        if ilang == "mal":  # if language is Malayalam
            m = mte(itext)  # execute function mte()
        elif ilang == "hin":    # if language is Hindi
            m = hte(itext)  # execute function hte()
        elif ilang == "tel":    # if language is Telugu
            m = tte(itext)  # execute function tte()
        else:   # else to detect language
            lang = [] # defining empty list
            for i in range(len(itext)): # for in range the total character length of text input
                if re.search("([\u0D00-\u0D7F]+)",itext[i]) != None: # searching if character belongs to the unicode range of Malayalam
                    if "mal" not in lang: 
                        lang.append("mal") # adding "mal" to list
                if re.search("([\u0C00-\u0C7F]+)",itext[i]) != None: # searching if character belongs to the unicode range of Telugu
                    if "tel" not in lang:
                        lang.append("tel") # adding "tel" to list
                if re.search("([\u0900-\u097F]+)",itext[i]) != None: # searching if character belongs to the unicode range of Hindi
                    if "hin" not in lang:
                        lang.append("hin") # adding "hin" to list
            if len(lang) > 1: # if multiple languages detected
                m = "Please input only one language"
            elif len(lang) == 0: # if any other/no languages detected
                m = "Currently, language detection only available for Hindi, Malayalam and Telugu"
            elif lang[0] == "mal": # if Malayalam detected, execute function mte()
                m = mte(itext)
            elif lang[0] == "tel": # if Telugu detected, execute function tte()
                m = tte(itext)
            elif lang[0] == "hin": # if Hindi detected, execute function hte()
                m = hte(itext)
        o = "Original Text: "   # defining strings
        t = "Transliteration: "
        return render_template("index.html", m=m, itext=itext, o=o, t=t) # render HTML template
    else: # for fresh loading of webpage
        return render_template("index.html")    # render HTML template



if __name__ == "__main__":  # for running the webpage
    app.run()



    
