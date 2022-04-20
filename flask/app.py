from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
@app.route('/main', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        form_data = request.form['your_number']
        return redirect(f'/square/{form_data}')
    return render_template("index.html")


@app.route('/square/<data>')
def answer(data):
    result = int(data)*int(data)
    return render_template("square.html", data=result)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
