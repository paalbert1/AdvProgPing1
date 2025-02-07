#import datetime
from flet.core import page
#import data_gather
import flet as ft
class Primary():
    def mains(page: ft.Page):
        page.bgcolor = ft.Colors.INDIGO_300
        name = ft.TextField(hint_text="can you repeat your name enter here and press plus when your done\n i know we literaly just asked this but for now please retype as same syntax as before")
        #def
        #    print("hi")
        def haveName(e):
            page.clean()
            page.bgcolor = ft.Colors.INDIGO_300
            page.add(
                ft.Image(
                    src = f"https://media.istockphoto.com/id/1212381977/vector/simple-flat-design-calendar-icon.jpg?s=612x612&w=0&k=20&c=lkzyW-wiFd-uHLJ9tRkLYzWA5joCCuJ4d_tifuHdANs="
                    ,
                    width = 250,
                    height = 250,

                ),
                ft.Image(
                    src=f"https://c8.alamy.com/comp/2G9EG6G/checklist-in-spiral-notebook-to-do-list-icon-in-simple-outline-design-wishlist-icon-vector-illustration-isolated-on-white-background-editable-2G9EG6G.jpg"
                    ,
                    width=290,
                    height=290,
                    #on_click=toDo(e)
                ))

        page.add(name, ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=haveName))


    ft.app(mains)



