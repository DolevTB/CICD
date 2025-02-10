from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    image_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZ2dM9XlW5hTI88i3JlD1YgIrAnDQ8GzJR49zDtplbNrYUpne9'
    return render_template('index.html', image_url=image_url)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
