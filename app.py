# app.py
from flask import Flask, render_template, request

# Create an instance of the Flask web application
app = Flask(__name__)

# Define a route for the home page ('/')
@app.route('/', methods=['GET', 'POST'])
def index():
    user_name = "Guest" # Default name
    if request.method == 'POST':
        # Get the 'user_name' from the form data
        submitted_name = request.form.get('user_name')
        if submitted_name:
            user_name = submitted_name
    # Render the 'index.html' template, passing the 'user_name' variable
    return render_template('index.html', name=user_name)

# This block is for local development only. Azure App Service will use a WSGI server (like Gunicorn)
# to run your app in production.
if __name__ == '__main__':
    app.run(debug=True)
