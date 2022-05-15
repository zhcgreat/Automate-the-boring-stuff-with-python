#! python3
# randonQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.
import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 quiz files.
for quizNum in range (35):
    # Creat the quiz and answer key files.
    quizFile = open('capitalsquiz%s.txt' %(quizNum+1) , 'w') #quizNum是从0开始的，所以需要+1
    answerKeyFile = open('capitalsquiz_answers%s.txt' %(quizNum +1), 'w')

    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate::\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (form %s)' %(quizNum+1))
    quizFile.write('\n\n')

    # Shuffle the oreder of the States.
    states = list(capitals.keys())
    random.shuffle(states)

    #Loop through all 50 states, making a question for each.
    for questionNum in range(50):
        #get right answer and wrong answer.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)] #.index()会返回wrongAnswrs中correctAnswer的序号
        wrongAnswers = random.sample(wrongAnswers, 3) #random.sample会随机从wrongAnswers中截取3个元素组成新的列表
        answerOption = wrongAnswers + [correctAnswer]
        random.shuffle(answerOption)
        # Write the question and the answer options to the quiz.
        quizFile.write('%s. What is the capital of %s?\n' %(questionNum +1, states[questionNum]))
        for i in range(4):
        quizFile.write(' %s. %s\n' %('ABCD'[i], answerOption[i]))
        quizFile.write('\n')
        # Write the answer key to a file.
        answerKeyFile.write(' %s. %s\n' %(questionNum+1, 'ABCD'[answerOption.index(correctAnswer)]))
    quizFile.close()  #原书中本版此处有缩进错误，英文版无误，下同。
    answerKeyFile.close()
