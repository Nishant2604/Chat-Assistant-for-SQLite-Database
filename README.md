Chatbot SQL Assistant
This is a Flask-based chatbot that translates natural language queries into SQL queries and retrieves relevant data from a SQLite database. Initially, the assistant worked via API endpoints using Postman, but a Simple UI Interface was added to enhance user interaction instead of using Postman.

Features
1)Converts user input into SQL queries.

2)Extracts key entities such as department names and dates.

3)Executes SQL queries on a SQLite database and returns results.

4)Interactive Web UI for user-friendly query submission.

Stages of Development and Respective Files
A) Database setup

setup_db.ipynb : Establishes connection with the SQLite database, creates the employees and departments tables, inserts sample records into them.

company.db: SQLite database used for storing employee data.

B) API-Based Query Handling

app.py: Main Flask application handling API requests.

query_handler.py and chatbot.ipynb: Contains logic to convert natural language into SQL queries.

C) requirements.txt: Lists dependencies, including spaCy and Flask.

D) Simple UI Integration

templates/index.html: Frontend for user interaction.

app.py: Updated to serve the UI and handle form submissions.

How It Works
The user enters a query in natural language (e.g., "What is the total salary expense of the Sales and HR departments?").

The assistant processes the query and extracts key entities (departments, date, etc.).

It constructs an appropriate SQL query based on predefined rules.

The query is executed against the SQLite database.

The result is displayed on the UI.

Steps to Run the Project Locally
Clone the Repository
git clone cd chatbot-sql-assistant

Create a Virtual Environment
python -m venv venv source venv/bin/activate # On macOS/Linux venv\Scripts\activate # On Windows

Install Dependencies
pip install -r requirements.txt python -m spacy download en_core_web_sm # Required for NLP processing

Run the Application through the command prompt using
python app.py

The chatbot will be accessible at http://127.0.0.1:5000.

Using the Simple UI Interface
Open your browser and navigate to http://127.0.0.1:5000

Enter a query in the text box.

Click Submit to receive a response from the chatbot.

Deployment on Render
This project is deployed on Render. https://chatbot-qycg.onrender.com

To deploy your own version:

Push the latest changes to a GitHub repository.

Create a new Web Service on Render.

Set the Start Command to:

gunicorn app:app

Add environment variables if needed (e.g., database credentials).

Deploy and access the UI via the Render URL.

Known Limitations & Suggestions for Improvement
Limitations
Currently supports predefined query patterns.

Doesn't handle complex queries with multiple conditions well.

No authentication/authorization in place.

Improvements
Expand NLP processing for more flexible query understanding.

Integrate a chatbot frontend for a more interactive experience.

Support multiple databases beyond SQLite.

Implement user authentication for security.







