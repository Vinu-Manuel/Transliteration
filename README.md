# Transliteration

The Transliteration program takes the input from the users, determine whether the input is in Hindi, Malayalam or Telugu and transliterates the input to its respective Roman characters

To use the program, follow the step-by-step guide given below:

1. Installing Flask: The program uses Flask and requires Flask to be installed in the system.
   Flash can be installed by:
        pip install Flask
        
2. Running file: After installing Flask, the folder ‘Transliteration’ can be accessed. In the folder, there are subfolders such as ‘static’ and ‘templates’. The folders are mandatory for the working of the program and hence, it is crucial that no file must be misplaced.
    
    The folder should contain the following hierarchy of the files and folders:
    <pre>
    Transliteration
      - hin_to_eng.py
      - hin_translit.py
      - main.py
      - mal_to_eng.py
      - mal_translit.py
      - tet_to_eng.py
      - tel_translit.py
      static
         - css.css
         images
            - by.jpg
            - hdr.jpg
      templates
         - index.html
</pre>
       
In the folder ‘Transliteration’, main.py is the program executing file. Run the file within the folder (Do not misplace/ extract the file alone) to use the program.

3. Running the URL: After running the main.py, the following message will be displayed.
<pre>
 * Serving Flask app "main" (lazy loading)
 * Environment: production
[31m   WARNING: This is a development server. Do not use it in a production deployment.[0m
[2m   Use a production WSGI server instead.[0m
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
</pre>
The URL address http://127.0.0.1:5000/ may differ depending on the port that python uses.
  
Copy, paste and run the URL in a browser (Chrome, Microsoft edge, etc.,). The result should display a webpage with the title "Transliteration".

4. Transliterating: To transliterate any text, input the text in the text-area provided in the webpage. Click the ‘TRANSLITERATE’ button to receive the transliterated output.

5. Exiting the program: To exit the program, close the browser. As the program is not published, manual exit of the running program is also required. For that press CTRL+C in the python console.
