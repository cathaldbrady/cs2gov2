from flask import Blueprint, render_template, session, redirect, url_for, send_from_directory, request, flash
from cs2go.models import File, User, School, Chat, Module1, Module2, Module3
from cs2go.schools.forms import ChatForm
from cs2go import app

schools_blueprint = Blueprint('schools',
                              __name__,
                              template_folder='templates/schools')


# Module1
@schools_blueprint.route('/module1', methods=['GET', 'POST'])
def module1():
    # Check if the user is logged in or not. if not logged in then redirect to login
    if session.get('email'):
        user = User.objects().filter(email=session.get('email')).first()
        # check if the user is teacher or student then also check if the student is approved or not
        if (user.user_type == 'instructor' or user.approved) or user.user_type == 'admin':
            #get document 
            user_school = School.objects(id=user.school.id).first()
            files = user_school.module1.files
            # get the list of files that are in module1 for this school
            print(files)
            # Here Fetch All the user school chat, 
            chats = user_school.module1.chats
            chats.sort(key=lambda x: x['created_at'], reverse=True)
            # sort the order of the chat by created_at
            return render_template('module1.html', files=files, user=user, chats=chats)
    else:
        return redirect(url_for('login'))


# Module2
@schools_blueprint.route('/module2', methods=['GET', 'POST'])
def module2():
    # Check if the user is logged in or not. if not logged in then redirect to login
    if session.get('email'):
        user = User.objects().filter(email=session.get('email')).first()
        # check if the user is teacher or student then also check if the student is approved or not
        if (user.user_type == 'instructor' or user.approved) or user.user_type == 'admin':
            user_school = School.objects(id=user.school.id).first()
            files = user_school.module2.files
            # get the list of files that are in module1 for this school
            # Here Fetch All the user school chat
            chats = user_school.module2.chats
            chats.sort(key=lambda x: x['created_at'], reverse=True)
            # use lambda expression to reverse order of the post to module post board so newest ones are first 
            return render_template('module2.html', files=files, user=user, chats=chats)
    else:
        return redirect(url_for('login'))


# Module3
@schools_blueprint.route('/module3', methods=['GET', 'POST'])
def module3():
    # Check if the user logged in or not. if not logged in then redirect to login
    if session.get('email'):
        user = User.objects().filter(email=session.get('email')).first()
        # check if the user is teacher or student then also check if the student is approved or not
        if (user.user_type == 'instructor' or user.approved) or user.user_type == 'admin':
            user_school = School.objects(id=user.school.id).first()
            files = user_school.module3.files
            # Here Fetch All the user school chat
            chats = user_school.module3.chats
            chats.sort(key=lambda x: x['created_at'], reverse=True)
            # use lambda expression to reverse order of the post to module post board so newest ones are first 
            return render_template('module3.html', files=files, user=user, chats=chats)
    else:
        redirect(url_for('login'))


# Only Teachers have access to this route
#This route is to create a new post for the "Module Post Board", This used to be called "Module Chat",
#A chat refers to a post
@schools_blueprint.route('/chat_create/<module>', methods=['GET', 'POST'])
def chat_create(module):
    if session.get('email'):
        form = ChatForm(request.form)
        # get instance of ChatForm model
        user = User.objects().filter(email=session.get('email')).first()
        # get user data of logged in user
        if user.user_type == 'instructor' or user.user_type == 'admin':
            #check if teacher or admin
            if request.method == 'POST' and form.validate():
                #validate the form
                chat = Chat()
                # create instance of Chat model and assign form data
                chat.user = user.id
                chat.description = form.description.data
                chat.save()
                user_school = School.objects(id=user.school.id).first()
                if module == 'module1':
                    #variable module is taken as parameter to the function
                    flash('Chat Successfully Added to Module1 !')
                    user_school_module1 = Module1.objects(id=user_school.module1.id).first()
                    user_school_module1.chats.append(chat.id)
                    user_school_module1.save()
                elif module == 'module2':
                    flash('Chat Successfully Added to Module2 !')
                    user_school_module2 = Module2.objects(id=user_school.module2.id).first()
                    user_school_module2.chats.append(chat.id)
                    user_school_module2.save()
                elif module == 'module3':
                    flash('Chat Successfully Added to Module3 !')
                    user_school_module3 = Module3.objects(id=user_school.module3.id).first()
                    user_school_module3.chats.append(chat.id)
                    user_school_module3.save()
                user_school.save()
                if module == 'module1':
                    return redirect(url_for('schools.module1'))
                if module == "module2":
                    return redirect(url_for('schools.module2'))     
                if module == "module3":
                    return redirect(url_for('schools.module3'))
                # redirect the user to the chat-create
                # Flash Message that Chat Successfully Created
                
        else:
            return redirect(url_for('students.profile'))
        return render_template('chat-create.html', form=form, user=user, module=module)
    else:
        return redirect(url_for('login'))

# route to add files to module 1
@schools_blueprint.route('/add_to_module1/<file_id>', methods=['GET', 'POST'])
def add_to_module1(file_id):
    # Check if the user is logged in or not. if not logged in then redirect to login
    if session.get('email'):
        file = File.objects(id=file_id).first()
        # get the logged in user school
        # add the file to the module1 array
        user = User.objects().filter(email=session.get('email')).first()
        if user.user_type == 'instructor' or user.user_type == 'admin':
            user_school = School.objects(id=user.school.id).first()
            user_school_module1 = Module1.objects(id=user_school.module1.id).first()
            user_school_module1.files.append(file.id)
            user_school_module1.save()
            return redirect(url_for('files.file_list'))
    else:
        return redirect(url_for('login'))

# route to add files to module 2
@schools_blueprint.route('/add_to_module2/<file_id>', methods=['GET', 'POST'])
def add_to_module2(file_id):
    # Check if the user is logged in or not. if not logged in then redirect to login
    if session.get('email'):
        file = File.objects(id=file_id).first()
        # get the logged in user school
        # add the file to the module2 array
        user = User.objects().filter(email=session.get('email')).first()
        if user.user_type == 'instructor' or user.user_type == 'admin':
            user_school = School.objects(id=user.school.id).first()
            user_school_module2 = Module2.objects(id=user_school.module2.id).first()
            user_school_module2.files.append(file.id)
            user_school_module2.save()
            return redirect(url_for('files.file_list'))
    else:
        return redirect(url_for('login'))

# route to add files to module 3
@schools_blueprint.route('/add_to_module3/<file_id>', methods=['GET', 'POST'])
def add_to_module3(file_id):
    # Check if the user is logged in or not. if not logged in then redirect to login
    if session.get('email'):
        file = File.objects(id=file_id).first()
        # get the logged in user school
        # add the file to the module3 array
        user = User.objects().filter(email=session.get('email')).first()
        if user.user_type == 'instructor' or user.user_type == 'admin':
            user_school = School.objects(id=user.school.id).first()
            user_school_module3 = Module3.objects(id=user_school.module3.id).first()
            user_school_module3.files.append(file.id)
            user_school_module3.save()
            return redirect(url_for('files.file_list'))
    else:
        return redirect(url_for('login'))


@schools_blueprint.route('/download/<file_name>', methods=['GET', 'POST'])
def download(file_name):
    uploads = app.config['UPLOAD_FOLDER']
    return send_from_directory(directory=uploads, filename=file_name)
