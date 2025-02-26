# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Indrihs", color="#b3ff30")
define a = Character("", color="#ffffff")

# The game starts here.
image indrihs = "indrihs/indrihs_1.png"
image indrihs_smile = "indrihs/indrihs_2.png"
image klase1 = "bg/cassroom1.png"
image visvaris1 = "bg/visvaris_scene1.png"
transform half_size: 
    zoom 0.5 #adjust as required
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene visvaris1

    a "Visvaris pieceļas no miega fizikas kabinētā"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    scene klase1

    show indrihs at half_size
    with dissolve

    # These display lines of dialogue.

    e "Aļo, beidz gulēt"
    hide indrihs
    show indrihs_smile at half_size
    e "sigma"

    # This ends the game.

    return
