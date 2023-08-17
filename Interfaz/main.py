from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('pages/home.html')

@app.route("/footer")
def footer():
	return render_template('components/footer.html')

if __name__ == '__main__':
	app.run(debug=True, port=6000)