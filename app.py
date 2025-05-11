from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for session management

# Sample quiz questions
questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['Paris', 'London', 'Berlin', 'Madrid'],
        'answer': 'Paris'
    },
    {
        'question': 'What is 2 + 2?',
        'options': ['3', '4', '5', '6'],
        'answer': '4'
    },
    {
        'question': 'Which language is primarily used for web development?',
        'options': ['Python', 'JavaScript', 'C++', 'Java'],
        'answer': 'JavaScript'
    },
    {
        'question': 'What is the largest planet in our solar system?',
        'options': ['Earth', 'Jupiter', 'Saturn', 'Mars'],
        'answer': 'Jupiter'
    },
    {
        'question': 'Who wrote the play "Romeo and Juliet"?',
        'options': ['William Shakespeare', 'Charles Dickens', 'Mark Twain', 'Jane Austen'],
        'answer': 'William Shakespeare'
    },
    {
        'question': 'What is the chemical symbol for water?',
        'options': ['H2O', 'O2', 'CO2', 'NaCl'],
        'answer': 'H2O'
    },
    {
        'question': 'Which country is known as the Land of the Rising Sun?',
        'options': ['China', 'Japan', 'South Korea', 'Thailand'],
        'answer': 'Japan'
    },
    {
        'question': 'What is the process by which plants make their food?',
        'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Germination'],
        'answer': 'Photosynthesis'
    },
    {
        'question': 'Who painted the Mona Lisa?',
        'options': ['Leonardo da Vinci', 'Vincent van Gogh', 'Pablo Picasso', 'Claude Monet'],
        'answer': 'Leonardo da Vinci'
    },
    {
        'question': 'What is the boiling point of water at sea level?',
        'options': ['90°C', '100°C', '110°C', '120°C'],
        'answer': '100°C'
    }
]

@app.route('/')
def index():
    session['score'] = 0
    session['current_question'] = 0
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    current_question = session.get('current_question', 0)
    score = session.get('score', 0)

    if request.method == 'POST':
        selected_option = request.form.get('option')
        if selected_option == questions[current_question]['answer']:
            score += 1
            session['score'] = score
        current_question += 1
        session['current_question'] = current_question

    if current_question >= len(questions):
        return redirect(url_for('result'))

    question = questions[current_question]
    return render_template('quiz.html', question=question, question_number=current_question + 1, total_questions=len(questions))

@app.route('/result')
def result():
    score = session.get('score', 0)
    total_questions = len(questions)
    return render_template('result.html', score=score, total_questions=total_questions)

@app.route('/leaderboard')
def leaderboard():
    # Placeholder static data for leaderboard
    leaderboard_data = [
        {'rank': 1, 'name': 'Alex', 'score': 95, 'time': '1m 20s'},
        {'rank': 2, 'name': 'Jordan', 'score': 90, 'time': '2m 05s'},
        {'rank': 3, 'name': 'Priya', 'score': 89, 'time': '1m 55s'},
        {'rank': 4, 'name': 'Sam', 'score': 85, 'time': '2m 30s'},
        {'rank': 5, 'name': 'Lee', 'score': 80, 'time': '3m 10s'},
    ]
    return render_template('leaderboard.html', leaderboard=leaderboard_data)

if __name__ == '__main__':
    app.run(debug=True)
