from flask import Flask, request, render_template_string, render_template
import pyodbc

app = Flask(__name__)

# Database connection settings
DATABASE_PATH = ".\\UserLogins.accdb"  # Replace with your actual file path. By default, keep the Access file next to this file


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
    return render_template("sign_up.html")  # Looks into the templates folder to see the html file, and renders that


# Route to handle form submission
@app.route("/submit", methods=["POST"])
def submit():
    # Retrieve form data
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    # Saving Data Into A Text File
    with open("login.txt", "a") as MyFile:
        MyFile.write(f"Name: {name}\nE-mail: {email}\nPassword: {password}\n\n")

    # Insert data into the database
    conn = get_db_connection()
    if conn is None:
        return "<h1>Database connection failed!</h1>"

    cursor = conn.cursor()

    try:
        # Insert query
        cursor.execute("INSERT INTO Users (UserName, Email, Password) VALUES (?, ?, ?)", (name, email, password))
        conn.commit()  # Commit the transaction
    except Exception as e:
        return f"<h1>Error while inserting into database: {e}</h1>"
    finally:
        cursor.close()
        conn.close()  # Close the database connection

    ReturnStr = (
        "<style>body { background-color: #0d0f12; } h1, h2 { color: #e3e6e8; } "
        "a { background-color: #0d0f12; border-radius: 12px; color: white; "
        "padding: 6px 10px; border: 2px solid white; text-decoration: none; }</style>"
        f"<h1>Thank you, {name}! You have successfully created an account with the email {email}.</h1>"
        "<br><h2>Click <a href=\"http://127.0.0.1:5000\">here</a> to go back to the User Sign up page.</h2>"
    )

    return ReturnStr


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
