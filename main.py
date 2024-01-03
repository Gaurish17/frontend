from flask import Flask, render_template, request, redirect, url_for,send_from_directory

app = Flask(__name__)

poem = "Unlock Your Heart !"  # Placeholder for poem
journey = ""  # Placeholder for romantic journey

# Sample questions and options
questions = [
    {"id": 1 ,"question": "What is my favorite hobby ?", "options": ["dancing", "singing", "troubling you", "sleeping"]},
    {"id": 2 ,"question": "What is your favourite part of our relationship? And least favourite?", "options": ["texting", "Calling", "doing nothing","other"]},
    {"id": 3 ,"question": "What’s an embarrassing thing you’ve done and never told anyone about?","options" : ["tell"]},
    {"id": 4 ,"question": "choose","options" : ["Dating me !!!!!","World Tour with me","Video calling shreya","spending rest your life with mom - dad"]},
    {"id": 5 ,"question": "What if you become Gaurish and he becomes Darshi , how you are gonna treat her  ? ","options" : ["Tell","Ofcourse he will be hottest darshika ever "]},
    {"id": 6 ,"question": "What is best thing you love and i can gift you right noww ?", "options": ["Chocolates", "Cake", "Guess"]},
    {"id": 7 ,"question": "since you guessed wrong here is your punishment !! hehe","options": ["Make video of me while you hold my hand "]}
]

current_question_index = 0
user_answers = {}

@app.route("/")
def index():
    global poem
    return render_template("index.html", poem=poem)

@app.route("/reveal", methods=["POST"])
def reveal():
    global poem
    poem = """
        Ham Ko Mili Hain Aaj, Ye Ghadiyaan Nasib Se
        
        Ji Bhar Ke Dekh Lijiye Ham Ko Karib Se
        
        Phir Aap Ke Nasib Men Ye Baat Ho Na Ho
        
        Shaayad Phir Is Janam Men Mulaaqaat Ho Na Ho
         ..."""  # Replace with your actual poem
    return render_template("index.html", poem=poem)


@app.route("/record_answer", methods=["POST"])
def record_answer():
    selected_answer = request.form.get('answer')
    question_id = int(request.form.get('question_id'))

    # Handle recording of the user's answer here
    # You might want to store the answers in a database or some data structure
    print(f"Question ID: {question_id}, Selected answer: {selected_answer}")

    # For now, redirect to the next question or a thank you page
    # Replace 'next_question' with the actual route for the next question
    return redirect(url_for('questionnaire'))

@app.route("/flowers")
def flowers():
    return render_template("flowers.html")

@app.route('/pic', methods=["GET","POST"])
def pic():
    return render_template('pic.html')

@app.route("/blos")
def blos():
    return render_template("blos.html")

# current_question_index = 0  # Keep track of the current question
recorded_answers = {}
@app.route("/questionnaire", methods=["GET", "POST"])
def questionnaire():
    global current_question_index

    if request.method == "POST":
        answer = request.form.get("answer")
        question_id = int(request.form.get("question_id"))
        recorded_answers[question_id] = answer

        current_question_index += 1

    if current_question_index < len(questions):
        current_question = questions[current_question_index]
        return render_template("questionnaire.html", current_question=current_question)
    else:
        return render_template("thank_you.html", recorded_answers=recorded_answers)

if __name__ == "__main__":
    app.run(debug=True)
