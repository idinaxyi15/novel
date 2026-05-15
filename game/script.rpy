# ========================персонажики===============================

#-------------гг
define gg = Character('[viname]', color="#9d00c19a", cps=25)

#-----------нпс
define mother = Character('Мать', color="#8c0000ff", cps=25)
define father = Character('Отец', color="#0d0073ff", cps=25)
define Holy_Mother = Character('Игуменья', color="#3b0000ff", cps=25 )
define Holy_Father = Character('Игумен', color="#0a003aff", cps=25)


define alter = Character('???', color="#a0a0a0", cps=25, what_italic=True)


# Игра начинается здесь:
label start:

    # ВВОД ИМЕНИ (без выбора пола)
    $ viname = renpy.input('Введите ваше имя, игра идет от женского лица', 'Маргарита')
    
    if not viname:
        $ viname = 'Маргарита'
    
jump glava1_beginning