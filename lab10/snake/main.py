import pygame
import random
import datetime
import psycopg2
from config import *

from game_object import GameObject 
from worm import Worm
from food import Food
from wall import Wall

def create_background(screen, width, height):
        colors = [(255, 255, 255), (212, 212, 212)]
        tile_width = 20
        y = 0
        while y < height:
                x = 0
                while x < width:
                        row = y // tile_width
                        col = x // tile_width
                        pygame.draw.rect(screen, colors[(row + col) % 2],pygame.Rect(x, y, tile_width, tile_width))
                        x += tile_width
                y += tile_width

pygame.init()

def score(counter,white):
    text = font_for_score.render(f"Score: {counter}",True,white)
    text_rect = text.get_rect(center = (60,20))
    screen.blit(text,text_rect)

def level(lev,white):
    text = font_for_score.render(f"lv: {lev}",True,white)
    text_rect = text.get_rect(center = (50,45))
    screen.blit(text,text_rect)

def create_table():
    try:
     connection = psycopg2.connect(
        host = "localhost",
        user = "postgres",
        password = "20051337",
        database = "postgres"
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
        host = "localhost",
        user = "postgres",
        password = "20051337",
        database = "postgres"
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
        host = "localhost",
        user = "postgres",
        password = "20051337",
        database = "postgres"
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
is_Paused = False
paused_Surface = pygame.Surface((400, 300))
run = False

screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

# Score and level
speed = 5
SCORE = 0
LEVEL = 1

worm = Worm(20)
food = Food(20)
wall = Wall(20)


# create_table()

if player_name:
   run = True

font = pygame.font.SysFont('Times New Roman',70)
font_for_score = pygame.font.SysFont("Times New Roman",30)

counter = 0
white = (255, 255, 255)

while run:
        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                  if not is_Paused:
                     is_Paused = True
                  else:
                     try:
                        connection = psycopg2.connect(
                            host = "localhost",
                            user = "postgres",
                            password = "20051337",
                            database = "postgres"
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
                    
                     insert_score(player_name, counter)

                     paused_Surface.blit(screen, (0, 0))
                     is_Paused = False
            if event.type == pygame.QUIT:
                    run = False
            else:
                filtered_events.append(event)
        
        if is_Paused:
           screen.blit(paused_Surface, (0, 0))
           continue

        worm.process_input(filtered_events)
        worm.move()

        food.time_out()

        # check for wall collision
        pos = wall.can_hit(worm.points[0])
        if pos != None or worm.points[0].X < 0 or worm.points[0].X >= 400 or worm.points[0].Y < 0 or worm.points[0].Y >= 300:
              done = True
              break


        pos = food.can_eat(worm.points[0])
        if(pos != None):
            SCORE += food.weight
            worm.increase(pos)
            for i in range(food.weight - 1):
                pos.X += 1
                worm.increase(pos)

            counter += food.weight
            food.change_pos()
            
            if len(worm.points) > 5:
                wall.next_level()
                worm.next_level()
                speed += 5
                LEVEL = (LEVEL + 1) % 2

        create_background(screen, 400, 300)

        level(worm.level, white)
        score(counter, white)
        
        food.draw(screen)
        wall.draw(screen)
        worm.draw(screen)
        
        pygame.display.flip()
        clock.tick(speed)

pygame.quit()

# create_table() # It needed when I created table now it doesnt`t need because I only insert data`
insert_score(player_name,counter)
bd_levels(player_name, worm.level)