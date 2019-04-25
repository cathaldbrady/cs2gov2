import os
from flask import Blueprint, render_template, request, session, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from cs2go import app

from cs2go.assignments.forms import AssignmentForm, AssignmentDocumentForm
from cs2go.models import User, Assignment, School, Document

assignments_blueprint = Blueprint('assignments',
                                  __name__,
                                  template_folder='templates/assignments')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'pptx', 'docx', 'mp4'}


# Only instructor and admin can access this route
@assignments_blueprint.route('/', methods=['GET', 'POST'])
def assignment_list():
    if session.get('email'):
        # get the logged in user by session.get('email')
        user = User.objects().filter(email=session.get('email')).first()
        if user.user_type == 'instructor' or user.user_type == 'admin':
            assignments = Assignment.objects(school=user.school.id)
            # get all the assignments from the Assignments collection
        else:
            return redirect(url_for('students.profile'))
            #if logged in user is not either teacher or admin redirect to student homepage
        return render_template('assignments.html', assignments=assignments, user=user)
    else:
        return redirect(url_for('login'))


# Only instructor and admin can access this route
@assignments_blueprint.route('/details/<assignment_id>', methods=['GET', 'POST'])
def assignment_details(assignment_id):
    if session.get('email'):
        # get the logged in user by session.get('email')
        user = User.objects().filter(email=session.get('email')).first()
        if user.user_type == 'instructor' or user.user_type == 'admin':
            # get all the question from the Post table
            assignment = Assignment.objects(id=assignment_id).first()
        else:
            return redirect(url_for('students.profile'))
        return render_template('assignment-details.html', assignment=assignment, user=user)
    else:
        return redirect(url_for('login'))


# Only instructor and admin can access this route
@assignments_blueprint.route('/create', methods=['GET', 'POST'])
def create_assignment():
    # get the logged in user by session.get('email')
    if session.get('email'):
        # get instance of assignment form
        form = AssignmentForm(request.form)
        user = User.objects().filter(email=session.get('email')).first()
        # get the user document from database from logged in user
        if user.user_type == 'instructor' or user.user_type == 'admin':
            if request.method == 'POST' and form.validate():
                # check if the user type is teacher or admin and validate form for incoming POST request
                # First save the Question
                assignment = Assignment()
                # declare instance of assignment model for use and assign form data to it
                assignment.title = form.title.data
                assignment.description = form.description.data
                assignment.submission_date = form.submission_date.data
                assignment.created_by = user.id
                assignment.school = user.school.id
                assignment.save()
                # save the assignment to the database
                # get the user school
                user_school = School.objects(id=user.school.id).first()
                # get the school document from database based on the school id
                user_school.assignments.append(assignment.id)
                # add the assignment to the list of assignments for the school
                user_school.save()
                # redirect the user in the assignments list route
                return redirect(url_for('assignments.assignment_list'))
        else:
            return redirect(url_for('students.profile'))
        return render_template('assignment-create.html', form=form, user=user)
    else:
        return redirect(url_for('login'))


# only student can access this route
# for student uploading documents
@assignments_blueprint.route('/document/<assignment_id>', methods=['GET', 'POST'])
def upload_document(assignment_id):
    # get the logged in user by session.get('email')
    if session.get('email'):
        submitted = False
        assignment = Assignment.objects(id=assignment_id).first()
        # check if the user has already submitted the assignment or not
        form = AssignmentDocumentForm()
        # create instance of AssignmentDocumentForm
        user = User.objects().filter(email=session.get('email')).first()
        #get user document of logged in user by email of user in session
        previously_submitted_doc = Document.objects(assignment=assignment.id, submitted_by=user.id).first()
        #check if the user has already submitted a document for this assignment
        if previously_submitted_doc is not None:
            # if user has already submitted document for assignment
            submitted = True
            form.submit.label.text = 'Edit Upload'
        if request.method == 'POST' and form.validate():
            file = form.file.data
            if file and allowed_file(file.filename):
                # check if the file submitted in the POST request is of the allowed type, check by extension
                if not submitted:
                    filename = secure_filename(file.filename)
                    # get name of the file
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    # save the file name in the database
                    document = Document()
                    # declare instance of Document model and assign form data to it
                    document.filename = filename
                    document.assignment = assignment.id
                    document.submitted_by = user.id
                    document.save()
                    assignment.documents.append(document.id)
                    assignment.save()
                    # set a flash message that document successfully updated
                else:
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    previously_submitted_doc.filename = filename
                    previously_submitted_doc.save()
                    # set a flash message that document successfully updated
            # redirect the user in the questions routes
            return redirect(url_for('assignments.assignment_list'))
        return render_template('assignment-document.html', form=form, assignment=assignment, user=user,
                               submitted=submitted, document=previously_submitted_doc)
    else:
        return redirect(url_for('login'))


@assignments_blueprint.route('/close/<assignment_id>', methods=['GET', 'POST'])
def close_assignment(assignment_id):
    if session.get('email'):
        # get the logged in user by session.get('email')
        user = User.objects().filter(email=session.get('email')).first()
        if user.user_type == 'instructor' or user.user_type == 'admin':
            # check the user type
            assignment = Assignment.objects(id=assignment_id).first()
            # get document from assignment collection based on the id
            # make the assignment status false
            assignment.status = False
            assignment.save()
            # update the status of the assignment to false, meaning it is closed and no longer accepting submissions
        return redirect(url_for('assignments.assignment_details', assignment_id=assignment_id))

    else:
        return redirect(url_for('login'))


@assignments_blueprint.route('/open/<assignment_id>', methods=['GET', 'POST'])
def open_assignment(assignment_id):
    if session.get('email'):
        # get the logged in user by session.get('email')
        user = User.objects().filter(email=session.get('email')).first()
        if user.user_type == 'instructor' or user.user_type == 'admin':
            # get the document from assignment collection in database based on assignment id
            assignment = Assignment.objects(id=assignment_id).first()
            # make the assignment status True
            assignment.status = True
            assignment.save()
            # update the status to open, now accepting submissions again
        return redirect(url_for('assignments.assignment_details', assignment_id=assignment_id))
    else:
        return redirect(url_for('login'))


# Checking if the file uploaded is in the allowed extension 
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

#route for downloading assignments
@assignments_blueprint.route('/download/<file_name>', methods=['GET', 'POST'])
def download(file_name):
    uploads = app.config['UPLOAD_FOLDER']
    return send_from_directory(directory=uploads, filename=file_name)
