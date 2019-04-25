from flask import Blueprint, render_template, request, session, redirect, url_for, flash
import sys
from cs2go.bebras.forms import Bebras1, Bebras2
from cs2go.models import BebrasQuiz1, BebrasQuiz2
from bson import ObjectId
import datetime


bebras_blueprint = Blueprint('bebras',
                            __name__,
                            template_folder='templates/bebras')
#route for bebrasquiz1
@bebras_blueprint.route('/bebrasquiz1', methods=['GET', 'POST'])
def bebrasquiz1():
    form = Bebras1(request.form)
    #get form data
    if request.method == 'POST' and form.validate():
        bebrasquiz = BebrasQuiz1()
        #create instance of the BebrasQuiz1 model and assign data
        bebrasquiz.email = session['email']
        bebrasquiz.braclet = form.Braclet.data
        bebrasquiz.animation = form.Animation.data
        bebrasquiz.animalcompetition = form.AnimalCompetition.data
        bebrasquiz.crosscountry = form.CrossCountry.data
        bebrasquiz.stackcomputer = form.StackComputer.data
        bebrasquiz.dicethrow = form.DiceThrow.data
        bebrasquiz.drawingstars = form.DrawingStars.data
        bebrasquiz.beaverlunch = form.BeaverLunch.data
        bebrasquiz.wontfind = form.YouWontFind.data
        bebrasquiz.bowlfactory = form.BowlFactory.data
        bebrasquiz.fireworks = form.Fireworks.data
        bebrasquiz.kangaroo = form.Kangaroo.data
        bebrasquiz.spies = form.Spies.data
        bebrasquiz.score = bebras1results(form)
        #save the document to bebras1 collection in db
        bebrasquiz.save()

        return redirect(url_for('bebras.quiz1result'))

    elif request.method == 'POST' and form.validate() == False:
        #if form validation fails, display the errors to the user
        if form.errors:
            errors = form.errors
            for i in errors:
                flash(i)

    return render_template('bebras1.html', form=form)
#function to calculate the grade of bebras1 wuiz
def bebras1results(form):
    braclet = form.Braclet.data
    animation = form.Animation.data
    animalcompetition = form.AnimalCompetition.data
    stackcomputer = form.StackComputer.data
    crosscountry = form.CrossCountry.data
    dicethrow = form.DiceThrow.data
    drawingstars = form.DrawingStars.data
    beaverlunch = form.BeaverLunch.data
    wontfind = form.YouWontFind.data
    bowlfactory = form.BowlFactory.data
    fireworks = form.Fireworks.data
    kangaroo = form.Kangaroo.data
    spies = form.Spies.data
    score = 0
    questions = [braclet, animation, animalcompetition, crosscountry, stackcomputer, dicethrow, drawingstars, beaverlunch, wontfind, bowlfactory, fireworks, kangaroo, spies] 
    questionslower = [x.lower() for x in questions]


    anwsers = ["b","bdcae","6","C. Mr Brown, Mrs Green, Mrs Pink","4 8 3 + * 2","c","10:4","D","FLOOD","4","4","I","4"]
    answerslower = [x.lower() for x in anwsers]
    #convert all lower case so capitalisation is not considered

    for x in range(0, len(questionslower)):
        if questionslower[x] == answerslower[x]:
            score += 1

    return round((score / 13) * 100)
    #return the grade the student got in the quiz

#function to calculate the grade of bebras1 wuiz
def bebras2results(form):
    bebraspainting = form.BebrasPainting.data
    bottles = form.Bottles.data
    partyguests = form.PartyGuests.data
    tubesystem = form.TubeSystem.data
    magicpotions = form.MagicPotions.data
    concurrentdirections = form.ConcurrentDirections.data
    secretmessages = form.SecretMessages.data
    triangles = form.Triangles.data
    scannercode = form.ScannerCode.data
    thegame = form.TheGame.data
    benigma = form.Benigma.data
    theatre = form.Theatre.data
    piratehunters = form.PirateHunters.data
    score = 0
    questions = [bebraspainting, bottles, partyguests, tubesystem, magicpotions, concurrentdirections, secretmessages, triangles, scannercode, thegame, benigma, theatre, piratehunters]
    questionslower = [x.lower() for x in questions]

    answers = ["b", "A. E D C B A","NotSure","3","Beaker D","B. N, E, E, S, E","B. OKIWILLBETHERE!","b","D","5.1","D. UOOUPQ","NotSure","D. The police have no chance of winning"]
    
    answerslower = [x.lower() for x in answers]


    for x in range(0, len(questionslower)):
        if questionslower[x] == answerslower[x]:
            score += 1

    return round((score / 13) * 100)


#route for bebrasquiz2
@bebras_blueprint.route('/bebrasquiz2', methods=['GET', 'POST'])
def bebrasquiz2():
    form = Bebras2(request.form)
    if request.method == 'POST' and form.validate(): 
        bebrasquiz = BebrasQuiz2()
        #create instance of Berasquiz2 model and assign data
        bebrasquiz.email = session['email']
        bebrasquiz.bebraspainting = form.BebrasPainting.data
        bebrasquiz.bottles = form.Bottles.data
        bebrasquiz.partyguests = form.PartyGuests.data
        bebrasquiz.tubesystem = form.TubeSystem.data
        bebrasquiz.magicpotions = form.MagicPotions.data
        bebrasquiz.concurrentdirections = form.ConcurrentDirections.data
        bebrasquiz.secretmessages = form.SecretMessages.data
        bebrasquiz.triangles = form.Triangles.data
        bebrasquiz.scannercode = form.ScannerCode.data
        bebrasquiz.thegame = form.TheGame.data
        bebrasquiz.benigma = form.Benigma.data
        bebrasquiz.theatre = form.Theatre.data
        bebrasquiz.piratehunters = form.PirateHunters.data
        bebrasquiz.score = bebras2results(form)
        bebrasquiz.save()

        return redirect(url_for('bebras.quiz2result'))

    elif request.method == 'POST' and form.validate() == False:
        if form.errors:
            errors = form.errors
            for i in errors:
                flash(i)

    return render_template('bebras2.html', form=form)



@bebras_blueprint.route('/bebrasquiz1result', methods=['GET', 'POST'])
def quiz1result():
    bebras = BebrasQuiz1.objects().get(email=session['email'])

    return render_template('bebrasResults.html', bebras=bebras)

    
@bebras_blueprint.route('/bebrasquiz2result', methods=['GET', 'POST'])
def quiz2result():
    bebras = BebrasQuiz2.objects().get(email=session['email'])

    return render_template('bebrasResults2.html', bebras=bebras)


