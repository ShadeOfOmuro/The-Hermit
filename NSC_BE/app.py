from flask import *
app = Flask(__name__)
class backpack :
    question = ["Nan","1" , "2" , "3"  , "4"  , "5"  , "6"  , "7"  , "8"  , "9"  , "10"]
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
    if(backpack.curr_question > 10) :
        return redirect("/mindwave")

    else :
        return redirect("/choicequiz")
@app.route("/mindwave")
def render_mindwave() :
    #dostuff()
    return render_template("mindwave.html")

@app.route("/full_result")
def render_test_result() :
    return render_template("result.html")

app.run(debug=True)