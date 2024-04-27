import pygame
import random
import datetime
import psycopg2
from config import *

def game_over(red,w,h):
    text = font.render("Press space to play again",True, red) 
    text_rect = text.get_rect(center = (w//2,h//2))
    screen.blit(text,text_rect)

def score(counter,white):
    text = font_for_score.render(f"Score: {counter}",True,white)
    text_rect = text.get_rect(center = (60,20))
    screen.blit(text,text_rect)

def level(lev,white):
    text = font_for_score.render(f"lv: {lev}",True,white)
    text_rect = text.get_rect(center = (50,45))
    screen.blit(text,text_rect)

def pause_image():
   image = pygame.image.load("lab10/snake/pause.png")
   rectt_image = image.get_rect(center = (875,25))
   screen.blit(image,rectt_image)

def create_table():
    try:
     connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
    )
     connection.autocommit = True

     with connection.cursor() as cursor:
        cursor.execute(
            "CREATE TABLE Snake (User_name VARCHAR(64) NOT NULL, Score BIGINT NOT NULL);")
        print("[INFO] Table created!")

    except Exception as _ex:
     print("[INFO] Eror while working with PostgreSQL",_ex)

    finally:
     if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")

def insert_score(player_name,counter):
    try:
     connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database =db_name
    )
     connection.autocommit = True

     with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO snake (user_name, score) VALUES {};".format((player_name,counter)))
        print("[INFO] Inserted succesfully!")

    except Exception as _ex:
     print("[INFO] Eror while working with PostgreSQL",_ex)

    finally:
     if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")

def bd_levels(player_name,lev):
    try:
     connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database =db_name
    )
     connection.autocommit = True

     with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM snake WHERE user_name = '{}';".format(player_name))
        forvalue = []
        for x in cursor.fetchall():
           forvalue.append(x[1])
        print("Max level of this player:", max(forvalue) // 5)
        print("Current level of this player:", lev)

    except Exception as _ex:
     print("[INFO] Eror while working with PostgreSQL",_ex)

    finally:
     if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
   


player_name = input()
process = False
run = False

if player_name:
   process = True

# process = True
if process:   
    w, h = 900,700
    pygame.init()
    screen = pygame.display.set_mode((w,h))
    pygame.display.set_caption("Snake")
    run = True
    white = (255,255,255)
    black = (0,0,0)
    green = (0,255,0)
    red = (255,0,0)
    x,y = w//2,h//2
    pos = (x,y,50,50)
    z,t = random.choice(range(1,800)),random.choice(range(1,600))

    font = pygame.font.SysFont('Times New Roman',70)
    font_for_score = pygame.font.SysFont("Times New Roman",30)

    apple = pygame.image.load("lab10/snake/apple.png")
    apple_rect = apple.get_rect(center = (z,t))

    apple_green = pygame.image.load("lab10/snake/green_apple.png")
    green_rect = apple_green.get_rect(center = (z,t))

    apple_yellow = pygame.image.load("lab10/snake/yellow_apple.png")
    yellow_rect = apple_yellow.get_rect(center = (z,t))

    flag_left = False
    flag_right = False
    flag_up = False
    flag_down = False
    game = True
    clock = pygame.time.Clock()
    fps = 20
    once = True
    counter = 0
    lev = 0
    length = False
    g,a = 50,50
    q = 10
    segments = [pos]
    press_r = True #эти флаги нужны чтобы не двигаться в обратном направление если движется вправо то нажать на лево нельзя
    press_up = True
    press_down = True
    press_l = True
    flag = False
    number = 1 #служит для смены яблока
    seconds = datetime.timedelta(seconds = 10)
    current_time = datetime.datetime.now()
    current_seconds = current_time.second
    change_cord_apple = False
    pause = False
    there = False
    only_once = True
    

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                counter = 0
                lev = 0
                q = 10
                game = True
                x,y = w//2,h//2
                pos = (x,y,50,50)
                segments.clear()
                press_r = True
                press_l = True
                press_down = True
                press_up = True
                
            if event.key == pygame.K_LEFT and press_l:
                if game:
                   flag_left = True
                   flag_right = False
                   flag_up = False
                   flag_down = False
                
            elif event.key == pygame.K_RIGHT and press_r:
                if game:
                   flag_left = False
                   flag_right = True
                   flag_up = False
                   flag_down = False
                
            elif event.key == pygame.K_UP and press_up:   
                if game:
                   flag_left = False
                   flag_right = False
                   flag_up = True
                   flag_down = False
                   
            elif event.key == pygame.K_DOWN and press_down:
                if game:
                   flag_left = False
                   flag_right = False
                   flag_up = False
                   flag_down = True

        elif event.type == pygame.MOUSEBUTTONDOWN and game == True:
            if there:
               pause = not pause
               only_once = True
           
        elif event.type == pygame.MOUSEMOTION:
           dx,dy = event.pos
           if dx <= w - 15 and dx >= w - 30 and dy >= 0 and dy <= 50:
              there = True
           else:
              there = False
           
                
    screen.fill(black)
    score(counter,white)
    level(lev,white)
    pause_image()

    mouse = pygame.mouse.get_pressed()
    if mouse[0] == 0:
       if pause:
        flag_left = False
        flag_right = False
        flag_up = False
        flag_down = False
        press_r = True
        press_l = True
        press_down = True
        press_up = True
        text_1 = font.render(f"Pause",True,white)
        text_rect_1 = text_1.get_rect(center = (w//2,h//2))
        screen.blit(text_1,text_rect_1)
        if only_once:
          try:
            connection = psycopg2.connect(
                host = host,
                user = user,
                password = password,
                database =db_name
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
              cursor.execute(
                "INSERT INTO snake (user_name, score) VALUES {};".format((player_name + '(ON PAUSE)',counter)))
              print("[INFO] Inserted succesfully!")

          except Exception as _ex:
            print("[INFO] Eror while working with PostgreSQL",_ex)

          finally:
            if connection:
              connection.close()
              print("[INFO] PostgreSQL connection closed")
        only_once = False


          
    if current_time + datetime.timedelta(seconds = 5) <= datetime.datetime.now():
        if game:
           change_cord_apple = True
        

    if once: #once нужен для того чтобы шарик рисовался в одном месте пока змейка не соприкоснется с ним
        apple_rect = apple.get_rect(center = (z,t))
        green_rect = apple_green.get_rect(center = (z,t))
        yellow_rect = apple_yellow.get_rect(center = (z,t))
        if number == 1:
           screen.blit(apple,apple_rect)
        elif number == 2:
            screen.blit(apple_green,green_rect)
        elif number == 3:
            screen.blit(apple_yellow,yellow_rect)

    
    if abs(x - z) <= 60 and abs(y - t) <= 62:
        counter += 1
        if counter % 5 == 0:
           lev += 1
           flag = True
        once = False
        if number == 2:
            q += 0.5 #если съел зеленое яблоко то скорость увеличивается на 0.5 и размер на 0.5 станет больше
        elif number == 3:
            q += 1
        change_cord_apple = True
        
    else:
        once = True
        if len(segments) != 0:# из за того что очищаю список когда нажимаю на пробел пришлось сделать это условие когда только есть элементы в списке только тогда удалять
           segments.pop(0)


    if change_cord_apple:
        r,i = z,t
        z,t = random.choice(range(50,840)),random.choice(range(50,640))
        number = random.choice(range(1,4))
        if (r == z and i == t) or (z == x and t == y): #меняем координаты заново если шарик создался на змейке или на том же месте где только что съели
           z,t = random.choice(range(1,800)),random.choice(range(1,600))
           apple_rect = apple.get_rect(center = (z,t))
           screen.blit(apple,apple_rect)
        current_time = datetime.datetime.now()
        current_seconds = current_time.second
        change_cord_apple = False

        
    if game == False: #означает змейка дошла границ экрана и отображается текст, в случаи нажатии кнопки пробел game станет true a это значит дальше не будет рисоваться текст а оставшийся текст закрасит черный цвет
       game_over(white,w,h)
       flag_left = False
       flag_right = False
       flag_up = False
       flag_down = False

    if flag_left:
       if x <= 7:
          game = False
          continue
       press_r = False
       press_up = True
       press_down = True
       if counter % 5 == 0 and counter != 0 and flag:
           q += 1
       flag = False
       x -= q
       pos = (x,y,g,a)
    elif flag_right:
        if x >= w - 50:
           game = False
           continue
        press_l = False
        press_up = True
        press_down = True
        if counter % 5 == 0 and counter != 0 and flag:
           q += 1
        flag = False
        x += q
        pos = (x,y,g,a)
    elif flag_up:
        if y <= 7:
           game = False
           continue
        press_r = True
        press_l = True
        press_down = False
        if counter % 5 == 0 and counter != 0 and flag:
           q += 1
        flag = False
        y -= q
        pos = (x,y,g,a)
    elif flag_down:
        if y >= h - 50:
           game = False
           continue
        press_r = True
        press_up = False
        press_l = True
        if counter % 5 == 0 and counter != 0 and flag:
           q += 1
        flag = False
        y += q
        pos = (x, y, g,a)
    
    segments.append(pos)
    if pause == False and pos != segments[len(segments) - 1]:
     for k in range(1, len(segments)):
        if segments[0] == segments[k]:
           game = False
           break
    for segment in segments:
        pygame.draw.rect(screen, green, (segment[0],segment[1], g, a))
        pygame.draw.rect(screen,black,(segment[0],segment[1],g,a),1)
    
   

    pygame.display.flip()
    clock.tick(fps)
    
pygame.quit()
            
"""При новым достижение уровня змейка движется на 1 пиксель больше тоесть начинает ускорятся"""

# create_table() # It needed when I created table now it doesnt`t need because I only insert data`
insert_score(player_name,counter)
bd_levels(player_name,lev)






