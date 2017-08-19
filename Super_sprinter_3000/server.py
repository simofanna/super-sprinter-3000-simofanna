from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)


@app.route('/')
def route_form():
    return render_template('form.html')


@app.route('/edit-note')
def route_form_edit():
    return render_template('list.html')


@app.route('/save-note', methods=['POST'])
def route_save():
    print('POST request received!')
    session['note'] = request.form['note']
    return redirect('/')


if __name__ == "__main__":
    app.secret_key = 'magic'  
    app.run(
        debug=True,  
        port=5000  
    )
