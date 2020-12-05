#!/usr/local/bin/python
from flask import *
import read_mindwave_mobile
import threading
app = Flask(__name__)

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

def force_stop_test() :
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
    print("END")


def render_measure() :
    t = threading.Thread(target= read_mindwave_mobile.start_measure)
    t.run()
    return render_template("measure.html")


def render_end() :
    force_stop_test()
    # plt.plot(datapackMW.Delta)
    # plt.plot(datapackMW.Theta)
    # plt.plot(datapackMW.LowAlpha)
    # plt.plot(datapackMW.HighAlpha)
    # plt.plot(datapackMW.LowBeta)
    # plt.plot(datapackMW.HighBeta)
    # plt.plot(datapackMW.LowGamma)
    # plt.plot(datapackMW.MedGamma)
    # plt.plot(datapackMW.AttentionLevel)
    # plt.plot(datapackMW.MeditationLevel)
    # plt.show()
    return Response(str())


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
    t = threading.Thread(target= read_mindwave_mobile.start_measure)
    t.run()
    return render_template("mindwave.html")

@app.route("/full_result")
def render_test_result() :
    return render_template("result.html")

app.run(debug=True)