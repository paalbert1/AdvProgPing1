import datetime
import flet as ft
from flet.core import page
grabpass = open("infoPassing.txt", 'w')
#grabpass.write("\n")
grabpass.close()
grabpass = open("infoPassing.txt", 'r')
for line in grabpass:
    line.strip()
grabpass.close()
#from Primary import Primary
#from flet.core.alignment import center
close = "n"
blocks = ["A", "B", "C", "D", "E", "F", "H1", "H2", "H3"]
class_titles = []
counter = 0
subject = blocks[counter]
class DataGather:
    def data_gather(page: ft.Page):
        page.bgcolor = ft.Colors.INDIGO_300

        counter = 0
        #subject = blocks[counter]
        def classes_good(e):
            def write_data(e):
                page.clean()
                page.update()
                f = open(name.value + ".txt", "a")
                f.write(Day_of_week.value + "\n" + AorB.value)
                for title in class_titles:
                    f.write("\n" + title)
                f.close()
                #Primary.py()
            page.clean()  # Remove all controls from the page
            page.update()
            Day_of_week = ft.TextField(hint_text="what day of the week is today?")
            page.add(Day_of_week)
            AorB = ft.TextField(hint_text="which week is it? A/B ")
            page.add(AorB, ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=write_data))


            #page.add(ft.TextField(" type none if you dont have a class then"))
        def classes_redo(e):
            page.clean()  # Remove all controls from the page
            page.update()
            print("redo")
            class_titles.clear()
            new_task = ft.TextField( hint_text="Enter your classes by clicking on this text and hit the plus mark to record them")
            page.add(new_task, ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_clicked))
            page.add(ft.TextField("when your finished type 'done' please record them in this order ['A', 'B', 'C', 'D', 'E', 'F', 'H1', 'H2', 'H3'] "))
            page.add(ft.TextField(" type none if you dont have a class then"))
        def add_clicked(e):
            page.add(ft.Checkbox(label=new_task.value))
            class_titles.append(new_task.value)
            page.update()
            new_task.value = ""

            print(class_titles)
            for class_title in class_titles:
                if class_title == "done":
                    class_titles.remove("done")
                    page.clean()
                    page.update()
                    #classes_good.value = ""
                    classesgood = ft.TextField(hint_text="are these all of your classes: type y/n " +"when done click the plus button")
                    page.add(classesgood)
                    for title in class_titles:
                        page.add(ft.TextField(title))
                    def add_clicked2(e):
                        print(classesgood)
                        print(classesgood.value)
                        if classesgood.value == "y":
                            classes_good(e)
                        elif classesgood.value == "n":
                            classes_redo(e)
                    page.add(ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_clicked2))
                    #page.add(ft.FloatingActionButton(icon=ft.Icons.ADD_CIRCLE, on_click=classes_good))
                    #page.add(ft.Button(icon=ft.Icons.CAR_CRASH, on_click=classes_redo))

        new_task = ft.TextField(hint_text="Enter your classes by clicking on this text and hit the plus mark to record them")
        def NameEntered():
            page.clean()
            page.add(new_task, ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_clicked))
            page.add(ft.TextField("when your finished type 'done' please record them in this order ['A', 'B', 'C', 'D', 'E', 'F', 'H1', 'H2', 'H3'] "))
            page.add(ft.TextField(" type none if you dont have a class then"))
        currnt = datetime.datetime.now()
        name = ft.TextField(hint_text="whats your name enter here and press plus when your done")
        def addname():
            b = open("users.txt", "a")
            b.write(name.value + "\n")
        def checkname(e):
            USR = open("users.txt", 'r')
            count = 0
            for line in USR:
                count += 1
                content = USR.readline()
                print("hi")
                print(content)
                keyWord = name.value + "\n"
                if keyWord == content:
                    next()
                    return
                else:
                    found = "false"
            if found == "false":
                addname()
                NameEntered()

            USR.close()

        page.add (name, ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=checkname))
        def addhorsey():
            page.add(
                ft.Container(
                    content=ft.Image(
                        src = f"https://media.istockphoto.com/id/1129584570/vector/flying-pegasus-horse-black-vector-design.jpg?s=612x612&w=0&k=20&c=GkiLrH4bo7bmfOYyjtJdQ2sDIz4eK2Jx5o5g3bWGwPQ="
                    ,
                    width=250,
                    height=250
                    ),
                    margin=50,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.Colors.DEEP_PURPLE_50,
                    width=300,
                    height=300,
                    border_radius=10,
            ))
        addhorsey()
        def next():
            grabpass = open("infoPassing.txt", 'a')
            grabpass.write(name.value + "\n")
            grabpass.close()
            page.window.close()




    ft.app(data_gather)







