from flask import Flask, request
import pyodbc

app = Flask(__name__)

# Database connection configuration
DB_CONFIG = {
    'driver': 'ODBC Driver 17 for SQL Server',
    'server': 'your_server_name',
    'database': 'your_database_name',
    'username': 'your_username',
    'password': 'your_password'
}

def get_db_connection():
    connection_string = (
        f"DRIVER={{{DB_CONFIG['driver']}}};"
        f"SERVER={DB_CONFIG['server']};"
        f"DATABASE={DB_CONFIG['database']};"
        f"UID={DB_CONFIG['username']};"
        f"PWD={DB_CONFIG['password']}"
    )
    return pyodbc.connect(connection_string)

@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "SELECT TOP 10 * FROM your_table_name"  # Replace with your SQL query
        cursor.execute(query)
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        print(results)  # Print results to the terminal
    except Exception as e:
        print({'error': str(e)})  # Print error to the terminal
    finally:
        conn.close()
    return "Check the terminal for output."

@app.route('/api/insert', methods=['POST'])
def insert_data():
    try:
        data = request.json
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO your_table_name (column1, column2) VALUES (?, ?)"  # Adjust columns
        cursor.execute(query, (data['column1'], data['column2']))
        conn.commit()
        print({'message': 'Data inserted successfully'})  # Print success message to the terminal
    except Exception as e:
        print({'error': str(e)})  # Print error to the terminal
    finally:
        conn.close()
    return "Check the terminal for output."

if __name__ == '__main__':
    app.run(debug=True)