from flask import Blueprint, render_template, request, session, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from cs2go.models import User, File, School, Module1, Module2, Module3
from cs2go import app
import sys

from cs2go.files.forms import UploadForm, TagForm
import os

files_blueprint = Blueprint('files',
                            __name__,
                            template_folder='templates/files')

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'pptx', 'docx', 'mp4'}


@files_blueprint.route('/upload', methods=['GET', 'POST'])
def upload():
    #check if the user is logged in by checking session.email
    if session.get('email'):
        form = UploadForm()
        #create instacnce of UploadForm
        user = User.objects().filter(email=session.get('email')).first()
        #get the user document from database based on the email of the logged in user
        if request.method == 'POST':
            file = form.file.data
            if file and allowed_file(file.filename):
                #check if file has been selected for upload and check if it is the allowed type
                filename = secure_filename(file.filename)
                #convert the file name into a 'secure version' so it can be stored in database
                #https://werkzeug.palletsprojects.com/en/0.15.x/utils/
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                print('Hello world!', file=sys.stderr)
                # save the file name in the database
                new_file = File()
                #declare instance of File model and assign data
                new_file.filename = filename
                new_file.user = user.id
                new_file.save()
                #save the uploaded fle to database and store it in the uploads folder
                return redirect(url_for('files.file_list'))
        return render_template('upload-file.html', form=form, user=user)
    else:
        return redirect(url_for('login'))

#route for downloading file
@files_blueprint.route('/download/<file_id>', methods=['GET', 'POST'])
def download(file_id):
    if session.get('email'):
        file = File.objects(id=file_id).first()
        # get file details from File collection
        if file:
            # if the file exists 
            uploads = app.config['UPLOAD_FOLDER']
            # set uploads to the directory of the uploads folder
            return send_from_directory(directory=uploads, filename=file.filename)
            #download the file
    else:
        return redirect(url_for('login'))


@files_blueprint.route('/', methods=['GET', 'POST'])
def file_list():
    # get the logged in user by session.get('email')
    if session.get('email'):
        user = User.objects().filter(email=session.get('email')).first()
        #get the user document from database based on the email of the logged in user
        files = File.objects()
        return render_template('files.html', files=files, user=user)
    else:
        return redirect(url_for('login'))


@files_blueprint.route('/add_to_module1/<file_id>', methods=['GET', 'POST'])
def add_to_module1(file_id):
    # Check if the user is logged in or not. if not logged in then redirect to login
    if session.get('email'):
        file = File.objects(id=file_id).first()
        # get the logged in user school
        # add the file to the module1 array
        user = User.objects().filter(email=session.get('email')).first()
        if user.user_type == 'instructor' or user.user_type == 'admin':
            user_school = School.objects(id=user.school.id).first()
            #get the school document from School collection that the student is enrolled
            user_school_module1 = Module1.objects(id=user_school.module1.id).first()
            user_school_module1.files.append(file.id)
            user_school_module1.save()
            return redirect(url_for('files.file_list'))
    else:
        return redirect(url_for('login'))


@files_blueprint.route('/add_to_module2/<file_id>', methods=['GET', 'POST'])
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


@files_blueprint.route('/add_to_module3/<file_id>', methods=['GET', 'POST'])
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


# Checking if the file uploaded is in the allowed extension variable
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@files_blueprint.route('/search', methods=['GET', 'POST'])
def search():
    if session.get('email'):
        search_tag = request.form.get('search')
        user = User.objects().filter(email=session.get('email')).first()
        # check if the user is teacher or if student then also check if the student is approved or not
        if (user.user_type == 'instructor' or user.approved) or user.user_type == 'admin':
            files = File.objects()
            # Now check for each files in which file this tag exists
            tagged_files = list()
            for file in files:
                # Loop through the tag and match the file tag with the search tag
                for file_tag in file.tags:
                    if file_tag.upper() == search_tag.upper():
                        tagged_files.append(file)
                        break
            #Also loop through all the names of the files to see if the search matches
            for file in files:
                if search_tag.upper() in file.filename.upper():
                    tagged_files.append(file)
                    

            return render_template('search-module.html', files=tagged_files, user=user)
    else:
        return redirect(url_for('login'))

# route for file details
@files_blueprint.route('/details/<file_id>', methods=['GET', 'POST'])
def details(file_id):
    if session.get('email'):
        form = TagForm()
        user = User.objects().filter(email=session.get('email')).first()
        if user.user_type == 'instructor' or user.approved or user.user_type == 'admin':
            file = File.objects(id=file_id).first()
            return render_template('file-details.html', file=file, user=user, form=form)
    else:
        return redirect(url_for('login'))

# route for adding tags to a file
@files_blueprint.route('/add_tag/<file_id>', methods=['GET', 'POST'])
def add_tag(file_id):
    if session.get('email'):
        # check if the user is logged in
        new_tags = request.form.get('tags').split(',')
        # get the tags from the form data and split up accordingly
        user = User.objects().filter(email=session.get('email')).first()
        # get user data for logged in user
        if user.user_type == 'instructor' or user.approved or user.user_type == 'admin':
            file = File.objects(id=file_id).first()
            # get file data by file id
            tag_list = list()
            for tag in file.tags:
                tag_list.append(tag.upper())
            for tag in new_tags:
                if tag.strip().upper() not in tag_list:
                    # trim the tag. so that no empty space before the tag and also after the tag
                    tag_list.append(tag.strip().upper())
            file.tags = tag_list
            file.save()
            # save the file with its new tags
        return redirect(url_for('files.file_list'))
    else:
        return redirect(url_for('login'))
