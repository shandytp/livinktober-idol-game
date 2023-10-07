# Define Characters
define f = Character("Fadhil", who_color = "#91300f")
define n = Character("Narator")
define i = Character("Indira", who_color = "#C62AE5")
define y = Character("Yuura", who_color = "#F58F0D")
define r = Character("Rifuki", who_color = "#BBB0E1")

# Define Images
image bg street = im.FactorScale("images/bg-street.jpg", 0.5, 0.5)
image fadhil happy = "images/fadhil-face.png"
image bg discord = "images/bg-discord-full.jpg"
image snow_hala livium = "images/snow-hala-livium.jpg"
image snow_hala livium_dim = "images/snow-hala-livium-dim.jpg"
image indira_gelinding = im.FactorScale("images/indira-gelinding.jpg", 0.5, 0.5)
image indira_gelinding dim = "images/indira-gelinding-dim.jpg"
image yuura_tua = im.FactorScale("images/yuura-tua.png", 0.5, 0.5)
image yuura_tua dim = "images/yuura-tua-dim.jpg"
image imas_149 bg= "images/bg-imas.jpg"
image dipenjara dim = "images/dipenjara-bg-dim.jpg"

# Define song
define audio.snow_hala_livium = "snow-hala-livium-song.ogg"
define audio.orang_pinggiran = "orang-pinggiran-ost.ogg"
define audio.nenek_tua = "nenek-tua-ost.ogg"
define audio.imas_ost = "imas-ost.ogg"
define audio.kotak_susu_ost = "kotak-susu-ost.ogg"

# The game starts here.

label start:

    # play kotak susu song
    play music kotak_susu_ost volume 0.15

    scene bg street

    n "Pada suatu hari di Kota Livium..."
    
    show fadhil happy at truecenter
    with moveinright

    # These display lines of dialogue.

    f "Hmm... Livinktober dah sampe hari ke-7 nich..."
    f "Kira - kira tema hari ini apaan ya...?"
    f "Bentar ah cek Discord Livium dulu..."

    scene bg discord at truecenter 
    with dissolve
    pause

    f "Aaahh..."
    f "Udah gw duga pasti Ngab Mada yang punya ide ini 😠"

    scene bg street
    with dissolve

    n "Pada saat itulah tiba - tiba dari atas sana muncullah {b}empat {b}pilihan ini..."
    
menu:
    "Tirai Satu":
        jump tirai_satu

    "Tirai Dua":
        jump tirai_dua
    
    "Kotak":
        jump kotak

    "Kantong":
        jump kantong


label tirai_satu:
    n "Tirai Satu adalah..."
    n "Project Livium Snow Halation!!!"

    # play snow hala livium song
    play music snow_hala_livium volume 0.15

    scene snow_hala livium
    pause

    f "Oma omagaa... Yesen yesennah..."

    scene snow_hala livium_dim

    centered "{size=+36}Todokete setsuna sa ni wa...{/size}"

    return

label tirai_dua:
    n "Tirai Dua adalah..."
    n "u149!!!"

    # play u149 song
    play music imas_ost volume 0.15

    show imas_149 bg
    with dissolve
    pause

    r "UWOGHHHHHHHHHHHH!!!!"
    
    scene dipenjara dim

    centered "{size=+36}Damn, dipenjara...{/size}"    

    return

label kotak:
    n "Kotak ini berisi..."
    n "Nona Indira yang belum mandi dan nggelinding di jalan 😭"

    # play orang pinggiran ost
    play music orang_pinggiran volume 0.15

    show indira_gelinding at truecenter
    with dissolve

    i "Kaakkk... Saya laper kakkk... 😭😭😭"
    f "Yhaaaaa... Baukkk!!!"

    scene indira_gelinding dim

    centered "{size=+36}Non... Mandi Non 😭{/size}"

    return

label kantong:
    n "Kantong ini berisi..."
    n "Yuura yang udah tua 😅😅😅"

    # play nenek sudah tua song
    play music nenek_tua volume 0.15

    show yuura_tua at truecenter
    with dissolve

    y "Naak... Kamu ngeliat tongkatnya Nenek nggak...? 😩😩😩"
    f "Yaa... Gimana ya Nek... 😅"

    show yuura_tua dim

    centered "{size=+36}Nenek Sudah Tua...{/size}"

    return
