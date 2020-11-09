import connexion

# Create the application instance
app = connexion.App(__name__, specification_dir='./')

@app.route('/')
def hello():
    return 'Hello World'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)