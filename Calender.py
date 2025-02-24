
import flet as ft

class createcalender():
    print("nada")
    def go(self):
        return
    def main(self):
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
            ft.app(self.go)


    ft.app(main)
    print("Extracuricular called")
    #from Extracurricular import Extracurricular
