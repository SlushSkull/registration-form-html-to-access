# registration-form-html-to-access
Connects an HTML form to MS Access, and retrieves data from it.

It uses Flask to send form data from HTML form to python variables and uses ptodbc to send the python variable data to the MS Access Database and retrieving Access data and displaying it in a web page. 

## How to run this?
1. Clone or download zip file and extract it in a folder.
2. Install flask and pyodbc using `pip install flask` and `pip install pyodbc` in your terminal/cmd.
3. Open two instances of terminal/cmd and type `python app.py` in one of them and `python retrieval.py --app` in the other one. (Alternatively, use pycharm, it allows for both files to run at the same time.)
4. Two HTML files will open in your web browser. Fill out the form and click on the **Sign up** button.
5. If successful, a text file called `login.txt` will be created with the data from the fields entered in the web browser. The Access file `UserLogins.accdb` will also have the data in it.
6. For Database retrieval, click on the button which is in the center of the web page.

> [!IMPORTANT]
> The MS Access file needs to have the table with its attributes already been created, or else it will not work.
