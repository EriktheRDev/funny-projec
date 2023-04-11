import PySimpleGUI as sg
sg.theme("DarkGreen7")
cue_layout = [[sg.Text("MasterMind")], #[0][0]
[sg.Button("R"), sg.Text("ed   "), sg.Button("O"), sg.Text('range'), sg.Button("Y"), sg.Text('ellow')], [sg.Button("G"), sg.Text('reen'), sg.Button("B"), sg.Text('lue    '), sg.Button("P"), sg.Text('urple')], #[0][1] and [0][2]
[sg.Text("[_]"),sg.Text("[_]"),sg.Text("[_]"),sg.Text("[_]"), sg.Text("L1")] #[0][3]
]
print("MasterMind Log")
import random
possibilities = ['R', 'O', 'Y', 'G', 'B', 'P']
correct = ['0','0','0','0']
correct[0] = possibilities[random.randint(0, 5)]
correct[1] = possibilities[random.randint(0, 5)]
correct[2] = possibilities[random.randint(0, 5)]
correct[3] = possibilities[random.randint(0, 5)]
cue_win = sg.Window(title="MasterMind", layout=cue_layout)
current_level = 3
print(correct)
eventies = ["[_]","[_]","[_]","[_]"]
spot = 0
while True:
    event, values = cue_win.Read()
    if event == sg.WIN_CLOSED:
        break
    if event == "R" or event == "O" or event == "Y" or event == "G" or event == "B" or event == "P":
        eventies[spot] = event
        spot += 1
        if spot == 4:
            print("ding")
            cor_str = ""
            my_str = ""
            my_guess = [eventies[spot - 4], eventies[spot - 3], eventies[spot - 2], eventies[spot - 1]]
            for i in correct:
                cor_str += str(i)
            for i in my_guess:
                my_str += str(i)
            print(cor_str)
            print(correct)
            print(my_str)
            if cor_str == my_str:
                sg.Popup("You Win!!!!!")
                break
            else:
                num_right_in_str = 0
                right_wrong_place = 0
                pcorrect = correct
                for i in range(0, len(pcorrect) - 1):
                    if my_guess[i] == pcorrect[i]:
                            num_right_in_str += 1
                            del my_guess[i]
                            
                place = -1
                for i in my_guess:
                    place += 1
                    if i in pcorrect:
                        right_wrong_place += 1
                        del my_guess[place]
                        
                wrong = len(my_guess)
                sg.Popup("Sorry! That's Not Right.\nYou Got " + str(num_right_in_str) + " Characters Correct and in Right Place, \n" + str(right_wrong_place) + " Charactersbut in Wrong Place, \n" + str(wrong) + " Characters Wrong.")
                sg.Popup("GAME OVER\nSOLUTION:" + str(correct)
        cue_win.refresh()
        cue_win.close()
        cue_win = sg.Window(title="MasterMind", layout=[[sg.Text("MasterMind")], #[0][0]
[sg.Button("R"), sg.Text("ed   "), sg.Button("O"), sg.Text('range'), sg.Button("Y"), sg.Text('ellow')], [sg.Button("G"), sg.Text('reen'), sg.Button("B"), sg.Text('lue    '), sg.Button("P"), sg.Text('urple')], #[0][1] and [0][2]
[sg.Text(eventies[0]),sg.Text(eventies[1]),sg.Text(eventies[2]),sg.Text(eventies[3]), sg.Text("L1")]])
cue_win.close()
