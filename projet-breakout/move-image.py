import pgzrun
import random

WIDTH = 800
HEIGHT = 600
ROTATION_SPEED = 60

score = 0

# *** player ***

target = Actor("zombie_talk", anchor=['center', 'center'])
target.pos = [WIDTH/2, HEIGHT/2]


#*** functions ***

def draw():
    screen.clear()
    target.draw()

    screen.draw.text("Tu m'as touché " + str(score) + " fois. Mais je suis immortel !", (10, 15), color=(255,255,255), fontsize=30)

def update(dt):

    target.angle += ROTATION_SPEED * dt
    
    if dt > 0.5 :
        return
    
    pos = target.pos
    if pos[0] > WIDTH -10:
        pos[0] = WIDTH -10
    elif pos[0] < 10:
        pos[0] = 10
        
    if pos[1] > WIDTH -10:
        pos[1] = WIDTH -10
    elif pos[1] < 10:
        pos[1] = 10
     

def random_pos():
    image_width = images.zombie_talk.get_width()
    image_heigth = images.zombie_talk.get_height()
    modifier = max(image_width, image_heigth) / 2
    x = random.randint(modifier, WIDTH - modifier)
    y = random.randint(modifier, HEIGHT - modifier)
    target.pos = [x, y]

def on_mouse_down(pos, button): # ne PAS oublier l'argument 'button'
    global score # mettre ici, pas dans l'update sinon fonctionne pas. UnboundLocalError: local variable 'score' referenced before assignment
    # In Python, we can read variables that are outside a function (...these are called global variables), but cannot write to them unless we declare them as global inside the function.

    if button == mouse.LEFT and target.collidepoint(pos):
        print("Eek!")
        random_pos()
        set_target_hurt()
        score += 1

def set_target_hurt():
    target.image = 'zombie_hurt'
    sounds.eep.play()   # il faut absolument que le fichier soit en un mot sans symboles '-' ni '_'
    clock.schedule_unique(set_target_normal, 1.0)

def set_target_normal():
    target.image = 'zombie_talk'



pgzrun.go()
