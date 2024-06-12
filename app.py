from flask import Flask, jsonify, render_template, request
from search import perform_search
from database import fetch_all_documents_from_database, get_document_file_url_from_database

# Fetch all documents from MongoDB
documents = fetch_all_documents_from_database()

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def homePage():
    return render_template('index.html')

@app.route('/perform_search', methods=['POST'])
def call_perform_search_function():
    # Get data from request body
    data = request.get_json()
    keyword = data.get('keyword')
    algorithm = data.get('algorithm')

    # Perform search using keyword and algorithm
    results = perform_search(keyword, algorithm, documents)

    # Return search results as JSON
    return jsonify(results)

@app.route('/document', methods=['POST'])
def get_document():
    # Get data from request body
    data = request.get_json()
    title = data.get('title')

    # Get document URL from database
    url = get_document_file_url_from_database(title)
    print(url)

    # Return document URL as JSON
    return jsonify({"url": url})

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=8000)
