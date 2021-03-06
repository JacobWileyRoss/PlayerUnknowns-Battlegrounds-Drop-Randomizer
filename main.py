import random
from tkinter import *
from tkinter.ttk import *

window = Tk()
window.geometry('460x215')
window.title("PUGB Drop Randomizer")


pubgBG = PhotoImage(file="pubgBG.gif")
background = Label(window, image=pubgBG)
background.pack()


lbl = Label(window, text="Select Map")
lbl.config(font=("Verdana", 20))
lbl.place(x=230, y=100, anchor="center")


map_select = Combobox(window)
map_select['values'] = ("Erangel", "Sanhok", "Miramar", "Vikendi")
map_select.place(x=230, y=50, anchor="center")


game_map = map_select.get()
drops = ""


def update_map_select(event):
    global game_map
    global drops
    game_map = map_select.get()
    print(game_map)
    if game_map == "Erangel":
        drops = ["Kameshki", "Zharki", "Stalber", "Northwest Bunker", "West Bunker", "East Bunker", "Shooting Range",
                 "Yasnaya Compound", "Plane Crash", "Georgopol", "Yasnaya Polyana", "Rozhok", "Hospital",
                 "Georgopol Hills", "Ruins", "Water Town", "School", "Apartments", "Mansion", "Lipovka", "Hay Farm",
                 "Gatka", "Pochinki", "Pochinki Hills", "Shelter", "Prison", "Gatka Radio", "Gatka Trenches",
                 "Woodcutter Camp", "Mylta Power", "Swamp Town", "Farmlands", "Farm Ridge", "Farm", "Mylta",
                 "Factory", "Quarry", "Ridge Comples", "Primolsk", "Ferry Pier", "Novorepnoye",
                 "Novorepnoye Radio", "Sosnovka Military Base"]
    elif game_map == "Miramar":
        drops = ["Torre Ahumada", "Campo Militar", "Alcantara", "La Cobreria", "Cruz del Valle", "Tierra Bronca",
                 "Ruins", "Trailer Park", "Crater Fields", "Water Treatment", "El Pozo", "San Martin",
                 "Hacienda del Patron", "El Azahar", "Monte Nuevo", "Power Grid", "Graveyard", "Minas Generales",
                 "Pecado", "La Bendita", " Impala", "Ladrillera", "Chumacera", "Los Leones", "Valle del Mar", "Mines",
                 "Puerto Paraiso", "Prison", "Minas del Sur", "Los Higos"]
    elif game_map == "Sanhok":
        drops = ["Khao", "Mongnai", "Tat Mok", "Ha Tinh", "Paradise Resort", "Camp Bravo", "Camp Alpha", "Bootcamp",
                 "Bhan", "Lakawi", "Ruins", "Pai Nan", "Quarry", "Kampong", "Ruins", "Pai Nan", "Tambang", "Cave",
                 "Na Kham", "Sahmee", "Camp Charlie", "Docks", "Ban Tai"]
    elif game_map == "Vikendi":
        drops = ["Dobro Mesto", "Goroka", "Podvosto", "Volnova", "Abbey", "Cantra", "Krichas", "Milnar", "Movatra",
                 "Pilnec", "Peshkova", "Tovar", "Trevno", "Vihar", "Zabava", "Dino Park", "Castle", "Cement Factory",
                 "Cosomodrome", "Hot Springs", "Villa", "Lumber Yard", "Mount Kreznic", "Port", "Sawmill", "Winery"]


def clicked():
    lbl.configure(text=str(random.choice(drops)))


btn = Button(window, text="Drop", command=clicked)
btn.place(x=230, y=175, anchor="center")
map_select.bind("<<ComboboxSelected>>", update_map_select)


window.mainloop()
