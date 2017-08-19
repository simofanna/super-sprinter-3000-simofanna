from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def route_form():
    return render_template('form.html')


@app.route('/edit-note')
def route_form_edit():
    return render_template('story_id.html')

if __name__ == "__main__":
    app.run(
        debug=True, # Allow verbose error reports
        port=5000 # Set custom port
    )
