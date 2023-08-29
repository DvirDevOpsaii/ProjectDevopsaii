# app/routes.py
from flask import render_template, url_for, flash, redirect
from app import app, db
from app.models import Task
from app.forms import TaskForm
from datetime import datetime

@app.route('/')
def calendar():
    tasks = Task.query.all()
    return render_template('calendar.html', tasks=tasks)

@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(title=form.title.data, due_date=form.due_date.data)
        db.session.add(task)
        db.session.commit()
        flash('Task has been added!', 'success')
        return redirect(url_for('calendar'))
    return render_template('add_task.html', form=form)
