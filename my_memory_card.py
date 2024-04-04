from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle
from random import randint

#класс Question

class Question():
    def __init__(self, question, ult, wrong1, wrong2, wrong3):
        self.question = question
        self.ult = ult
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

#функция обработки события

def show_result():
    radioGroupBox_q.hide()
    radioGroupBox_a.show()
    answer.setText('Следующий вопрос')
def show_question():
    radioGroupBox_a.hide()
    radioGroupBox_q.show()
    answer.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)
def click_OK():
    
    if answer.text() == 'Ответить':
        check_answer()
    else:
        next_q()
def aska(q: Question):
    shuffle(answers)
    answers[0].setText(q.ult)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    ult.setText(q.ult)
    show_question()
def show_correct(res):
    ult.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_correct('правильно)))')
        main_win.score += 1
    else:
        if (answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked()):
            show_correct(f'Неправильно, тупой ты ******\n Правильный ответ: {ult.text()}')
    if main_win.total != 0:
        rating = main_win.score / main_win.total * 100
        print('Рейтинг:',rating,'%')
        print(f'Статистика:\n- Всего вопросов: {main_win.total}\n- Правильных ответов: {main_win.score}')
def next_q():
    main_win.total += 1
    cur_question = randint(0, len(q_list) - 1)
    q = q_list[cur_question]
    aska(q)
    print(f'Статистика:\n- Всего вопросов: {main_win.total}\n- Правильных ответов: {main_win.score}')
    
memory_card = QApplication([])
main_win = QWidget()
main_win.cur_question = -1
main_win.setWindowTitle('Memory Card')
main_win.resize(600,400)

#вопрос и ответы

question = QLabel('Готов начать?')
answer = QPushButton('Ответить')
radioGroupBox_q = QGroupBox('Варианты ответов')
rbtn1 = QRadioButton('Да')
rbtn2 = QRadioButton('Нет')
rbtn3 = QRadioButton('Не особо')
rbtn4 = QRadioButton('Лееееень')

#группа кнопок

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

#список ответов

answers = [rbtn1, rbtn2, rbtn3, rbtn4]

#лейауты для группы

h_line_group = QHBoxLayout()
v_line_group1 = QVBoxLayout()
v_line_group2 = QVBoxLayout()
v_line_group1.addWidget(rbtn1, alignment = Qt.AlignCenter)
v_line_group1.addWidget(rbtn2, alignment = Qt.AlignCenter)
v_line_group2.addWidget(rbtn3, alignment = Qt.AlignCenter)
v_line_group2.addWidget(rbtn4, alignment = Qt.AlignCenter)
h_line_group.addLayout(v_line_group1)
h_line_group.addLayout(v_line_group2)
radioGroupBox_q.setLayout(h_line_group)
h_line3 = QVBoxLayout()
h_line3.addWidget(radioGroupBox_q)

#лейауты для окна

main_v_line = QVBoxLayout()
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
h_line1.addWidget(question, alignment = (Qt.AlignHCenter |Qt.AlignVCenter))

main_v_line.addLayout(h_line1)
main_v_line.addLayout(h_line3)

main_win.setLayout(main_v_line)

#новая группа

radioGroupBox_a = QGroupBox('Результат теста')
res = QLabel('Правильно/Неправильно')
ult = QLabel('Да')
ve_line_group = QVBoxLayout()
ve_line_group.addWidget(res, alignment = Qt.AlignCenter)
ve_line_group.addWidget(ult, alignment = Qt.AlignCenter)
radioGroupBox_a.setLayout(ve_line_group)
main_v_line.addWidget(radioGroupBox_a)
h_line2.addWidget(answer, stretch = 2)
main_v_line.addLayout(h_line2)
radioGroupBox_a.hide()

#конец

q_list = []
q = Question('Государственный язык Бразилии', 'Португальский', 'Испанский', 'Итальянский', 'Бразильский')
q1 = Question('Самая популярная часть Sims', 'Sims 2', 'Sims 3', 'Sims(первая часть)', 'Sims 4')
q2 = Question('Кто является президентом РФ?', 'В. В. Путин', 'И. В. Сталин', 'Н. С. Хрущёв', 'Л. И. Брежнев')
q3 = Question('Кто является женой Кристиана Пойхоко Де Ланя?', 'Сэдэо-чан', 'Анна', 'Сакура', 'Сам Кристиан')
q4 = Question('Кто душевный отец Рьюго?', 'Лилит', 'Фазиль', 'Никто', 'Лорин')
q5 = Question('Как называется корейский комикс?', 'Манхва', 'Манга', 'Маньхуа', 'Руманга')
q6 = Question('Кто является женой Кристиана Пойхоко Де Ланя?(вторая версия)', 'Винсент', 'Анна', 'Сакура', 'Сам Кристиан')
q7 = Question('Как звали первенца семьи Эйландеров?', 'Яков', 'Элизабет', 'Давид', 'Николас')
q8 = Question('Кто создал первый способ просветления?', 'Каролина Эйландер', 'Яков', 'Мистер Ворон(Олдос Вандербум)', 'Уильям Вандербум')
q9 = Question('Кто такая Лора Вандербум?', 'Перерождённый Уильям Вандербум', 'Искалеченная душа', 'Перерождение Харви', 'Просто дочь Розы Вандербум')
q10 = Question('Кто такой Харви?','Персонаж, достигнувший просветления', 'Попугай','Перерождение детектива Вандермеера','Перерождение мистера Ворона(Олдоса Вандербума)')
q11 = Question('Зачем убили Каролину Эйландер?', 'Чтобы достигнуть просветления', 'Просто так', 'Из-за ненависти к ней', 'Она была опасна')
q12 = Question('Самое древнее растение с фотоснтезом', 'Цианобактерия', 'Митохондрия', 'Алое', 'Пластида обыкновенная')
q13 = Question('Призналась ли Маринетт Эдриану в чувствах?', 'МЯмеспСПсМЯМеЯМ', 'Да', 'Нет', 'Они женаты')
q14 = Question('Цвет логотипа алгоритмики','Фиолетовый', 'Жёлтый', 'Красный', 'Синий')
q15 = Question('Кто такая Земфира?', 'Певица', 'Танцовщица', 'Депутат', 'Дворник')
q16 = Question('Как расшифровывается КиШ?', 'Король и Шут', 'Корона и шутка', 'Кирилл и Шапка', 'Колдун и Шаман')
q17 = Question('Что такое "база"?', 'Основа', 'Base', 'База', 'Слово')
q18 = Question('Символ евреев', 'Щит Давида', 'Звезда', 'Пентаграмма', 'Крест')
q19 = Question('Windows - это...', 'Операционная система', 'Окна', 'Двери', 'Приложение')

q_list.append(q)
q_list.append(q1)
q_list.append(q2)
q_list.append(q3)
q_list.append(q4)
q_list.append(q5)
q_list.append(q6)
q_list.append(q7)
q_list.append(q8)
q_list.append(q9)
q_list.append(q10)
q_list.append(q11)
q_list.append(q12)
q_list.append(q13)
q_list.append(q14)
q_list.append(q15)
q_list.append(q16)
q_list.append(q17)
q_list.append(q18)
q_list.append(q19)
answer.clicked.connect(click_OK)
main_win.score = 0
main_win.total = 0
next_q()
main_win.show()
memory_card.exec_()