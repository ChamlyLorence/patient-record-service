from app import create_app, db


app = create_app()

@app.before_first_request
def setup_database():
    db.create_all()

if __name__ == '__main__':
    print("MediTrack - Patient Service")
    app.run(host='0.0.0.0', port=5000)
    #commnet 4
