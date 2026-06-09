import turtle
import random
import math

screen = turtle.Screen()
screen.setup(width=900, height=650)
screen.bgcolor("black")
screen.title("Constellation – Le Cheval")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

bg = turtle.Turtle()
bg.hideturtle()
bg.speed(0)
bg.penup()
etoiles = [
    
    (-180, 150,  9, "white"),         
    (-210, 120,  7, "lightyellow"),   
    (-230,  90,  6, "lightyellow"),   
    (-220,  60,  7, "gold"),          
    (-195,  45,  5, "gold"),          
    (-165,  55,  6, "lightyellow"),  
    (-155, 120,  6, "lightyellow"),   
    # Museau / naseaux
    (-250,  70,  5, "orange"),      
    (-255,  55,  4, "darkorange"),    
    # Œil
    (-195, 130,  4, "cyan"),          
    # Oreilles
    (-170, 175,  4, "lightyellow"),  
    (-160, 195,  3, "white"),         

    (-130, 110,  7, "lightyellow"),   
    (-100, 130,  6, "gold"),          
    ( -70, 140,  5, "gold"),          
    ( -40, 135,  4, "darkorange"),    
    (-120,  60,  6, "lightyellow"),   

    ( -50,  90,  8, "white"),        
    (  30,  80,  7, "lightyellow"),   
    ( 110,  70,  8, "white"),         
    ( 150,  50,  7, "gold"),          
    ( 170,  20,  6, "gold"),          
    ( -20,  30,  7, "lightyellow"),   
    (  20,  20,  6, "lightyellow"),   
    (  90,  10,  6, "gold"),          
    ( 140, -10,  5, "gold"),          

    ( 180,  30,  6, "orange"),       
    ( 210,  10,  5, "darkorange"),    
    ( 230, -20,  4, "darkorange"),   
    ( 220, -40,  3, "sienna"),       

    ( -60,  10,  6, "cyan"),          
    ( -80, -30,  5, "deepskyblue"), 
    ( -90, -75,  4, "deepskyblue"),   
    (-100,-115,  4, "lightcyan"),     
    (-105,-150,  3, "white"),        

    (  10,  15,  6, "cyan"),          
    (  -5, -25,  5, "deepskyblue"),   
    (  10, -60,  4, "deepskyblue"),
    (  20, -90,  3, "white"),    

    ( 100, -10,  6, "cyan"),          
    ( 120, -55,  5, "deepskyblue"), 
    ( 130,-100,  4, "deepskyblue"),  
    ( 135,-140,  3, "white"),       

    ( 145, -15,  6, "cyan"),         
    ( 160, -55,  5, "deepskyblue"),   
    ( 155, -95,  4, "deepskyblue"),   
    ( 150,-125,  3, "white"),         
]

lignes = [
    # Contour tête
    (0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 0),
    # Museau
    (2, 7), (7, 8), (8, 4),
    # Œil
    (0, 9), (9, 1),
    # Oreille
    (0, 10), (10, 11),
    # Tête → encolure
    (5, 12), (6, 12),
    # Encolure
    (12, 16), (12, 13), (13, 14), (14, 15),
    # Encolure → corps
    (16, 22), (12, 17),
    # Corps dessus
    (17, 18), (18, 19), (19, 20), (20, 21),
    # Corps dessous
    (22, 23), (23, 24), (24, 25),
    # Fermeture corps
    (17, 22), (21, 25),
    # Queue
    (20, 26), (26, 27), (27, 28), (28, 29),
    # Patte avant gauche
    (22, 30), (30, 31), (31, 32), (32, 33), (33, 34),
    # Patte avant droite
    (23, 35), (35, 36), (36, 37), (37, 38),
    # Patte arrière gauche
    (24, 39), (39, 40), (40, 41), (41, 42),
    # Patte arrière droite
    (25, 43), (43, 44), (44, 45), (45, 46),
]


def dessiner_fond():
    """Fond étoilé avec nébuleuse."""
    
    for _ in range(250):
        x = random.randint(-440, 440)
        y = random.randint(-310, 310)
        r = random.uniform(0.5, 1.8)
        niv = random.randint(140, 255)
        c = "#{:02x}{:02x}{:02x}".format(niv, niv, niv)
        bg.goto(x, y - r)
        bg.pendown()
        bg.fillcolor(c)
        bg.begin_fill()
        bg.circle(r)
        bg.end_fill()
        bg.penup()

    
    for _ in range(30):
        x = random.randint(-440, 440)
        y = random.randint(-310, 310)
        r = random.uniform(1.0, 2.5)
        bg.goto(x, y - r)
        bg.pendown()
        bg.fillcolor("gold")
        bg.begin_fill()
        bg.circle(r)
        bg.end_fill()
        bg.penup()


def dessiner_etoile(x, y, rayon, couleur):
    """Dessine une étoile brillante avec halo et rayons."""
    # Halo
    t.goto(x, y - rayon * 3.5)
    t.pendown()
    t.fillcolor("#0d0520")
    t.pencolor("#0d0520")
    t.begin_fill()
    t.circle(rayon * 3.5)
    t.end_fill()
    t.penup()

    t.goto(x, y - rayon)
    t.pendown()
    t.fillcolor(couleur)
    t.pencolor(couleur)
    t.begin_fill()
    t.circle(rayon)
    t.end_fill()
    t.penup()

    
    pr = max(1, rayon // 2)
    t.goto(x, y - pr)
    t.pendown()
    t.fillcolor("white")
    t.pencolor("white")
    t.begin_fill()
    t.circle(pr)
    t.end_fill()
    t.penup()


    if rayon >= 5:
        t.pensize(1)
        for angle in [0, 90, 45, 135]:
            longueur = rayon * 3
            t.goto(x, y)
            t.setheading(angle)
            t.pencolor("white")
            t.pendown()
            t.forward(longueur)
            t.penup()
            t.goto(x, y)
            t.setheading(angle + 180)
            t.pendown()
            t.forward(longueur)
            t.penup()


def dessiner_ligne(ia, ib, couleur="cyan", epaisseur=2):
    """Relie deux étoiles."""
    xa, ya = etoiles[ia][0], etoiles[ia][1]
    xb, yb = etoiles[ib][0], etoiles[ib][1]
    t.pencolor(couleur)
    t.pensize(epaisseur)
    t.goto(xa, ya)
    t.pendown()
    t.goto(xb, yb)
    t.penup()


def afficher_titres():
    t.pencolor("#c8aaff")
    t.goto(0, -295)
    t.write("✦  Constellation – Le Cheval  ✦",
            align="center", font=("Arial", 13, "italic"))
    t.goto(0, -312)
    t.pencolor("#7a6aaa")
    t.write(str(len(etoiles)) + " étoiles  •  " + str(len(lignes)) + " lignes",
            align="center", font=("Arial", 9, "normal"))



print("🌌 Dessin du fond étoilé...")
dessiner_fond()
screen.update()

print("🔗 Tracé des lignes de constellation...")
for ia, ib in lignes:
    dessiner_ligne(ia, ib, couleur="cyan", epaisseur=2)
    # Ligne de reflet plus fine
    dessiner_ligne(ia, ib, couleur="#aaddff", epaisseur=1)
    screen.update()

print("⭐ Dessin des étoiles...")
for x, y, rayon, couleur in etoiles:   
    dessiner_etoile(x, y, rayon, couleur)
    screen.update()

afficher_titres()
screen.update()

print(f"✓ Constellation terminée ! ({len(etoiles)} étoiles, {len(lignes)} lignes)")
turtle.done()