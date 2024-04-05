import os
from taskmanager import app

if __name__ == "__main__":
    # Set environment variables
    os.environ['IP'] = '127.0.0.1'  # Replace with your desired IP address
    os.environ['PORT'] = '5500'      # Replace with your desired port number
    os.environ['DEBUG'] = 'True'     # Set to 'True' to enable debug mode, 'False' otherwise

    # Run the Flask application
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG") == 'True'
    )
