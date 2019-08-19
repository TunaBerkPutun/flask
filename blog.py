from flask import Flask, request, render_template

app = Flask(__name__)


plaka = None
@app.route('/')
def harita():
	if plaka is None:
		return render_template('Geocode.html')
	else:
		return render_template('Geocode.html', data=plaka)

@app.route('/pythonveri', methods=['POST'])
def get_python_data():
	plaka = str(request.get_data())
	tip = str(type(plaka))
	if plaka == "asda":
		return "no"
	else:
		return tip


if __name__ == "__main__":
	app.run(debug=True)
