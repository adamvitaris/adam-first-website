from flask import Flask, render_template, jsonify

app = Flask(__name__)

PLACES = [
  {
    'id': 1,
    'city':'Barcelona',
    'location':'Spain',
    'program':'City Tour'
  },
  {
    'id': 2,
    'city':'Crete',
    'location':'Greece',
    'program':'Swimming'
  },
   {
    'id': 3,
    'city':'Bohinj',
    'location':'Slovenia',
    'program':'Hiking'
  }
]

@app.route("/")
def hello_wordl():
  return render_template('home.html',
                        places=PLACES)

@app.route("/api/places")
def list_places():
  return jsonify(PLACES)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)