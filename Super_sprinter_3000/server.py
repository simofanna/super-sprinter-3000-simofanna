from flask import Flask, render_template, redirect, request, session
import csv
import random
import string


app = Flask(__name__)


def id_generator(chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for _ in range(6))


def stories_reader():
    lst = []
    with open("stories.csv", "r", newline='') as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            lst.append(row)
    return lst


def get_data():
    story_title = request.args.get('title')
    user_story = request.args.get('story')
    acc_criteria = request.args.get('criteria')
    business_value = request.args.get('value')
    estimation = request.args.get('estim')
    status = request.args.get('status')
    user_id = id_generator()
    actual_list = [user_id, story_title, user_story, acc_criteria, business_value, estimation, status]
    session['user_id'] = user_id
    return actual_list
    


def write_rows(filename):
    with open('stories.csv', 'w') as file:
        datawriter = csv.writer(file)
        datawriter.writerows(filename)


@app.route('/')
def story():
    stories_list = stories_reader()
    length_of_csv = len(stories_list)
    return render_template('list.html', stories_list=stories_list, long=length_of_csv)


@app.route('/new_story')
def route_list():
    return render_template('form.html')


@app.route('/update/<int:id_pos>')
def update_story(id_pos):
    stories_list = stories_reader()
    actual_data = get_data()
    for i in range(len(stories_list)):
        if id_pos-1 == i:
            stories_list[i] = actual_data
    write_rows(stories_list)
    return redirect("/")


@app.route('/delete/<int:id_pos>')
def delete_story(id_pos):
    stories_list = stories_reader()
    actual_data = []
    for i in range(len(stories_list)):
        if id_pos == i+1:
            continue
        else:
            actual_data.append(stories_list[i])
    write_rows(actual_data)
    return redirect('/')


@app.route('/save', methods=['GET'])
def save_story():
    new_data = get_data()
    with open('stories.csv', 'a') as file:
        datawriter = csv.writer(file)
        datawriter.writerow(new_data)
    return redirect('/')


@app.route('/story/<int:id_pos>')
def story_id(id_pos):
    stories_list = stories_reader()
    return render_template('form.html', id_pos=id_pos, stories_list=stories_list[id_pos-1])


if __name__ == "__main__":
    app.secret_key = 'magic'  
    app.run(
        debug=True,  
        port=5000  
    )
