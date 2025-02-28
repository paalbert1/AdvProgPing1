#import datetime
from os import WNOWAIT, write

from flet.core import page
#import data_gather
import flet as ft
import datetime
from flet.core.types import TextAlign
#from Homework import HomeworkApp
user = open("CurrentUser.txt", 'w')
user.write("\n")
user.close()
user = open("CurrentUser.txt", 'r')
for line in user:
    line.strip()
    print("strept")
user.close()
from data_gather import DataGather
datagath = DataGather()
DataGather()
grabpass = open("infoPassing.txt", 'r')
name = grabpass.readline()
print("hii " + name)
for line in grabpass:
    line.strip()
grabpass.close()
user = open("CurrentUser.txt", 'w')
user.write(name)
user.close()

def mains(page: ft.Page):
    place = "Homework"
    page.bgcolor = ft.Colors.INDIGO_300
    #name = ft.TextField(hint_text="can you repeat your name enter here and press plus when your done\n i know we literaly just asked this but for now please retype as same syntax as before")
    def Todo(e):
        #todotime()
        grabpass = open("infoPassing.txt", 'w')
        grabpass.write("\n")
        grabpass.write("todo")
        grabpass.close()
        page.window.close()
        return
        #Homeworkcl(ft.Row)
        #HomeworkApp()
    # signifies the user wants to view the calender
    def ExtraCuriculars(e):
        print("extracuriculars called")
        grabpass = open("infoPassing.txt", 'w')
        grabpass.write("\n")
        grabpass.write("extracuriculars")
        grabpass.close()
        page.window.close()
    def calender(e):
        grabpass = open("infoPassing.txt", 'w')
        grabpass.write("\n")
        grabpass.write("calender")
        grabpass.close()
        page.window.close()
    #signifies the script is ready to move on
    def haveName():
        page.clean()
        page.bgcolor = ft.Colors.INDIGO_500
        page.add(
            ft.Row([ft.Text(value="Welcome " + name, theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM)],
                   alignment=ft.MainAxisAlignment.CENTER),
            ft.Column(spacing=25,),
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ))
        page.add(
            ft.Row([ft.Text(value="click the drop down menu to see your to-do lists, calender or extracurriculars", theme_style=ft.TextThemeStyle.BODY_LARGE)],
                   alignment=ft.MainAxisAlignment.CENTER),
            ft.Column(spacing=20, ),
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ))

        #page.add(ft.TextField(hint_text="Welcome " + name, text_size=20, color=ft.Colors.WHITE))
        #page.add(
            #ft.TextField(hint_text=" ",
                        # text_size=20, color=ft.Colors.WHITE))
        # drop down menu
        #drop down menu
        pb = ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(
                    text="Calender", checked=False, on_click=calender
                ),
                ft.PopupMenuItem(
                    text="To-Do lists", checked=False, on_click=Todo
                ),
                ft.PopupMenuItem(
                    text="Manage Extracurriculars", checked=False, on_click=ExtraCuriculars
                )
            ]
        )
        page.add(pb)
    #enter button calling haveName function
    haveName()
    #page.add(name, ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=haveName))

#allows script to run independantly
ft.app(mains)
from Homework import Toodo

#from Extracurricular import Extracurricular
#createcalender()


#TODONOW = Toodo()
#Toodo()





