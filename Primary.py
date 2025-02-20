#import datetime
from flet.core import page
#import data_gather
import flet as ft
from flet.core.types import TextAlign
from Homework1 import TODONOW
from data_gather import DataGather

datagath = DataGather()
DataGather()
print("blub")
def mains(page: ft.Page):
    page.bgcolor = ft.Colors.INDIGO_300
    name = ft.TextField(hint_text="can you repeat your name enter here and press plus when your done\n i know we literaly just asked this but for now please retype as same syntax as before")
    def Todo(e):
        #Toodo = TODONOW()
        #Toodo()
        print("to-do")
    # signifies the user wants to view the calender
    def calender(e):
        print("calender")
    #signifies the script is ready to move on
    def haveName(e):
        page.clean()
        page.bgcolor = ft.Colors.INDIGO_500
        page.add(ft.TextField(hint_text="Welcome, click the drop down menu to see your to-do lists or calender", text_size=20, color=ft.Colors.WHITE))
        #drop down menu
        pb = ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(
                    text="Calender", checked=False, on_click=calender
                ),
                ft.PopupMenuItem(
                    text="To-Do lists", checked=False, on_click=Todo
                )
            ]
        )
        page.add(pb)
    #enter button calling haveName function
    page.add(name, ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=haveName))

#allows script to run independantly
ft.app(mains)



