#!/usr/local/bin/python
import flaskwebgui
from flask import *
import read_mindwave_mobile
import threading
import att_model , lowa_model , lowb_model
import matplotlib.pyplot as plt
app = Flask(__name__)
ui = flaskwebgui.FlaskUI(app)
class datapackMW : 
    Delta = []
    Theta = []
    LowAlpha = []
    HighAlpha = []
    LowBeta = []
    HighBeta = []
    LowGamma = []
    MedGamma = []
    AttentionLevel = []
    PoorSignalLevel = []
    Unknowdatapoint = []
    MeditationLevel = []

def print_end() :
    print('end')


def render_measure() :
    t = threading.Thread(target= read_mindwave_mobile.start_measure)
    t.run()
    return render_template("measure.html")



class backpack :
    question = ["0", "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "10"]
    curr_question = 1
    score = 0
    Name = ""
    age = 0
    sex = 0
    # for sex 
    # 0 = male
    # 1 = female 
@app.route("/")
def render_main() :
    backpack.curr_question = 1
    backpack.score = 0
    backpack.name = ""
    backpack.age = 0
    backpack.sex = 0
    return render_template("index.html")

@app.route("/info") 
def render_info() :
    return render_template("info.html")
@app.route("/registeration")
def render_register() :
    return render_template("register.html")
@app.route("/formhandler" , methods=["POST"])
def do_sth_with_data() :
    backpack.age = request.form.get("age")
    backpack.name = request.form.get("name")
    backpack.sex = request.form.get("sex")
    print(backpack.age,"\n")
    print(backpack.name,"\n")
    print(backpack.sex,"\n")
    return redirect("/choicequiz")
@app.route("/choicequiz")
def render_quiz() :
    return render_template("quiz.html" , question = backpack.question[backpack.curr_question])
@app.route("/quizhandler" , methods=['POST'])
def redirect_to_quiz() :
    backpack.score += int(request.form.get("score"))
    print(backpack.score)
    backpack.curr_question+=1
    if(backpack.curr_question > 9) :
        return redirect("/mindwave")

    else :
        return redirect("/choicequiz")
@app.route("/mindwave")
def render_mindwave() :
    return render_template("mindwave.html")
@app.route("/mindwave_test")
def render_mindwave_test() :
    t = threading.Thread(target= read_mindwave_mobile.start_measure)
    t.start();
    # try :
    #     t.run()
    # except :
    #     return render_template("error.html")
    return render_template("handler.html")
@app.route('/slide_txt')
def reds() :
    return render_template('mindwave_test.html')
@app.route('/slideshow')
def redss() :
    return render_template('mindwave_test2.html')
@app.route("/result")
def render_result() :
    read_mindwave_mobile.datapack.kill_code = True
    datapackMW.Delta += read_mindwave_mobile.Delta
    datapackMW.Theta += read_mindwave_mobile.Theta
    datapackMW.LowAlpha += read_mindwave_mobile.LowAlpha
    datapackMW.HighAlpha += read_mindwave_mobile.HighAlpha
    datapackMW.LowBeta += read_mindwave_mobile.LowBeta
    datapackMW.HighBeta += read_mindwave_mobile.HighBeta
    datapackMW.LowGamma += read_mindwave_mobile.LowGamma
    datapackMW.MedGamma += read_mindwave_mobile.MedGamma
    datapackMW.AttentionLevel += read_mindwave_mobile.AttentionLevel
    datapackMW.MeditationLevel += read_mindwave_mobile.MeditationLevel
    t = threading.Thread(target = print_end)
    t.run()
    return redirect('/result_handler')
@app.route("/result_handler")
def render_result_renderer() :
    print('stopping')
    Att_result = att_model.predict([datapackMW.AttentionLevel[19:47]])
    Worr_result = lowb_model.predict([datapackMW.LowBeta[19:47]])
    Happi_result = lowa_model.predict([datapackMW.LowAlpha[19:47]])
    print({'Att' : Att_result , 'Happ' : Happi_result , 'Worr' : Worr_result})
    print("END")
    predict_handler = {'Att' : Att_result , 'Happ' : Happi_result , 'Worr' : Worr_result}
    MwScore = 0
    if (predict_handler['Att'] == 0) :
        MwScore+= int(0.8846*35)
    else :
        MwScore += 0
    if (predict_handler['Happ'] == 0) :
        MwScore+= int(0.8823*35)
    else :
        MwScore += 0
    if (predict_handler['Worr'] == 0) :
        MwScore+= int(0.8214*35)
    else :
        MwScore += 0
    case = str()
    if(backpack.score + MwScore <= 21 + 9) :
        case = '0'
    elif (backpack.score + MwScore <= 42 + 18) :
        case = '1'
    elif (backpack.score + MwScore <= 63 + 27) :
        case = '2'
    elif (backpack.score + MwScore <= 84 + 36) :
        case = '3'
    elif (backpack.score + MwScore <= 105 + 45) :
        case = '4'
    overallscore = MwScore + backpack.score
    backpack.name.replace(" " , '%20')
    link_togo = 'http://app.montfort.ac.th/the-hermit/api' + '?n=' 
    link_togo +=  str(backpack.name.replace(' ','%20')) + '&a=' + str(backpack.age) + '&os=' + str(overallscore) 
    link_togo +=  '&ms=' + str(MwScore) + '&c=' 
    link_togo +=  str(backpack.score) + '&s=' + str(case) 
    link_togo += '&hs=' + str(predict_handler['Happ']) + '&ws=' 
    link_togo += str(predict_handler['Worr']) + '&atts=' + str(predict_handler['Att'])
    print(link_togo)
    print(backpack.name , backpack.age , MwScore , backpack.score , predict_handler['Happ'] , predict_handler['Worr'] , predict_handler['Att'] , case)
    percent_choice = int(backpack.score/45*100)/100
    percent_mindwave = int(MwScore/105 * 100)/100
    percent_all = int(overallscore/150*100)/100
    return render_template("result.html" , link_togo = link_togo , status =  case , cp = percent_choice , mp = percent_mindwave , op = percent_all)
app.run()
# ui.run()
