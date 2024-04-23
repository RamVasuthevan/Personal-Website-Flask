from flask import Flask, make_response, render_template

from chart_generator import generate_chart

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")


@app.route("/bitsbipsbricks/How-to-Chart/flask-chart.svg")
def chart_svg():
    chart_svg_data = generate_chart()

    response = make_response(chart_svg_data)
    response.content_type = "image/svg+xml"

    return response


if __name__ == "__main__":
    app.run(debug=True, port=5000)
