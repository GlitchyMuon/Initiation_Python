import pgzrun

# --- variables globales 

WIDTH = 800
HEIGHT = 600
ROWS = 7

# *** bricks ***
bricks = []

for y in range(0, ROWS*30, 30):

    for x in range(0, WIDTH, 100):
        brick = Actor("brick", anchor=["left","top"]) # d'abord left, center or right, puis top, center or bottom
    #important d'écrire l'orthographe correct de l'image qu'on appelle
        brick.pos = [x, y]  # pos=position, par rapport au milieu de l'objet, en [0, 0], on vient la moitié
        bricks.append(brick)

# *** player ***

player = Actor("player")
player.pos = [WIDTH/2, HEIGHT - 50] # HEIGHT-50 comme ça la raquette sera tjs en bas de l'écran

# *** ball ***

ball = Actor("ball")
ball.pos = [WIDTH/2, HEIGHT - 100]
ball_speed = [240, -240] # 30 pixel par seconde



# --- fonctions

def draw():
    screen.clear()
    for brick in bricks:
        brick.draw() # déssin de la brique, comme return sinon on ne voit rien
    
    player.draw()
    ball.draw()
    
def update(dt): #dt = temps         # quand on bouge un objet, mouvement de souris, vérifier des collisions, calculs. Fonction jouée à chaque frame
    if dt > 0.5 : # dès qu'il y a une frame plus grande qu'une demiseconde, elle n'est plus considérée. (workaround)
        return
    pos = ball.pos
    mvt = [ball_speed[0] * dt, ball_speed[1] * dt]
    # ou : mvt_x = ball_speed[0] * dt
    #      mvt_y = ball_speed[1] * dt
    pos = [pos[0] + mvt[0], pos[1] + mvt[1]]
    # ou position = [pos[0] + mvt_x, pos[1] + mvt_y]
    
    # cap : garde/restreint la balle toujours dans le cadre de l'écran
    if pos[0] > WIDTH -10:
        pos[0] = WIDTH -10
    elif pos[0] < 10:
        pos[0] = 10
        
    if pos[1] > WIDTH -10:
        pos[1] = WIDTH -10
    elif pos[1] < 10:
        pos[1] = 10
        
    ball.pos = pos # on est obligé de la redéfinir pour qu'elle le recalcule
    
    # *** collision with screen ***
    if ball.pos[0] >= WIDTH -10:    # dimension ball = 20       # WIDTH car horizontal 
        invert_horizontal_speed()
    elif ball.pos[0] <= 10 :
        invert_horizontal_speed()
        
    if ball.pos[1] <= 10:
        invert_vertical_speed()
    elif ball.pos[1] >= HEIGHT -10: # hauteur car vertical
        invert_vertical_speed()
    
    
    # *** collision with player ***
    if ball.colliderect(player):
        invert_vertical_speed()
        
    # *** collision with bricks ***
    
    for brick in bricks:
        if ball.colliderect(brick):
            invert_vertical_speed()
            bricks.remove(brick)
            break

        
    

def on_mouse_move(pos):
    if pos[0] > 75 and pos[0] < WIDTH - 75: # largeur de player = 150
        x = pos[0]
    elif pos[0] <= 75:
        x = 75
    else:
        x = WIDTH - 75
    
    y = player.pos[1] # 1 c'est la deuxième position, on redonne la position actuelle player
    player.pos = [x, y]

def invert_horizontal_speed():
    ball_speed[0] *= -1

def invert_vertical_speed():
    ball_speed[1] *= -1
   
#def on_key_down(key):
#   if key == keys.SPACE:
#            invert_horizontal_speed()
    
# --- programme principal 

    

pgzrun.go() 
#mettre le pgzrun.go() toujours à la fin car comme ça, il lit les instructions Avant de le lancer