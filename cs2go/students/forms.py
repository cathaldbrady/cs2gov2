from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, RadioField, BooleanField, SelectMultipleField
from wtforms.widgets import PasswordInput, ListWidget, CheckboxInput
from wtforms.validators import InputRequired, Length, DataRequired, Required

class StudentForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Length(max=30)])
    name = StringField('First Name', validators=[InputRequired()])
    surname = StringField('Last Name', validators=[InputRequired()])
    password = StringField('Password', widget=PasswordInput(hide_value=False))
    school = SelectField('School', coerce=str, validators=[DataRequired()], id='school')
    school_name = StringField('School Name')
    submit = SubmitField('Register')

class StudentPersonalQs(FlaskForm):
    Gender = RadioField('Gender', choices = [('Male','Male'),('Female','Female')])
    Age = SelectField('Age', choices = [('12', '12'), ('13', '14'),('15', '15'), ('16', '16'),('17', '17'), ('18+', '18+')])
    Year = SelectField('Year', choices = [('1st year', '1st year'), ('2nd year', '2nd year'),('3rd year', '3rd year'), ('4th year', '4th year'),('5th year', '5th year'), ('6th year', '6th year')])
    NativeEnglishSpeaker = RadioField('NativeEnglishSpeaker', validators=[InputRequired('Fix this please12111')] , choices = [('Yes','Yes'),('No','No')])
    MorningOrNight = RadioField('MorningOrNight', choices = [('Morning','Morning'),('Night','Night'),('No preference','No preference')])
    OwnSmartPhone = RadioField('OwnSmartPhone', choices = [('Yes','Yes'),('No','No')])
    HaveSphoneAccess = StringField('HaveSphoneAccess')
    PhoneHours = SelectField('PhoneHours', choices = [('Less than 1 hour', 'Less than 1 hour'), ('1-3 hours', '1-3 hours'),('More than 3 hours', 'More than 3 hours'), ('None', 'None')])
    PhoneActivity = SelectMultipleField('PhoneActivity', choices = [('Texting (SMS)','Texting (SMS)'),('Calling (using the phones network)','Calling (using the phones network)'),
                                                                        ('Other forms of messaging (Facebook Messenger, Whatsapp, Viber etc.)','Other forms of messaging (Facebook Messenger, Whatsapp, Viber etc.)'),('Facebook','Facebook'),
                                                                        ('Snapchat','Snapchat'),('Instagram','Instagram'),
                                                                        ('Browsing the web (using Safari/Chrome etc.)','Browsing the web (using Safari/Chrome etc.)'),('Playing games','Playing games'),
                                                                        ('Looking up news/information (BBC, RTE, Wikipedia etc.)','Looking up news/information (BBC, RTE, Wikipedia etc.)'),('Taking photos','Taking photos'),
                                                                        ('Sending/reading emails','Sending/reading emails'),('Reading books/newspapers etc.','Reading books/newspapers etc.'),
                                                                        ('Listen to music (ITunes, Spotify)','Listen to music (ITunes, Spotify)'),('Watch videos (using Netflix, YouTube etc.)','Watch videos (using Netflix, YouTube etc.)'),
                                                                        ('Other','Other')])
    OwnPersonalComputer = RadioField('OwnPersonalComputer', choices = [('Yes','Yes'),('No','No')])
    HaveComputerAccess = StringField('HaveComputerAccess')
    ComputerHours = SelectField('ComputerHours',  choices = [('Less than 1 hour', 'Less than 1 hour'), ('1-3 hours', '1-3 hours'),('More than 3 hours', 'More than 3 hours'), ('None', 'None')]) 
    ComputerActivity = SelectMultipleField('ComputerActivity', choices = [
                                                                    ('Instagram','Instagram'),('Browsing the web (using Safari/Chrome etc.)','Browsing the web (using Safari/Chrome etc.)'),
                                                                    ('Facebook & other social media','Facebook & other social media'),('Playing games','Playing games'),
                                                                    ('Looking up news/information (BBC, RTE, Wikipedia etc.)','Looking up news/information (BBC, RTE, Wikipedia etc.)'),('Sending/reading emails','Sending/reading emails'),
                                                                    ('School work or similar (using Word, Powerpoint etc.)','School work or similar (using Word, Powerpoint etc.)'),
                                                                    ('Watch videos (using Netflix, YouTube etc.)','Watch videos (using Netflix, YouTube etc.)'),('Listening to music','Listening to music'),
                                                                    ('Other','Other')])
    OwnTablet = RadioField('OwnTablet',   choices = [('Yes','Yes'),('No','No')])
    TabletHours = SelectField('TabletHours',   choices = [('Less than 1 hour', 'Less than 1 hour'), ('1-3 hours', '1-3 hours'),('More than 3 hours', 'More than 3 hours'), ('None', 'None')])
    TabletActivity = SelectMultipleField('TabletActivity', choices = [('Instagram','Instagram'),('Browsing the web (using Safari/Chrome etc.)','Browsing the web (using Safari/Chrome etc.)'),
                                                                    ('Facebook','Facebook'),('Playing games','Playing games'),
                                                                    ('Looking up news/information (BBC, RTE, Wikipedia etc.)','Looking up news/information (BBC, RTE, Wikipedia etc.)'),('Sending/reading emails','Sending/reading emails'),
                                                                    ('Snapchat','Snapchat'),('Reading books/newspapers etc.','Reading books/newspapers etc.'),
                                                                    ('Some form of texting/messaging (Facebook Messenger, Whatsapp, Viber etc.)','Some form of texting/messaging (Facebook Messenger, Whatsapp, Viber etc.)'),('Listening to music','Listening to music'),
                                                                    ('Watch videos (using Netflix, YouTube etc.)','Watch videos (using Netflix, YouTube etc.)'),('Other','Other')])
    ProgrammingExperience = RadioField('ProgrammingExperience',  choices = [('Yes','Yes'),('No','No')])           
    ProgrammingExperienceTime = SelectField('ProgrammingExperienceTime',   choices = [('I have never programmed before', 'I have never programmed before'),('I have programmed once or twice', 'I have programmed once or twice'),
                                                                    ('I have done programming a number of times', 'I have done programming a number of times'), ('I have been programming for over a year', 'I have been programming for over a year')])
    ProgrammingLanguages = SelectMultipleField('ProgrammingLanguages', choices = [('Java','Java'),('Python','Python'),
                                                                        ('Scratch','Scratch'),('C/C++','C/C++'),
                                                                        ('JavaScript','JavaScript'),('Other','Other')])
    ProgramOften = RadioField('ProgramOften',   choices = [('Never','Never'),('Barely','Barely'),
                                                        ('Occassionly','Ocassionly'),('Often','Often'),
                                                        ('Daily','Daily')])
    PersonalProgrammingProficiency = RadioField('PersonalProgrammingProficiency',  choices = [('Bad','Bad'),('Not the best','Not the best'),
                                                        ('Average','Average'),('Good','Good'),
                                                        ('Excellent','Excellent')])
    DoneWebOrAppDev = RadioField('DoneWebOrAppDev',   choices = [('Yes','Yes'),('No','No')])
    KnownTechnologies  = SelectMultipleField('KnownTechnologies ', choices = [('HTML','HTML'),('CSS','CSS'),
                                                                    ('JavaScript','JavaScript'),('PHP or other server-side langauge','PHP or other server-side langauge'),
                                                                    ('App Inventor','App Inventor'),('Android Studio','Android Studio'),
                                                                    ('XCode (Apple App Development tool)','XCode (Apple App Development tool)')])
    ProgrammingSites = SelectMultipleField('ProgrammingSites', choices = [('Bebras challenge','Bebras challenge'),('Codecademy','Codecademy'),
                                                                        ('Khan Academy','Khan Academy'),('Udacity','Udacity'),
                                                                        ('Kangaroo Maths','Kangaroo Maths'),('Call to Code','Call to Code'),
                                                                        ('Hour of Code (code.org)','Hour of Code (code.org)'),('AILO (All Ireland Linguistics Olympiad)','AILO (All Ireland Linguistics Olympiad)'),
                                                                        ('None of the above','None of the above'),('Other','Other')])
    JuniorCertLevel = RadioField('JuniorCertLevel', choices = [('Foundation','Foundation'),('Ordinary ','Ordinary '),('Higher','Higher')])
    ITParentOccupation = RadioField('ITParentOccupation', choices = [('Yes','Yes'),('No','No'),('Not Sure','Not Sure')])
    Submit = SubmitField('Submit')


class StudentCSQs(FlaskForm):
    StudyCSUni = RadioField('StudyCSUni' , choices = [('Yes','Yes'),('No','No'),('Maybe','Maybe')])
    ThinkOfCS = StringField('ThinkOfCS')
    CSInteresting = RadioField('CSInteresting', choices = [('Yes','Yes'),('No','No')])
    CSInterestingWhy = StringField('CSInterestingWhy')
    CSChallenging =  RadioField('CSChallenging', choices = [('Yes','Yes'),('No','No')])
    CSChallengingWhy = StringField('CSChallengingWhy')
    InternetCentral = RadioField('InternetCentral', choices =[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    WordExcelCentral = RadioField('WordExcelCentral', choices =[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    InstallingCentral = RadioField('InstallingCentral', choices =[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    ProgrammingCentral = RadioField('ProgrammingCentral', choices =[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    SolvingProblemsCentral = RadioField('SolvingProblemsCentral', choices =[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    RelatedToMaths  = RadioField('RelatedToMaths', choices =[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    WorkWithOthers = RadioField('WorkWithOthers', choices =[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    MenMoreLikely = RadioField('MenMoreLikely', choices =[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    DoneNoComputer = RadioField('DoneNoComputer', choices =[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    HeardOfCompThinking =  RadioField('HeardOfCompThinking', choices = [('Yes','Yes'),('No','No')])
    CompThinkingMeaning = StringField('CompThinkingMeaning')
    Submit = SubmitField('Submit')

class EditForm(FlaskForm):
    name = StringField('First Name', validators=[InputRequired()])
    surname = StringField('Last Name', validators=[InputRequired()])
    submit = SubmitField('Update')
