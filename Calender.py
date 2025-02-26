
import flet as ft

class createcalender():
    print("nada")
    def go(self):
        print("go")

    grabpass = open("infoPassing.txt", 'r')
    print("opened")
    for line in grabpass:
        content = grabpass.readline()
        print(content + "content")
        if content == "extracuriculars":
            print("keyword found ec")
            close = "true"
        else:
            close = "false"
    if close == "false":
        print("keywod not found")
        print("calender interface")


    #ft.app(main)
    from Extracurricular import Extracurricular
