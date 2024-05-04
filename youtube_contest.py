#подключение библиотек
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout,QRadioButton,QGroupBox,QHBoxLayout , QButtonGroup,QMessageBox
from random import *

class Question():
    def __init__ (self, question,right_answer,wrong1,wrong2,wrong3):
        self.question =question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
 
question_list =[]
question_list.append(Question('Кто действующий президент Кыргызстана?','Садыр Жапаров','Курманбек Бакиев','Роза Отунбаева','Соронбай Жээнбеков'))#правильный-2
question_list.append(Question('Кто изобрёл вилку?','Томас Кориэт','Джеймс Смит','Конор Элберт','Еллизавета Уайт '))#правильный-2
question_list.append(Question('Родина яблони?','Казахстан','Германия','Франция','Россия'))#правильный-2
question_list.append(Question('Самый высокогорный город в России?','Тырнауз','Азнакаево','Калуга','Тверь'))
question_list.append(Question('Где вы сейчас находитесь?',' Пушкина 47',' Пушкина 23','Пушкина 35','Пушкина 29'))
question_list.append(Question('Где находиться Сыктывкар от центра России?','На Востоке','На юге','На севре','на западе'))
question_list.append(Question('Какой инструмент используют в шахтах?','Койло','Терменвокс','Кельма','Терки'))
question_list.append(Question('Какое имя настоящее?','Даян','Самора','Далина','Марани'))
question_list.append(Question('Что такое натуропатия?','Лечение природными средствами','боязнь растений','ненависть к растениям','боязнь стать растением'))


app =QApplication([])
window = QWidget()
window.setWindowTitle("Викторина")
lb_Question = QLabel('а?')
btn_Ok = QPushButton('Ответить')
radioGroups=QGroupBox('Варианты ответа')
RGroup = QButtonGroup()
rbtn1 = QRadioButton('2')
rbtn2 = QRadioButton('0')
rbtn3 = QRadioButton('2')
rbtn4 = QRadioButton('3')
RGroup.addButton(rbtn1)
RGroup.addButton(rbtn2)
RGroup.addButton(rbtn3)
RGroup.addButton(rbtn4)
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn2)
layout_ans2.addWidget(rbtn1)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
radioGroups.setLayout(layout_ans1)


AGBox =QGroupBox('Результаты теста:')
lb_result = QLabel('Прав или не прав')
lb_correct = QLabel('правильный ответ:')
layout_results =QVBoxLayout()
layout_results.addWidget(lb_result,alignment =(Qt.AlignHCenter | Qt.AlignVCenter) )
layout_results.addWidget(lb_correct,alignment = Qt.AlignHCenter, stretch = 2)
AGBox.setLayout(layout_results)
AGBox.hide()


line1 =QHBoxLayout()
line2 =QHBoxLayout()
line3 =QHBoxLayout()

line1.addWidget(lb_Question, alignment =(Qt.AlignHCenter | Qt.AlignVCenter))
line2.addWidget(radioGroups)
line2.addWidget(AGBox)
line3.addStretch(1)
line3.addWidget(btn_Ok, stretch = 2)
line3.addStretch(1)

line = QVBoxLayout()
line.addLayout(line1, stretch = 2)
line.addLayout(line2, stretch = 8)
line.addStretch(1)
line.addLayout(line3)
line.addStretch(1)
line.setSpacing(100)

def show_result():
    radioGroups.hide()
    AGBox.show()
    btn_Ok.setText('следующий вопрос')

def Show_Q():
    radioGroups.show()
    AGBox.hide()
    btn_Ok.setText('Ответить')
    RGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RGroup.setExclusive(True)



answers = [rbtn1,rbtn2,rbtn3,rbtn4]
 
def ask (q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_correct.setText(q.right_answer)
    Show_Q()
 
def show_correct(result):
    lb_result.setText(result)
    show_result()

def check_answer():
    if answers[0].isChecked():
        window.score += 1
        show_correct('правильно')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('неправильно')

def MSBox(result):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(result)
    msg.setWindowTitle('Итог:')
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()
   
def next_questiom():
    window.total += 1
    window.cur_question +=1
    if window.cur_question >= len(question_list):
        MSBox('Ваш результат:'+ str(window.score)+ ' из '+ str(window.total-1))
        window.cur_question = 00
    else:
        q =question_list[window.cur_question]
        ask(q)
def click_Ok():
    if btn_Ok.text()=="Ответить":
        check_answer()
    else:
        next_questiom()


window.setLayout(line)
window.cur_question = -1
window.total = 0
window.score = 0
btn_Ok.clicked.connect(click_Ok)
next_questiom()
window.show()

app.exec()

