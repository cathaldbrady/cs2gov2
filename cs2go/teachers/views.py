from flask import Blueprint, render_template, request, flash, redirect, url_for, session
import bcrypt
from bson import ObjectId

from cs2go.teachers.forms import TeacherForm, EditForm, AdminForm
from cs2go.models import User, School, Module1, Module2, Module3, Assignment

teachers_blueprint = Blueprint('teachers',
                               __name__,
                               template_folder='templates/teachers')


@teachers_blueprint.route('/create', methods=['GET', 'POST'])
def create():
    form = TeacherForm(request.form)
    # get all the schools from the schools table
    school_list = [(str(row.id), row.name) for row in School.objects()]
    school_list.append(("not-listed", "My school is not listed"))
    form.school.choices = school_list
    if request.method == 'POST' and form.validate():
        # check if a user exist with the given email or not
        existing_user = User.objects().filter(email=form.email.data).first()
        if existing_user is None:
            # before inserting the document into database we have to hash password
            hash_password = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt())
            # check if the school is listed or not
            school_id = form.school.data
            if form.school.data == 'not-listed':
                # if the school name isn't listed when signing up:
                # get the name of the school
                school_name = request.form.get('school_name')
                # insert the school into the database
                school = School()
                school.name = school_name
                # need to create document in Module1, Module2, Module3 collections for this school
                module1 = Module1()
                module1.save()
                # blank module1 document is saved to the database
                school.module1 = module1.id
                # saving the id for the module1 document created for this school.
                # school.module1 is of type ReferenceField meaning that this will be a reference to the document in the Module1 collection for this school.
                module2 = Module2()
                module2.save()
                school.module2 = module2.id
                # same idea again, collection Module2 contains all information about all Module2s for every school
                # school.module1 is of type ReferenceField meaning that this will be a reference to the document in the Module1 collection for this school.
                module3 = Module3()
                module3.save()
                school.module3 = module3.id

                school.save()
                school_id = school.id
            user = User()
            # finally create document in User collection containing information about the registering user
            user.title = form.title.data
            user.user_type = 'instructor'
            user.name = form.name.data
            user.surname = form.surname.data
            user.email = form.email.data
            user.password = hash_password
            user.school = ObjectId(school_id)
            # save the user
            user.save()
            session['email'] = user.email
            return redirect(url_for('teachers.profile'))
        else:
            flash('User with this email already exist')
            return redirect(url_for('teachers.create'))
    return render_template('teacher-create.html', form=form)


@teachers_blueprint.route('/create_admin', methods=['GET', 'POST'])
def create_admin():
    form = AdminForm(request.form)
    # get all the schools from the schools table
    school_list = [(str(row.id), row.name) for row in School.objects()]
    school_list.append(("not-listed", "My school is not listed"))
    form.school.choices = school_list
    if request.method == 'POST' and form.validate():
        # check if a user exist with the given email or not
        existing_user = User.objects().filter(email=form.email.data).first()
        # Here check the SECRET KEY
        if existing_user is None and form.secret.data == 'some_super_secret_text_here':
            # before inserting the document into database we have to hash password
            hash_password = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt())
            # check if the school is listed or not
            school_id = form.school.data
            if form.school.data == 'not-listed':
                # get the name of the school
                school_name = request.form.get('school_name')
                # insert the school into the database
                school = School()
                school.name = school_name
                # here create the module1, module2, module3
                module1 = Module1()
                module1.save()
                school.module1 = module1.id

                module2 = Module2()
                module2.save()
                school.module2 = module2.id

                module3 = Module3()
                module3.save()
                school.module3 = module3.id

                school.save()
                school_id = school.id
            user = User()
            # create document in User collection to contain information about registering user
            user.title = form.title.data
            user.user_type = 'admin'
            user.name = form.name.data
            user.surname = form.surname.data
            user.email = form.email.data
            user.password = hash_password
            user.school = ObjectId(school_id)
            user.save()
            session['email'] = user.email
            return redirect(url_for('teachers.profile'))
        else:
            if form.secret.data != 'some_super_secret_text_here':
                flash('Wrong secret key !')
            else:
                flash('User with this email already exist')
            return redirect(url_for('teachers.create_admin'))
    return render_template('admin-create.html', form=form)


@teachers_blueprint.route('/profile', methods=['GET', 'POST'])
def profile():
    if session.get('email'):
        user = User.objects().filter(email=session.get('email')).first()
        # find the assignments
        # need to find the assignment which is open as well as same the same school
        assignments = Assignment.objects(school=user.school.id)
        return render_template('teacher-profile.html', user=user, assignments=assignments)
    else:
        return redirect(url_for('login'))


@teachers_blueprint.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    if session.get('email'):
        form = EditForm()
        school_list = [(str(row.id), row.name) for row in School.objects()]
        form.school.choices = school_list
        user = User.objects().filter(email=session.get('email')).first()
        form.name.data = user.name
        form.surname.data = user.surname
        if request.method == 'POST' and form.validate():
            user.name = form.name.data
            user.surname = form.surname.data
            if user.user_type == 'admin' and form.school.data is not None:
                user.school = ObjectId(form.school.data)
            user.save()
            flash('Profile successfully updated !')
        return render_template('teacher-edit-profile.html', user=user, form=form)
    else:
        return redirect(url_for('login'))
