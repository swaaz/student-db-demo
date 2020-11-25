import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def render_index():
    return render_template("index.html")


@app.route('/add_student')
def render_add_student_page():
    return render_template("add_student.html")


@app.route('/add_student_button', methods=['POST'])
def add_student_record():
    with sqlite3.connect("student.db") as conn:
        c = conn.cursor()

        name = request.form.get("name")
        usn = request.form.get("usn")
        sem = request.form.get("sem")

        c.execute("""
                    INSERT INTO Students(name, usn, sem) VALUES(?,?,?)
                    """, (name, usn, sem))

        return "successfully added new student"

@app.route('/add_teacher')
def render_add_teacher_page():
    return render_template("add_teacher.html")


@app.route('/add_teacher_button', methods=['POST'])
def add_teacher_record():
    with sqlite3.connect("student.db") as conn:
        c = conn.cursor()

        name = request.form.get("name")
        eno = request.form.get("eno")
        subject = request.form.get("subject")

        c.execute("""
                    INSERT INTO Teachers(name, eno, subject) VALUES(?,?,?)
                    """, (name, eno, subject))

        return "successfully added new teacher"


@app.route('/view_students')
def render_all_students():
    with sqlite3.connect('student.db')