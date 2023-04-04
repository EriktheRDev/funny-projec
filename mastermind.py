import PySimpleGUI as sg
sg.theme("DarkGreen7")
cue_layout = [[sg.Text("MasterMind")], #[0][0]
[sg.Button("R"), sg.Text("ed   "), sg.Button("O"), sg.Text('range'), sg.Button("Y"), sg.Text('ellow')], [sg.Button("G"), sg.Text('reen'), sg.Button("B"), sg.Text('lue    '), sg.Button("P"), sg.Text('urple')], #[0][1] and [0][2]
[sg.Text("[_]"),sg.Text("[_]"),sg.Text("[_]"),sg.Text("[_]"), sg.Text("L1")], #[0][3]
[sg.Text("[_]"),sg.Text("[_]"),sg.Text("[_]"),sg.Text("[_]"), sg.Text("L2")], #[0][4]
[sg.Text("[_]"),sg.Text("[_]"),sg.Text("[_]"),sg.Text("[_]"), sg.Text("L3")], #[0][5]
[sg.Text("[_]"),sg.Text("[_]"),sg.Text("[_]"),sg.Text("[_]"), sg.Text("L4")], #[0][6]
[sg.Text("[_]"),sg.Text("[_]"),sg.Text("[_]"),sg.Text("[_]"), sg.Text("L5")], #[0][7]
[sg.Text("[_]"),sg.Text("[_]"),sg.Text("[_]"),sg.Text("[_]"), sg.Text("L6")], #[0][8]
[sg.Text("[_]"),sg.Text("[_]"),sg.Text("[_]"),sg.Text("[_]"), sg.Text("L7")], #[0][9]
[sg.Text("[_]"),sg.Text("[_]"),sg.Text("[_]"),sg.Text("[_]"), sg.Text("L8")], #[0][10]
[sg.Text("[_]"),sg.Text("[_]"),sg.Text("[_]"),sg.Text("[_]"), sg.Text("L9")], #[0][11]
[sg.Text("[_]"),sg.Text("[_]"),sg.Text("[_]"),sg.Text("[_]"), sg.Text("L10")], #[0][12]
[sg.Text("[_]"),sg.Text("[_]"),sg.Text("[_]"),sg.Text("[_]"), sg.Text("SOLUTION")], #[0][13] 
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
eventies = ["[_]","[_]","[_]","[_]","[_]","[_]","[_]","[_]","[_]","[_]","[_]","[_]","[_]","[_]","[_]","[_]","[_]","[_]","[_]","[_]","[_]","[_]","[_]","[_]","[_]","[_]","[_]","[_]","[_]","[_]","[_]","[_]","[_]","[_]","[_]","[_]","[_]","[_]","[_]","[_]",]
spot = 0
while True:
    event, values = cue_win.Read()
    if event == sg.WIN_CLOSED:
        break
    if event == "R" or event == "O" or event == "Y" or event == "G" or event == "B" or event == "P":
        eventies[spot] = event
        spot += 1
        if spot == 4 or spot == 8 or spot == 12 or spot == 16 or spot == 20 or spot == 24 or spot == 28 or spot == 32 or spot == 36 or spot == 40:
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
                            del pcorrect[i]
                place = -1
                for i in my_guess:
                    place += 1
                    if i in pcorrect:
                        right_wrong_place += 1
                        del my_guess[place]
                        
                wrong = len(my_guess)
                sg.Popup("Sorry! That's Not Right.\nYou Got " + str(num_right_in_str) + " Characters Correct and in Right Place, \n" + str(right_wrong_place) + " Charactersbut in Wrong Place, \n" + str(wrong) + " Characters Wrong.")    
        cue_win.refresh()
        cue_win.close()
        cue_win = sg.Window(title="MasterMind", layout=[[sg.Text("MasterMind")], #[0][0]
[sg.Button("R"), sg.Text("ed   "), sg.Button("O"), sg.Text('range'), sg.Button("Y"), sg.Text('ellow')], [sg.Button("G"), sg.Text('reen'), sg.Button("B"), sg.Text('lue    '), sg.Button("P"), sg.Text('urple')], #[0][1] and [0][2]
[sg.Text(eventies[0]),sg.Text(eventies[1]),sg.Text(eventies[2]),sg.Text(eventies[3]), sg.Text("L1")],
[sg.Text(eventies[4]),sg.Text(eventies[5]),sg.Text(eventies[6]),sg.Text(eventies[7]), sg.Text("L2")],
[sg.Text(eventies[8]),sg.Text(eventies[9]),sg.Text(eventies[10]),sg.Text(eventies[11]), sg.Text("L3")],
[sg.Text(eventies[12]),sg.Text(eventies[13]),sg.Text(eventies[14]),sg.Text(eventies[15]), sg.Text("L4")],
[sg.Text(eventies[16]),sg.Text(eventies[17]),sg.Text(eventies[18]),sg.Text(eventies[19]), sg.Text("L5")],
[sg.Text(eventies[20]),sg.Text(eventies[21]),sg.Text(eventies[22]),sg.Text(eventies[23]), sg.Text("L6")],
[sg.Text(eventies[24]),sg.Text(eventies[25]),sg.Text(eventies[26]),sg.Text(eventies[27]), sg.Text("L7")],
[sg.Text(eventies[28]),sg.Text(eventies[29]),sg.Text(eventies[30]),sg.Text(eventies[31]), sg.Text("L8")],
[sg.Text(eventies[32]),sg.Text(eventies[33]),sg.Text(eventies[34]),sg.Text(eventies[35]), sg.Text("L9")],
[sg.Text(eventies[36]),sg.Text(eventies[37]),sg.Text(eventies[38]),sg.Text(eventies[39]), sg.Text("L10")],
[sg.Text("[_]"),sg.Text("[_]"),sg.Text("[_]"),sg.Text("[_]"), sg.Text("SOLUTION")]]) #[0][13] )
cue_win.close()
