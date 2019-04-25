from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, RadioField, BooleanField, SelectMultipleField
from wtforms.widgets import PasswordInput
from wtforms.validators import InputRequired, Length, DataRequired




class Bebras1(FlaskForm):
    Braclet = RadioField('Braclet', choices = [('a','a'),('b','b'),('c','c'),('d','d')])
    Animation = StringField('Animation', validators=[InputRequired()])
    AnimalCompetition = RadioField('AnimalCompetition', choices = [('2','2'),('3','3'),('5','5'),('6','6'),('7','7')])
    CrossCountry = RadioField('CrossCountry', choices = [('A. Mrs Pink, Mr Brown, Mrs Green','A. Mrs Pink, Mr Brown, Mrs Green'),('B. Mr Brown, Mrs Pink, Mrs Green','B. Mr Brown, Mrs Pink, Mrs Green'),
            	                                       ('C. Mr Brown, Mrs Green, Mrs Pink','C. Mr Brown, Mrs Green, Mrs Pink'),('D. Mrs Green, Mrs Pink, Mr Brown','D. Mrs Green, Mrs Pink, Mr Brown')])
    StackComputer = StringField('StackComputer', validators=[InputRequired()])
    DiceThrow = RadioField('DiceThrow', choices = [('a','a'),('b','b'),('c','c'),('d','d')])
    DrawingStars = RadioField('DrawingStars', choices = [('9:3','9:3'),('9:4','9:4'),('10:4','10:4'),('10:5','10:5')])
    BeaverLunch = RadioField('BeaverLunch', choices = [('a','a'),('b','b'),('c','c'),('d','d')])
    YouWontFind = RadioField('YouWontFind', choices = [('RIVER','RIVER'),('KNOCK','KNOCK'),('FLOOD','FLOOD'),('LODGE','LODGE')])
    BowlFactory = StringField('BowlFactory', validators=[InputRequired()])
    Fireworks = RadioField('Fireworks', choices = [('0','0'),('1','1'),('2','2'),('3','3'),('4','4')])
    Kangaroo = RadioField('Kangaroo', choices = [('A','A'),('B','B'),('C','C'),('D','D'),('E','E'),('F','F'),('G','G'),('H','H'), ('I','I'), ('J','J')])
    Spies = RadioField('Spies', choices = [('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    Submit = SubmitField('Submit')


class Bebras2(FlaskForm):
    BebrasPainting = RadioField('BebrasPainting', choices = [('a','a'),('b','b'),('c','c'),('d','d')])
    Bottles = RadioField('Bottles', choices = [('A. E D C B A','A. E D C B A'),('B. D B C A E','B. D B C A E'),('C. E C D A B','C. E C D A B'),('D. D C E B A','D. D C E B A')])
    PartyGuests = StringField('PartyGuests', validators=[InputRequired()])
    TubeSystem = RadioField('TubeSystem', choices = [('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    MagicPotions = RadioField('MagicPotions', choices = [('Beaker A','Beaker A'),('Beaker B','Beaker B'),(' Beaker C',' Beaker C'),('Beaker D','Beaker D'),(' Beaker E',' Beaker E'),('Beaker F','Beaker F')])
    ConcurrentDirections = RadioField('ConcurrentDirections', choices = [('A. N, E, E, E','A. N, E, E, E'),('B. N, E, E, S, E','B. N, E, E, S, E'),('C. N, N, S, E, N','C. N, N, S, E, N'),('D. N, E, E, S, W','D. N, E, E, S, W')])
    SecretMessages = RadioField('SecretMessages', choices = [('A. OKWHERETOMEET!','A. OKWHERETOMEET!'),('B. OKIWILLBETHERE!','B. OKIWILLBETHERE!'),('C. WILLYOUBETHERETOO?','C. WILLYOUBETHERETOO?'),('D. OKIWILLMEETHIM!','D. OKIWILLMEETHIM!')])
    Triangles = RadioField('Triangles', choices = [('a','a'),('b','b'),('c','c'),('d','d')])
    ScannerCode = RadioField('ScannerCode', choices = [('a','a'),('b','b'),('c','c'),('d','d')])
    TheGame = StringField('TheGame', validators=[InputRequired()])
    Benigma = RadioField('Benigma', choices = [('A. UOSAEB','A. UOSAEB'),('B. UOUQOP','B. UOUQOP'),('C. UOOOIP','C. UOOOIP'),('D. UOOUPQ','D. UOOUPQ')]) 
    Theatre = StringField('Theatre', validators=[InputRequired()])
    PirateHunters = RadioField('PirateHunters', choices = [('A. The police win in 2 turns','A. The police win in 2 turns'),('B. The police win in 3 turns','B. The police win in 3 turns'),('C. The police win in 5 turns','C. The police win in 5 turns'),('D. The police have no chance of winning','D. The police have no chance of winning')])
    Submit = SubmitField('Submit')

