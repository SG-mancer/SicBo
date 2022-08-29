# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
init:

    image bg sicboboard = "bg sicboboard.png"
# The game starts here.

label start:

    scene bg sicboboard
    
    call sicBoStart
    jump placeBets

    return
