import os
from flask import Flask, redirect, url_for, render_template, request, flash
from forms import UserForm
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

@app.route('/',methods=['GET','POST'])
def home():
    form = UserForm(request.form)    
    if request.method=='POST' and form.validate():
        user = User(form.f_name.data, form.l_name.data, form.email.data, form.feedback.data)
        db.session.add(user)
        db.session.commit()
        flash('Thank you for your feedback.','success')
        # Handle POST Request here
        return redirect(url_for('index'))
    return render_template('index.html', form=form)


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)