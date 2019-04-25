from flask import Blueprint, render_template, request, session, redirect, url_for, flash
import bcrypt

from cs2go.students.forms import StudentForm, EditForm, StudentPersonalQs, StudentCSQs
from cs2go.models import User, School, Module1, Module2, Module3, Assignment, PersonalQuestions, CSQs, BebrasQuiz1, BebrasQuiz2
from bson import ObjectId
import datetime

students_blueprint = Blueprint('students',
                               __name__,
                               template_folder='templates/students')


@students_blueprint.route('/create', methods=['GET', 'POST'])
def create():
    form = StudentForm(request.form)
    # get all the schools from the schools table
    school_list = [(str(row.id), row.name) for row in School.objects()]
    form.school.choices = school_list

    if request.method == 'POST' and form.validate():
        # check if a user exist with the given email or not
        existing_user = User.objects().filter(email=form.email.data).first()
        if existing_user is None:
            # have to hash password
            #get the school id here.
            hash_password = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt())
            # check if the school is listed or not
            school_id = form.school.data
            user = User()
            # create instance of User model and assign form data to it 
            user.user_type = 'student'
            user.name = form.name.data
            user.surname = form.surname.data
            user.email = form.email.data
            user.password = hash_password
            user.approved = False
            user.login_counter = 1
            user.login_array = [datetime.datetime.now()]
            user.school = ObjectId(school_id)
            user.save()
            session['email'] = user.email
            return redirect(url_for('students.PersonalQuestion'))
        else:
            flash('User with this email already exist')
            return redirect(url_for('students.create'))

    return render_template('student-create.html', form=form)


# route to get the form information from the personal quiz
@students_blueprint.route('/PersonalQs', methods=['GET', 'POST'])
def PersonalQuestion():
    form = StudentPersonalQs(request.form)
    if request.method == 'POST' and form.validate():
        personalqs = PersonalQuestions()
        personalqs.userid = session['email']
        personalqs.gender = form.Gender.data
        personalqs.age = form.Age.data
        personalqs.year = form.Year.data
        personalqs.englishspeaker = form.NativeEnglishSpeaker.data
        personalqs.mornornight = form.MorningOrNight.data
        personalqs.personalsmartphone = form.OwnSmartPhone.data
        personalqs.phoneaccess = form.HaveSphoneAccess.data
        personalqs.phonehours = form.PhoneHours.data
        personalqs.phoneactivity = form.PhoneActivity.data
        personalqs.personalcomputer = form.OwnPersonalComputer.data
        personalqs.nocomputer = form.HaveComputerAccess.data
        personalqs.computerhours = form.ComputerHours.data
        personalqs.computeractivity = form.ComputerActivity.data
        personalqs.personaltablet = form.OwnTablet.data
        personalqs.tablethours = form.TabletHours.data
        personalqs.tabletactivity = form.TabletActivity.data
        personalqs.programmingexperience = form.ProgrammingExperience.data
        personalqs.programmingexperiencetime = form.ProgrammingExperienceTime.data
        personalqs.programminglanguages = form.ProgrammingLanguages.data
        personalqs.programoften = form.ProgramOften.data
        personalqs.programminglevel = form.PersonalProgrammingProficiency.data
        personalqs.weborappdev = form.DoneWebOrAppDev.data
        personalqs.technologies = form.KnownTechnologies.data
        personalqs.programmingsite = form.ProgrammingSites.data
        personalqs.jclevel = form.JuniorCertLevel.data
        personalqs.parentoccupation = form.ITParentOccupation.data
        personalqs.save()
        return redirect(url_for('students.CSQuestion'))

    elif request.method == 'POST' and form.validate() == False:
        if form.errors:
            errors = form.errors
            for i in errors:
                flash(i)
         
    return render_template('student-PersonalQs.html', form=form)

# route to get the form data from the cs quiz
@students_blueprint.route('/CSQs', methods = ['GET', 'POST'])
def CSQuestion():
    form = StudentCSQs(request.form)
    if request.method == 'POST' and form.validate():
        studentcsqs = CSQs()
        studentcsqs.userid = session['email']
        studentcsqs.studycs = form.StudyCSUni.data
        studentcsqs.thinkcs = form.ThinkOfCS.data
        studentcsqs.csinteresting = form.CSInteresting.data
        studentcsqs.csinterestingwhy = form.CSInterestingWhy.data
        studentcsqs.cschallenging = form.CSChallenging.data
        studentcsqs.cschallengingwhy = form.CSChallengingWhy.data
        studentcsqs.internetcentral = form.InternetCentral.data
        studentcsqs.wordexcelcentral = form.WordExcelCentral.data
        studentcsqs.installingcentral = form.InstallingCentral.data
        studentcsqs.programmingcentral = form.ProgrammingCentral.data
        studentcsqs.solvingproblemscentral = form.SolvingProblemsCentral.data
        studentcsqs.relatedtomaths = form.RelatedToMaths.data
        studentcsqs.workwithothers = form.WorkWithOthers.data
        studentcsqs.menmorelikely = form.MenMoreLikely.data
        studentcsqs.donenocomputer = form.DoneNoComputer.data
        studentcsqs.heardcompthinking = form.HeardOfCompThinking.data
        studentcsqs.compthinkingmeaning = form.CompThinkingMeaning.data
        studentcsqs.save()

        return redirect(url_for('bebras.bebrasquiz1'))

    elif request.method == 'POST' and form.validate() == False:
        if form.errors:
            errors = form.errors
            for i in errors:
                flash(i)

    return render_template('student-csqs.html', form=form)



@students_blueprint.route('/profile', methods=['GET', 'POST'])
def profile():
    if session.get('email'):
        user = User.objects().filter(email=session.get('email')).first()
        # find assignments
        # need to find the assignment which is open as well as same as the same school
        assignments = Assignment.objects(school=user.school.id)
        return render_template('student-profile.html', user=user, assignments=assignments)
    else:
        return redirect(url_for('login'))


# This method can only be accessed by a teacher
# this route is for loading the list of students for teacher to approve/disapprove
@students_blueprint.route('/', methods=['GET', 'POST'])
def student_list():
    if session.get('email'):
        user = User.objects().filter(email=session.get('email')).first()
        if user.user_type == 'instructor' or user.user_type == 'admin':
            students = User.objects().filter(user_type='student')
            return render_template('students.html', students=students, user=user)
        else:
            return redirect(url_for('students.profile'))
    else:
        return redirect(url_for('login'))


# This method can only be accessed by a teacher
# Approve a new student
# when teacher clicks on green arrow to approve student this route is executed
@students_blueprint.route('/approve/<student_id>', methods=['GET', 'POST'])
def approve(student_id):
    if session.get('email'):
        user = User.objects().filter(email=session.get('email')).first()
        if user.user_type == 'instructor' or user.user_type == 'admin':
            # get the student by student_id
            # update the approve value to true
            User.objects(id=student_id).update_one(approved=True)
            # Redirect to student list page
            return redirect(url_for('students.student_list'))
        else:
            return redirect(url_for('students.profile'))
    else:
        return redirect(url_for('login'))


# This method can only be accessed by a teacher
# Approve a new student
# when teacher clicks on red x to remove student this route is executed
@students_blueprint.route('/remove/<student_id>', methods=['GET', 'POST'])
def remove(student_id):
    if session.get('email'):
        user = User.objects().filter(email=session.get('email')).first()
        if user.user_type == 'instructor' or user.user_type == 'admin':
            # get the student by student_id
            User.objects(id=student_id).delete()
            return redirect(url_for('students.student_list'))
        else:
            return redirect(url_for('students.profile'))
    else:
        return redirect(url_for('login'))

# this route is for the student progress page, when you click on a students name from the students list
@students_blueprint.route('/progress/<student_id>', methods=['GET', 'POST'])
def progress(student_id):
    if session.get('email'):
        # check if user is logged in
        teacher = User.objects().filter(email=session.get('email')).first()
        if teacher.user_type == 'instructor' or teacher.user_type == 'admin':
            student = User.objects(id=student_id).first()
            # get the students data
            teacher = User.objects().filter(email=session['email']).first()
            bebras1 = BebrasQuiz1.objects().filter(email=student.email).first() 
            # get bebras 1 quiz results 
            bebras2 = BebrasQuiz2.objects().filter(email=student.email).first()
            # get bebras 2 quiz results
            return render_template('student-progress.html', user=teacher, student=student, bebras1 = bebras1, bebras2 = bebras2)
        else:
            return redirect(url_for('students.profile'))
    else:
        return redirect(url_for('login'))

# this route for the edit profile page for students
@students_blueprint.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    if session.get('email'):
        form = EditForm()
        user = User.objects().filter(email=session.get('email')).first()
        if request.method == 'POST' and form.validate():
            user.name = form.name.data
            user.surname = form.surname.data
            user.save()
            flash('Profile successfully updated !')
        return render_template('student-edit-profile.html', user=user, form=form )
    else:
        return redirect(url_for('login'))
