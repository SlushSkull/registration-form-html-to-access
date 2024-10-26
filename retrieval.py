from flask import Flask, request, render_template_string, render_template
import pyodbc

app = Flask(__name__)

# Database connection settings
DATABASE_PATH = ".\\UserLogins.accdb"  # Replace with your actual file path
def get_db_connection():
    # Connect to the Access database
    conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                f'DBQ={DATABASE_PATH};')
    
    try:
        conn = pyodbc.connect(conn_str)
        print("Connection successful!")
        return conn  # Return the connection object
    except Exception as e:
        print("Error:", e)
        return None  # Return None if connection fails

# Route to display the form
@app.route("/")
def index():
    # Use either of these methods
    # return render_template_string(html_template) # Assign html_template with html code as string for it to work
    return render_template("retrieve.html") # Looks into the templates folder to see the html file, and renders that

# Route to retrieve and display all users
@app.route("/users")
def show_users():
    conn = get_db_connection()
    if conn is None:
        return "<h1>Database connection failed!</h1>"

    cursor = conn.cursor()
    try:
        # Fetch all rows from Users table
        cursor.execute("SELECT * FROM Users")
        users = cursor.fetchall()  # Fetch all rows
        # print(users[0])

        ThisString = ""
        for x in range(len(users)):
            FormattedString = str(users[x])
            FormattedString = FormattedString[1 : len(FormattedString) - 1]
            # print(FormattedString)
            ThisString = ThisString + FormattedString + "<br>"
            

    except Exception as e:
        return f"<h1>Error while retrieving data: {e}</h1>"
    finally:
        cursor.close()
        conn.close()

    ReturnStr = (
        "<style>body { background-color: #0d0f12; } h1, h2 { color: #e3e6e8; } "
        "a { background-color: #0d0f12; border-radius: 12px; color: white; "
        "padding: 6px 10px; border: 2px solid white; text-decoration: none; } .align { display: flex; justify-content: center; align-items: center; }</style>"
        "<h1>Retrieved Items are:<h1>"
        "<h1 class=\"align\">UserID, Name, Email, Password<h1>"
        f"<h1 class=\"align\">{ThisString}</h1>"
        "<br><h2>Click <a href=\"http://127.0.0.1:5001\">here</a> to go back to the Button retrieval page.</h2>"
    )

    # Pass users to the template for rendering
    return ReturnStr


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
