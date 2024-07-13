from app import app

# For local system & cloud
if __name__ == "__main__":
    app.run(debug=True,threaded=False,port=8080)