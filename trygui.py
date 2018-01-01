import easygui as g
import sys

while 1:
	g.msgbox('hi,welcome to the first game')
	msg = 'what would you like to learn'
	title = 'multiactive '
	choices = ['love', 'program', 'OOXX', 'chess and picture']
	choice = g.choicebox(msg, title, choices)
	g.msgbox('you choice is :' + str(choice), 'result')
	msg = 'would you like to play again?'
	title = 'please'
	if g.ccbox(msg, title):
		pass
	else:
		sys.exit(0)
