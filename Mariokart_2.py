'''
Created on May 24, 2018
@author: Luck
'''
#Importing libraries to use 
import pygame, sys, time, os,datetime,winsound
from random import randint
from pygame.locals import *
from pygame.constants import *
from __builtin__ import True
pygame.init()

#Setting fps clock to make game run at set fps and pygame.init allows for text to be displayed onscreen
fpsClock = pygame.time.Clock()
pygame.init()
pygame.mixer.init() #Allows for initialization of mixture module

#Setting variable definitions
select,rgb = 3,0
x,y,side,up,pic,count,ac = 600,300,7,7,0,0,2.0
cpuX,cpuY,cpuACC,dirr,turn = 600,100,0.0,0,0
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption ('Mario Kart!')
boundsA = [1160,19660,21160,1040,1200,-320]
boundsB = [20520,740,900,820,19120,-677,1900]
checkpoint = [False,False]
for i in range(0,len(boundsA)):
    boundsA[i]+=200
for i in range(0,len(boundsB)):
    boundsB[i]-=200

#Image definitions to set all images and music to be accessed in lists
Mario1 = pygame.image.load(os.path.join('D:\\Programming\\Files\\My Projects\\Mario Kart\\Mario','Mario1.png'))
Mario2 = pygame.image.load(os.path.join('D:\\Programming\\Files\\My Projects\\Mario Kart\\Mario','Mario2.png'))
Mario3 = pygame.image.load(os.path.join('D:\\Programming\\Files\\My Projects\\Mario Kart\\Mario','Mario3.png'))
Mario4 = pygame.image.load(os.path.join('D:\\Programming\\Files\\My Projects\\Mario Kart\\Mario','Mario4.png'))
Mario5 = pygame.image.load(os.path.join('D:\\Programming\\Files\\My Projects\\Mario Kart\\Mario','Mario5.png'))
Mario6 = pygame.image.load(os.path.join('D:\\Programming\\Files\\My Projects\\Mario Kart\\Mario','Mario6.png'))
Mario7 = pygame.image.load(os.path.join('D:\\Programming\\Files\\My Projects\\Mario Kart\\Mario','Mario7.png'))
Mario8 = pygame.image.load(os.path.join('D:\\Programming\\Files\\My Projects\\Mario Kart\\Mario','Mario8.png'))

Bowser1 = pygame.image.load(os.path.join('D:\\Programming\\Files\\My Projects\\Mario Kart\\Bowser','Bowser1.png'))
Bowser2 = pygame.image.load(os.path.join('D:\\Programming\\Files\\My Projects\\Mario Kart\\Bowser','Bowser2.png'))
Bowser3 = pygame.image.load(os.path.join('D:\\Programming\\Files\\My Projects\\Mario Kart\\Bowser','Bowser3.png'))
Bowser4 = pygame.image.load(os.path.join('D:\\Programming\\Files\\My Projects\\Mario Kart\\Bowser','Bowser4.png'))
Bowser5 = pygame.image.load(os.path.join('D:\\Programming\\Files\\My Projects\\Mario Kart\\Bowser','Bowser5.png'))
Bowser6 = pygame.image.load(os.path.join('D:\\Programming\\Files\\My Projects\\Mario Kart\\Bowser','Bowser6.png'))
Bowser7 = pygame.image.load(os.path.join('D:\\Programming\\Files\\My Projects\\Mario Kart\\Bowser','Bowser7.png'))
Bowser8 = pygame.image.load(os.path.join('D:\\Programming\\Files\\My Projects\\Mario Kart\\Bowser','Bowser8.png'))

R = pygame.image.load(os.path.join('D:\\Programming\\Files\\My Projects\\Mario Kart\\Arrow','RArrow.png'))
D = pygame.image.load(os.path.join('D:\\Programming\\Files\\My Projects\\Mario Kart\\Arrow','DArrow.png'))
L = pygame.image.load(os.path.join('D:\\Programming\\Files\\My Projects\\Mario Kart\\Arrow','LArrow.png'))
U = pygame.image.load(os.path.join('D:\\Programming\\Files\\My Projects\\Mario Kart\\Arrow','UArrow.png'))

Track1 = pygame.image.load(os.path.join('D:\\Programming\\Files\\My Projects\\Mario Kart\\Tracks','Track1.png'))
Track2 = pygame.image.load(os.path.join('D:\\Programming\\Files\\My Projects\\Mario Kart\\Tracks','Track2.png'))
Track3 = pygame.image.load(os.path.join('D:\\Programming\\Files\\My Projects\\Mario Kart\\Tracks','Track3.png'))
Track4 = pygame.image.load(os.path.join('D:\\Programming\\Files\\My Projects\\Mario Kart\\Tracks','Track4.png'))

menu_theme = ('D:\\Programming\\Files\\My Projects\\Mario Kart\\Music\\Menu.wav')
track1_theme = ('D:\\Programming\\Files\\My Projects\\Mario Kart\\Music\\Track1_Music.wav')
track2_theme = ('D:\\Programming\\Files\\My Projects\\Mario Kart\\Music\\Track2_Music.wav')
track3_theme = ('D:\\Programming\\Files\\My Projects\\Mario Kart\\Music\\Track3_Music.wav')
track4_theme = ('D:\\Programming\\Files\\My Projects\\Mario Kart\\Music\\Track4_Music.wav')
win_theme = ('D:\\Programming\\Files\\My Projects\\Mario Kart\\Music\\Win.wav')
lose_theme = ('D:\\Programming\\Files\\My Projects\\Mario Kart\\Music\\Lose.wav')

Mario = [Mario1,Mario2,Mario3,Mario4,Mario5,Mario6,Mario7,Mario8]
Bowser = [Bowser1,Bowser2,Bowser3,Bowser4,Bowser5,Bowser6,Bowser7,Bowser8]
char = [Mario,Bowser]
arrow = [R,D,L,U]
menu = [Track1,Track2,Track3,Track4]
music = [menu_theme,track1_theme,track2_theme,track3_theme,track4_theme,win_theme,lose_theme]

SFLine = pygame.image.load(os.path.join('D:\\Programming\\Files\\My Projects\\Mario Kart\\','Finish Line.png'))
SFLine = pygame.transform.scale(SFLine, (1500, 200))

#Functions
def instructions():
    '''instructions() gives player a rundown of the instructions in the game'''
    

def OutOfBounds(a,b,c,d,e,acc,r):
    '''OutOfBounds() detects collisions with boundaries of the track
    a - x coordinate of player
    b - y coordinate of player
    c - x factor vehicle travels by
    d - y factor vehicle travels by
    e - Direction of the vechile
    acc - Acceleration of the vehicle
    r - Radius of the hitbox'''
    dir_x = c*acc
    dir_y = d*acc
    
    if ((b+dir_y >= boundsB[0]-r or (b+dir_y >= boundsB[1]+r and b >= boundsB[1]+20 and b <= boundsB[2] and a > boundsA[0]-r and a < boundsA[1]+r)) and (e == 0 or e == 1 or e == 2)):
        b-=dir_y*2.5
        acc = 0.0
    elif e == 0: 
        b+=dir_y
    
    if ((a+dir_x >= boundsA[2]-r or (a+dir_x >= boundsA[3]+r and a >= boundsA[3]+20 and a <= boundsA[4] and b > boundsB[3]-r and b < boundsB[4]+r)) and (e == 2 or e == 5 or e == 7)):
        a-=dir_x*2.5
        acc = 0.0
    elif e == 2:
        a+=dir_x
        b+=dir_y
    elif e == 7:
        a+=dir_x
    
    if ((b-dir_y <= boundsB[5]+r or (b-dir_y <= boundsB[4]+10-r and b <= boundsB[4]-80+r and b > boundsB[6] and a > boundsA[0]-r and a < boundsA[1]+r)) and (e == 3 or e == 4 or e == 5)):
        b+=dir_y*2.5
        acc = 0.0
    elif e == 3: 
        b-=dir_y
    elif e == 5:
        a+=dir_x
        b-=dir_y
        
    if ((a-dir_x <= boundsA[5]+r or (a-dir_x <= boundsA[1]+110-r and a <= boundsA[1]+40+r and a > boundsA[1]+40 and b > boundsB[3]-r and b < boundsB[4]+r)) and (e == 1 or e == 4 or e == 6)):
        print True
        a+=dir_x*2.5
        acc = 0.0
    elif e == 1:
        a-=dir_x
        b+=dir_y
    elif e == 4:
        a-=dir_x
        b-=dir_y
    elif e == 6:
        a-=dir_x
    
    return [a,b,c,d,e,acc,r]
    

def drive(a,b,c,d,e,acc,r):
    '''drive(a,b,c,d,e) takes 7 parameters and returns values to make the character drive (also detects boundaries of track)
    a - The horizontal translation of the background (x)
    b - The vertical translation of the background (y)
    c - The x factor that the vehicle travels by (side)
    d - The y factor that the vehicle travels by (up)
    e - The character's direction
    acc - Acceleration of the vehicle
    r - Radius of the player's hitbox
    '''
    if pressed[pygame.K_w] or pressed[pygame.K_a] or pressed[pygame.K_s] or pressed[pygame.K_d]:
        if acc < 5.1:
            acc+=0.1
        if pressed[pygame.K_w]:
            e = 0
            if pressed[pygame.K_a] or pressed[pygame.K_d]:
                if pressed[pygame.K_a] and pressed[pygame.K_d]:
                    acc+=0.1
                elif pressed[pygame.K_a]:
                    e = 1
                elif pressed[pygame.K_d]:
                    e = 2
        elif pressed[pygame.K_s]:
            e = 3
            if pressed[pygame.K_a] and pressed[pygame.K_d]:
                    acc+=0.1
            elif pressed[pygame.K_a]:
                e = 4
            elif pressed[pygame.K_d]:
                e = 5
        elif pressed[pygame.K_a] or pressed[pygame.K_d]:
            if pressed[pygame.K_a] and pressed[pygame.K_d]:
                    pass
            elif pressed[pygame.K_a]:
                e = 6
            elif pressed[pygame.K_d]:
                e = 7
    else:  
        if acc <= 0.0:
            acc = 0.0
        else:
            acc-=0.1    
            
    move = OutOfBounds(a, b, c, d, e, acc, r)  
    a,b,c,d,e,acc = move[0],move[1],move[2],move[3],move[4],move[5]
    
    return [a,b,c,d,e,acc]

def CPU(a,b,c,d,t,r,lapped):
    '''CPU(a,b,c,d) controls CPU behaviors when driving
    a - x coordinate of CPU
    b - y coordinate of CPU
    c - Acceleration of CPU
    d - Direction of CPU
    t - Turn of the CPU
    r - Radius of the hitbox
    '''
    
    if c > 4:
        gamble = randint(1,2)
        if gamble == 1:
            c+=0.1
        else:
            c-=0.1
    elif c < 4:
        c+=0.08
    if c < 0:
        c = 0.0
    
    dir_x = 7*c
    dir_y = 7*c
    
    g1,g2,g3,g4 = (-19028),21000,0,500
    
    if t == 0:
        d = 0
        if b > g1:
            b-=dir_y
        else:
            t+=1
    elif t == 1:
        d = 7
        if a < g2:
            a+=dir_x
        else:
            t+=1
    elif t == 2:
        d = 3
        if b < g3:
            b+=dir_y
        else:
            t+=1
    elif t == 3:
        d = 6
        if a > g4:
            a-=dir_x
        else:
            t = 0
            lapped+=1
    
    return [a,b,c,d,t,lapped]

def boundaries(a,b):
    '''collision(a,b) sets appropriate boundaries for vehicle
    a - Represents the character chosen
    b - Represents direction of vehicle
    '''
    if a == 0:
        if b == 6 or b == 7:
            xc,yc = 640,510
        elif b == 1:
            xc,yc = 620,510
        elif b == 2:
            xc,yc = 635,510
        elif b == 5:
            xc,yc = 621,520
        else:
            xc,yc = 611,520
    else:
        if b == 6 or b == 7:
            xc,yc = 628,530
        elif b == 1:
            xc,yc = 615,525
        elif b == 2:
            xc,yc = 630,525
        elif b == 4 or b == 5:
            xc,yc = 621,530
        else:
            xc,yc = 619,525
    
    return [xc,yc]

def design(a):
    '''design(a) creates the rectangle patterns on the race track
    a - Represents the secondary colour of the track
    '''
    for z in range(0,20000,500):
        pygame.draw.rect (screen, (a),(300-x,1000+y-z,1500,200))
    for z in range(0,20000,500):
        pygame.draw.rect (screen, (a),(300-x+z,-20000+y,200,1500))
    for z in range(0,20000,500):
        pygame.draw.rect (screen, (a),(20300-x,-500+y-z,1500,200))
    for z in range(0,20000,500):
        pygame.draw.rect (screen, (a),(2000-x+z,-300+y,200,1500))
        
def arrows(a,b):
    '''arrows(a,b) displays an arrow on screen to indicates turn
    a - x coordinate of player
    b - y coordinate of player
    '''
    if a > 0 and a < 1450 and b > 19000 and b < 20000:
        screen.blit(arrow[0],(350,50))
    if a > 20000 and a < 22000 and b > 18000 and b < 20000:
        screen.blit(arrow[1],(350,50))
    if a > 20000 and a < 22000 and b > -750 and b < 930:
        screen.blit(arrow[2],(350,50))
    if a > 0 and a < 1600 and b > -750 and b < 620:
        screen.blit(arrow[3],(350,50))
        
def watch(a,b):
    '''watch(a,b) times the length of the race and converts it to text that can be output to the console
    a - The time elapsed from the start of the race
    b - The lap of the race
    '''
    font = pygame.font.SysFont("Comic Sans MS",20,bold = True,italic = False)
    swatch = "Time: "+str(a)
    LAP = "Lap: "+str(b)
    swatch = font.render(swatch, True,(0,0,0))
    screen.blit(swatch,(500,500))
    LAP = font.render(LAP, True,(0,0,0))
    screen.blit(LAP,(500,550))
    
def laps(a,b,c):
    '''laps(a,b,c,d) determines the laps that the player has taken
    a - x coordinate of the player
    b - y coordinate of the player
    c - the number of laps the player has taken
    '''
    reset = 0
    for i in range(0,2):
        if checkpoint[i] == True:
            reset+=1
    
    if reset == 2:
        for i in range(0,2):
            checkpoint[i] = False
        c+=1
    
    if a >= 18000 and a <= 22000 and b >= 18000 and b <= 22000:
        checkpoint[1] = True
    if a >= 0 and a <= 2000 and b >= 0 and b <= 1000 and checkpoint[1] == True:
        checkpoint[0] = True
        
    return c
    
#Game loop
while True:
    pygame.mixer.music.load(music[0])
    pygame.mixer.music.play(5)
    win,Total_time = 3,0
    while select != 2: #This loop breaks when selecting to play a game, so it allows you to read instructions and go back to the title screen
        done = False     
        while not done: #Printing out the main menu page
            pressed = pygame.key.get_pressed()
            typed = False
            
            screen.fill((128,138,135))
            
            if rgb == 0:
                col = 1
            if rgb == 255:
                col=-1
            rgb+=col
            title = "Mario Kart!"
            text = "Press \"1\" for instructions and \"2\" to play! (Press the \"Esc\" key to exit)"
            font = pygame.font.SysFont("Comic Sans MS",50,bold = False,italic = False)
            title = font.render(title, True,(rgb,rgb,rgb))
            screen.blit(title,(270,200))
            font = pygame.font.SysFont("Comic Sans MS",20,bold = False,italic = False)
            text = font.render(text, True,(0,0,0))
            screen.blit(text,(70,300))
                
            pygame.display.update()
                 
            fpsClock.tick(60)   
        
            for event in pygame.event.get():
                if (event.type == KEYUP) or (event.type == KEYDOWN):
                    print event
                    if (event.key == K_1):
                        done,select = True,1
                    elif (event.key == K_2):
                        done,select = True,2
                    elif (event.key == K_ESCAPE):
                        done = True
                        sys.exit()
                    else:
                        pass
        
        if select == 1: #Printing out instructions page
            choose = 10
            done = False
            while not done:
                a = "Welcome to \"Mario Kart!\", the high speed racing game with your favourite Nintendo characters!"
                b = "To drive, use the \"W\",\"A\",\"S\" and \"D\" keys."
                c = "To win the game, you must complete 3 laps around the track while beating the CPU."
                d = "Arrows will pop up around turns.  To increase acceleration past 10, hold a and d when driving up or down."
                e = "To return to menu, press \"BACKSPACE\"."
                
                screen.fill((128,138,135))
                font = pygame.font.SysFont("Comic Sans MS",15,bold = False,italic = False)
                a = font.render(a, True,(0,0,0))
                screen.blit(a,(10,100))
                b = font.render(b, True,(0,0,0))
                screen.blit(b,(10,150))
                c = font.render(c, True,(0,0,0))
                screen.blit(c,(10,200))
                d = font.render(d, True,(0,0,0))
                screen.blit(d,(10,250))
                e = font.render(e, True,(0,0,0))
                screen.blit(e,(10,300))
                pygame.display.update()
                
                for event in pygame.event.get():
                    if (event.type == KEYUP) or (event.type == KEYDOWN):
                        print event
                        if (event.key == K_BACKSPACE):
                            done = True               
        
        elif select == 2: #Printing out menu selections
            
            done,picture = False,0
            while not done:     
                
                a,b,c = "Choose your character:","Mario (Press A)","Bowser (Press B)"
                picnum = [0,1,6,4,3,5,7,2]
            
                screen.fill((128,138,135))
                font = pygame.font.SysFont("Comic Sans MS",15,bold = False,italic = False)
                a = font.render(a, True,(0,0,0))
                screen.blit(a,(10,100))
                b = font.render(b, True,(0,0,0))
                screen.blit(b,(100,500))
                c = font.render(c, True,(0,0,0))
                screen.blit(c,(500,500))
                screen.blit(char[0][picnum[picture]],(100,230))
                screen.blit(char[1][picnum[picture]],(500,200))
                pygame.display.update()  
                
                if picture < 7:
                    picture+=1
                elif picture == 7:
                    picture = 0
                time.sleep(0.1)
                
                for event in pygame.event.get():
                    if (event.type == KEYUP) or (event.type == KEYDOWN):
                        if (event.key == K_a):
                            done,choose = True,0
                            r,cpu,cpuR = 70,1,80
                        elif (event.key == K_b):
                            done,choose = True,1
                            r,cpu,cpuR = 80,0,70
            
            done = False
            while not done:#Second page of menu options   
                a,b,c,d,e = "Select a stage:","Mario Circuit","Peach Beach","Bowser Castle","Frosted Glacier"
                screen.fill((128,138,135))
                font = pygame.font.SysFont("Comic Sans MS",15,bold = False,italic = False)
                a = font.render(a, True,(0,0,0))
                screen.blit(a,(10,100))
                b = font.render(b, True,(0,0,0))
                screen.blit(b,(50,500))
                screen.blit(menu[0],(75,300))
                c = font.render(c, True,(0,0,0))
                screen.blit(c,(250,500))
                screen.blit(menu[1],(275,300))
                d = font.render(d, True,(0,0,0))
                screen.blit(d,(450,500))
                screen.blit(menu[2],(475,300))
                e = font.render(e, True,(0,0,0))
                screen.blit(e,(650,500))
                screen.blit(menu[3],(675,300))
                pygame.display.update()  
                
                for event in pygame.event.get():
                    if (event.type == KEYUP) or (event.type == KEYDOWN):
                        if (event.key == K_1):
                            colour1,colour2,colour3 = (113,238,0),(131,139,139),(193,205,205)
                            pygame.mixer.music.load(music[1])
                            pygame.mixer.music.play(5)
                            done = True
                        elif (event.key == K_2):
                            colour1,colour2,colour3 = (0,178,238),(255,228,196),(205,170,125)
                            pygame.mixer.music.load(music[2])
                            pygame.mixer.music.play(5)
                            done = True
                        elif (event.key == K_3):
                            colour1,colour2,colour3 = (255,127,0),(165,42,42),(139,35,35)
                            pygame.mixer.music.load(music[3])
                            pygame.mixer.music.play(5)
                            done = True
                        elif (event.key == K_4):
                            colour1,colour2,colour3 = (0,255,255),(248,248,255),(255,250,240)
                            pygame.mixer.music.load(music[4])
                            pygame.mixer.music.play(5)
                            done = True
    
    #Redefine key variables here because after code is run once, old variables are still saved so this refreshes them
    Time1,lap,cpuLap = datetime.datetime.now(),1,1
    select,rgb = 3,0
    x,y,side,up,pic,count,ac = 600,300,7,7,0,0,2.0
    cpuX,cpuY,cpuACC,dirr,turn = 600,100,0.0,0,0
    done = False
    while not done and lap < 4: #The game run loop, where the game runs within the entire program
        pressed = pygame.key.get_pressed()
        typed = False
        
        #Calling and redefining variables to create movement
        race = drive(x,y,side,up,pic,ac,r)
        Cpu = CPU(cpuX,cpuY,cpuACC,dirr,turn,cpuR,cpuLap)
        bounce = boundaries(choose,pic)
        
        x,y,side,up,pic,ac = race[0],race[1],race[2],race[3],race[4],race[5]
        cpuX,cpuY,cpuACC,dirr,turn,cpuLap = Cpu[0],Cpu[1],Cpu[2],Cpu[3],Cpu[4],Cpu[5]
        Char = char[choose][pic]
            
        #Printing out polygons and images based on the redefined variables
        pygame.draw.circle (screen, (255,255,255),(bounce[0],bounce[1]), r, 0)
        screen.fill(colour1)
        pygame.draw.rect (screen,(colour2),(300-x,-20000+y,1500,20000))
        pygame.draw.rect (screen, (colour2),(300-x,-20000+y,20000,1500))
        pygame.draw.rect (screen, (colour2),(20300-x,-20000+y,1500,20000))
        pygame.draw.rect (screen, (colour2),(300-x,-300+y,21500,1500))
        design(colour3)
        screen.blit(SFLine,(300-x,-300+y))
        screen.blit(Char,(350,270))
        screen.blit(char[cpu][dirr],(cpuX-x,cpuY+y))
        arrows(x,y)
        watch(datetime.datetime.now()-Time1,lap)
        lap=laps(x,y,lap)
        pygame.display.update()
        print cpuX,cpuY,cpuACC,cpuLap,"|",x,y,ac,checkpoint,lap
        
        if lap == 4: #Counter to check whether game requirements of four laps have been met
            if cpuLap >= 4:
                win = 0
            else:
                win = 1
            done = True
            Time2 = datetime.datetime.now()
            Total_time = str(Time2-Time1)
        for event in pygame.event.get():
            if (event.type == KEYUP) or (event.type == KEYDOWN):
                print event
                if (event.key == K_ESCAPE):
                    done = True
    
    if win == 1: #Win message (although most code repeats as lose message code, I must keep the variables within the loop or it doesn't work)
        pygame.mixer.music.load(music[5])
        pygame.mixer.music.play(5)
        done = False
        while not done:
            a,b,c = "You won!","Time: "+str(Total_time),"(Press \"END\" to return to the menu screen)"
        
            screen.fill((128,138,135))
            font = pygame.font.SysFont("Comic Sans MS",50,bold = True,italic = False)
            a = font.render(a, True,(0,201,87))
            screen.blit(a,(300,200))
            font = pygame.font.SysFont("Comic Sans MS",15,bold = False,italic = False)
            b = font.render(b, True,(0,0,0))
            screen.blit(b,(100,400))
            c = font.render(c, True,(0,0,0))
            screen.blit(c,(100,500))
            pygame.display.update() 
            
            for event in pygame.event.get():
                if (event.type == KEYUP) or (event.type == KEYDOWN):
                    if (event.key == K_END):
                        done = True
                        select = 0                       
    elif win == 0: #Lose message
        pygame.mixer.music.load(music[6])
        pygame.mixer.music.play(5)
        done = False
        while not done:
            a,b,c = "You lost!","Time: "+str(Total_time),"(Press \"END\" to return to the menu screen)"
        
            screen.fill((128,138,135))
            font = pygame.font.SysFont("Comic Sans MS",50,bold = True,italic = False)
            a = font.render(a, True,(255,48,48))
            screen.blit(a,(300,200))
            font = pygame.font.SysFont("Comic Sans MS",15,bold = False,italic = False)
            b = font.render(b, True,(0,0,0))
            screen.blit(b,(100,400))
            c = font.render(c, True,(0,0,0))
            screen.blit(c,(100,500))
            pygame.display.update() 
           
            for event in pygame.event.get():
                if (event.type == KEYUP) or (event.type == KEYDOWN):
                    if (event.key == K_END):
                        done = True
                        select = 0