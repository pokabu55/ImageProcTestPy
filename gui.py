import PySimpleGUI as sg

# デザインテーマの設定
sg.theme("DarkAmber")

# ウィンドウに配置するコンポーネント
layout = [  [sg.Text("ここは１行目")],
            [sg.Text("ここは、２行目：適当な文字をいれてください"), sg.InputText()],
            [sg.Button("OK."), sg.Button("Cancel.")]
        ]

# ウィンドウの生成
window = sg.Window("サンプルプログラム", layout)

# イベントループ
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancel.":
        break
    elif event == "OK.":
        print("your input is : ", values[0])

window.close()

pushのお試しように記述

