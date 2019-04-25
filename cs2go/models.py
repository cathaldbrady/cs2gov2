from cs2go import db
from datetime import datetime

class School(db.Document):
    # There is a school document created for each indivdual school, it holds information about the school
    # School name, assignments, and posts and files added to each module
    # The info related to what each module contains for each school is not actually held in school document but is held in collections Module1,Module2,Module3 and then referencing those here.
    name = db.StringField(required=True, max_length=100)
    module1 = db.ReferenceField('Module1')
    # In create() for teachers on line 39 school.module1 = module1.id 
    # ReferenceField allows us to reference to another document
    module2 = db.ReferenceField('Module2')
    module3 = db.ReferenceField('Module3')
    # A school will have a list of assignments
    assignments = db.ListField(db.ReferenceField('Assignment'))
    meta = {
        'collection': 'schools'
    }


class Assignment(db.Document):
    title = db.StringField(required=True, max_length=200)
    description = db.StringField()
    # Who created the assignment.
    created_by = db.ReferenceField('User')
    # What school.
    school = db.ReferenceField('School')
    # Submission date
    submission_date = db.DateTimeField(required=True)
    # Status open or close. true means open false means close
    status = db.BooleanField(required=True, default=True)
    # Submitted documents
    documents = db.ListField(db.ReferenceField('Document'))
    meta = {
        'collection': 'assignments'
    }


class Document(db.Document):
    # Name of the file
    filename = db.StringField()
    # Which assignment this document belongs to, document being the students submissopm
    assignment = db.ReferenceField('Assignment')
    # Who is submitted the document
    submitted_by = db.ReferenceField('User')
    # When was the document submitted
    submitted_date = db.DateTimeField(required=True, default=datetime.utcnow)
    meta = {
        'collection': 'documents'
    }


class Module1(db.Document):
    # Each document in this collection refers to a different school and contains information about module1 for that school.
    files = db.ListField(db.ReferenceField('File'))
    # The list of files in module1 for that school
    chats = db.ListField(db.ReferenceField('Chat'))
    #'chats' refers to the posts made by a teacher on the 'module post board', was called 'module chat' but i have not since changed the naming convention to match the new feature name
    meta = {
        'collection': 'module1'
    }


class Module2(db.Document):
    # Each document in this collection refers to a different school and contains information about module2 for that school.
    files = db.ListField(db.ReferenceField('File'))
    # The list of files in module2 for that school
    chats = db.ListField(db.ReferenceField('Chat'))
    # List of posts for module post board made by a teacher
    meta = {
        'collection': 'module2'
    }


class Module3(db.Document):
    # Each document in this collection refers to a different school and contains information about module3 for that school.
    files = db.ListField(db.ReferenceField('File'))
    # The list of files in module3 for that school
    chats = db.ListField(db.ReferenceField('Chat'))
    # The list of posts in module3 for that school
    meta = {
        'collection': 'module3'
    }


class Chat(db.Document): #Note: Chat refers to "Module Post Board", It was first called "Module Chat" but changed the name
    # All posts made by module post board are stored in the Chat collection for every school and module.
    # the document id of the post just made is saved to module1/2/3.chats and that is what is used to fetch the correct posts for each school's module
    description = db.StringField(required=True)
    #description is the post itself
    user = db.ReferenceField('User')
    # A user reference to who added this post
    created_at = db.DateTimeField(required=True, default=datetime.utcnow)
    #time the post was made at for display purposes
    meta = {
        'collection': 'chats'
    }


class PersonalQuestions(db.Document):
    # All the fields for PersonalQuestions forum for student sign-up
    gender = db.StringField(required=True)
    age = db.StringField(required=True)
    year = db.StringField(required=True)
    englishspeaker = db.StringField(required=True)
    mornornight = db.StringField(required=True)
    personalsmartphone = db.StringField(required=True)
    phoneaccess = db.StringField(required=True)
    phonehours = db.StringField(required=True)
    phoneactivity = db.StringField
    personalcomputer = db.StringField(required=True)
    computeraccess = db.StringField
    phonehours = db.StringField(required=True)
    phoneactivity = db.ListField
    nocomputer = db.StringField(required=True)
    computerhours = db.StringField(required=True)
    computeractivity = db.ListField
    personaltablet = db.StringField(required=True)
    tablethours = db.StringField(required=True)
    tabletactivity = db.ListField
    programmingexperience = db.StringField(required=True)
    programmingexperiencetime = db.StringField(required=True)
    programminglanguages = db.ListField
    programoften = db.StringField(required=True)
    programminglevel = db.StringField(required=True)
    weborappdev = db.StringField(required=True)
    technologies = db.ListField
    programmingsite = db.ListField
    jclevel = db.StringField(required=True)
    parentoccupation = db.StringField(required=True)

    meta = {
        'collection': 'PersonalQs'
    }

class CSQs(db.Document):
    #All the fields for CS Questions for student sign-up
    userid = db.StringField(required=True)
    studycs = db.StringField(required=True)
    thinkcs = db.StringField(required=True)
    csinteresting = db.StringField(required=True)
    csinterestingwhy = db.StringField
    cschallenging = db.StringField(required=True)
    cschallengingwhy = db.StringField
    internetcentral = db.StringField(required=True)
    wordexcelcentral = db.StringField(required=True)
    installingcentral = db.StringField(required=True)
    programmingcentral = db.StringField(required=True)
    solvingproblemscentral = db.StringField(required=True)
    relatedtomaths = db.StringField(required=True)
    workwithothers = db.StringField(required=True)
    menmorelikely = db.StringField(required=True)
    donenocomputer = db.StringField(required=True)
    heardcompthinking = db.StringField(required=True)
    compthinkingmeaning = db.StringField


    meta = {
        'collection': 'ComputerScienceQs'
    }



class BebrasQuiz1(db.Document):
    #All the fields for the bebras1 quiz, all fields are required as anwser is needed for each field
    email = db.StringField(required=True)
    braclet = db.StringField(required=True)
    animation = db.StringField(required=True)
    animalcompetition = db.StringField(required=True)
    stackcomputer = db.StringField(required=True)
    crosscountry = db.StringField(required=True)
    dicethrow = db.StringField(required=True)
    drawingstars = db.StringField(required=True)
    beaverlunch = db.StringField(required=True)
    wontfind = db.StringField(required=True)
    bowlfactory = db.StringField(required=True)
    fireworks = db.StringField(required=True)
    kangaroo = db.StringField(required=True)
    spies = db.StringField(required=True)
    score = db.IntField(required=True)

    meta = {
        'collection': 'BebrasQuiz1'
    }


class BebrasQuiz2(db.Document):
    #bebras2
    email = db.StringField(required=True)
    bebraspainting = db.StringField(required=True)
    bottles = db.StringField(required=True)
    partyguests = db.StringField(required=True)
    tubesystem = db.StringField(required=True)
    magicpotions = db.StringField(required=True)
    concurrentdirections = db.StringField(required=True)
    secretmessages = db.StringField(required=True)
    triangles = db.StringField(required=True)
    scannercode = db.StringField(required=True)
    thegame = db.StringField(required=True)
    benigma = db.StringField(required=True)
    theatre = db.StringField(required=True)
    piratehunters = db.StringField(required=True)
    score = db.IntField(required=True)


    meta = {
        'collection': 'BebrasQuiz2'
    }



class User(db.DynamicDocument):
    dl_docs_array = db.ListField(db.ReferenceField('File'))
    # This List was to keep track of all the files a user download, feature was not finished
    login_counter = db.IntField()
    # Counter for the amount of times the user has logged in,  feature was not finished
    login_array = db.ListField(db.DateField())
    # List of the last 5 times a user logged in,  feature was not finished, this and two about meant for student progress
    title = db.StringField()
    # Title of user, Mr, Dr etc
    approved = db.BooleanField()
    # Boolean used to check if student is approved to class or not
    name = db.StringField(required=True, max_length=50)
    surname = db.StringField(required=True)
    email = db.EmailField(required=True)
    password = db.BinaryField(required=True)
    user_type = db.StringField(required=True)
    school = db.ReferenceField(School)
    # Here we will store what school the user is in
    posts = db.ListField(db.ReferenceField('Post'))
    # List of all the questions user has added to teacher discussion forum

    meta = {
        'collection': 'users'
    }


class File(db.Document):
    # Each document in this collection refers to a different file
    # Files are NOT stored in database, Files are stored on the machine that is hosting the website
    # Files are stored in the 'Uploads Folder'
    # http://flask.pocoo.org/docs/1.0/patterns/fileuploads/
    user = db.ReferenceField('User')
    filename = db.StringField()
    tags = db.ListField(db.StringField(), default=list)
    created_at = db.DateTimeField(required=True, default=datetime.utcnow)
    meta = {
        'collection': 'files'
    }


class Post(db.Document):
    # For teacher discussion forum, post refers to a question
    # Details for each question asked
    subject = db.StringField()
    author = db.StringField(required=True, max_length=50)
    description = db.StringField()
    created_at = db.DateTimeField(required=True, default=datetime.utcnow)
    comments = db.ListField(db.ReferenceField('Comment'))
    # Post will have a list of comments, comments being replies
    meta = {
        'collection': 'posts'
    }


class Comment(db.DynamicDocument):
    # For replies to questions in teacher discussion forum
    description = db.StringField()
    post = db.ReferenceField('Post')
    # Refernece to what post(question) the comment (reply) is for
    created_at = db.DateTimeField(required=True, default=datetime.utcnow)
    user_id = db.ReferenceField(User)  
    # Store id of the user
    author = db.StringField(required=True, max_length=50)
    meta = {
        'collection': 'comments'
    }
