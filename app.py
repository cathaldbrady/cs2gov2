from cs2go import app
from flask import render_template, request, session, redirect, url_for, flash
from cs2go.forms import LoginForm
from cs2go.models import User
import bcrypt


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # first check if the request is get or post
    if request.method == 'POST':
        if form.validate():
            # if request is post then grab the data from the request
            email = form.email.data
            password = form.password.data.encode('utf-8')
            # check if the user exists in the database using the given credentials
            user = User.objects().filter(email=email).first()
            # if user exists then check the password
            if user:
                if bcrypt.checkpw(password, user.password):
                    session['email'] = form.email.data
                    # Check the type of the user.
                    # If user is a student then redirect that user to the student profile
                    # If user is a instructor then redirect that user to the teacher profile
                    if user.user_type == 'instructor' or user.user_type == 'admin':
                        return redirect(url_for('teachers.profile'))
                    return redirect(url_for('students.profile'))
                else:
                    # if password is incorrect than show the below message and redirect
                    flash('Email or password is incorrect')
                    return render_template('login.html', form=form)
            else:
                # if user not found then flash the below message and redirect
                flash('No user found. please sign up')
                return render_template('login.html', form=form)

    # if everything is okay then delete the password from the user object
    # set the user into the session
    # redirect the user in profile page
    return render_template('home.html', form=form)


@app.route('/edit_profile', methods=['GET', 'POST'])
def profile_edit():
    if session.get('email'):
        user = User.objects().filter(email=session.get('email')).first()
        if user.user_type == 'instructor' or user.user_type == 'admin':
            return redirect(url_for('teachers.edit_profile'))
        else:
            return redirect(url_for('students.edit_profile'))
    else:
        return redirect(url_for('login'))

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if session.get('email'):
        session.clear()
    return redirect(url_for('login'))


################################################################

# Error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, port=8080)

#https://cs2gomu.herokuapp.com/
#http://localhost:8080/teachers/create_admin
#some_super_secret_text_here
