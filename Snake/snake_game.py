import pygame
import random
import os
import time
import pickle 
import sys
# from snake_class import Snake 

file_path1 = '/Users/apple/Snake-Game/Snake/snake1.pickle'
file_path2 = '/Users/apple/Snake-Game/Snake/snake2.pickle'
file_path3 = '/Users/apple/Snake-Game/Snake/snake3.pickle'

start_noise = '/Users/apple/Snake-Game/Snake/Assets/start noise1.wav'


elapsed_time = 0
count = 0
homescreen = True
game_loaded = False
FONT = "/Users/apple/Snake-Game/Snake/Assets/8Bit.ttf"
pygame.mixer.init()
pygame.font.init()


y1 = 0
y2 = 0
y3 = 0

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GOLD = (255, 215,0)
TRANSPARENT = (255, 255, 255, 0)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 30
HEIGHT = 30

# This sets the margin between each cell
MARGIN = 3


def home_screen():   
    while True:
        pygame.mixer.music.load('/Users/apple/Snake-Game/Snake/Assets/snake music.wav')
        pygame.mixer.music.play(-1)
        global homescreen 
        home_screen_surface = pygame.Surface((1000, 1000))
        pygame.draw.rect(gameDisplay, BLACK, (500, 500, 500, 500), 0)
        background = pygame.image.load('/Users/apple/Snake-Game/Snake/Assets/main_screen2.png')
        button_hover = pygame.image.load('/Users/apple/Snake-Game/Snake/Assets/button_hover.png').convert_alpha()
        button_hover_long = pygame.image.load('/Users/apple/Snake-Game/Snake/Assets/button_hover_long_screen.png').convert_alpha()
        button_background = pygame.image.load('/Users/apple/Snake-Game/Snake/Assets/button_background_background.png')
        game_text = font2.render("SNAKE", True, WHITE)
        start_button = font.render("New Game", True, WHITE)
        load_button = font.render("Load Game", True, WHITE)
        token_shop = font.render("Token Shop", True, WHITE)
        game_info = font.render("Game Info", True, WHITE)

        home_screen_surface.blit(button_background, [0,-35])
        home_screen_surface.blit(background, [0,-35])
        home_screen_surface.blit(game_text, [305, 25])
        home_screen_surface.blit(start_button, [420, 240])
        home_screen_surface.blit(load_button, [415, 380])
        home_screen_surface.blit(token_shop, [405, 520])
        home_screen_surface.blit(game_info, [415, 660])
        
        gameDisplay.blit(home_screen_surface, (0, 0))
        pygame.display.update()
        load_game_bool = True
        is_hovering = False

        while load_game_bool:
            mouse = pygame.mouse.get_pos()
            event = pygame.event.wait()
            if 340 + 300 > mouse[0] > 340 and 225 + 80 > mouse[1] > 225:
                if not is_hovering:
                    is_hovering = True
                    gameDisplay.blit(button_hover, (340, 222))
                    gameDisplay.blit(start_button, [420, 240])
                    pygame.display.update()
            elif 340 + 300 > mouse[0] > 340 and 362 + 80 > mouse[1] > 362:
                if not is_hovering:
                    is_hovering = True
                    gameDisplay.blit(button_hover, (340, 362))
                    gameDisplay.blit(load_button, [415, 380])
                    pygame.display.update()
            elif 340 + 300 > mouse[0] > 340 and 500 + 80 > mouse[1] > 500:
                if not is_hovering:
                    is_hovering = True
                    gameDisplay.blit(button_hover, (340, 500))
                    gameDisplay.blit(token_shop, [405, 520])
                    pygame.display.update()
            elif 340 + 300 > mouse[0] > 340 and 640 + 80 > mouse[1] > 640:
                if not is_hovering:
                    is_hovering = True
                    gameDisplay.blit(button_hover, (340, 640))
                    gameDisplay.blit(game_info, [415, 660])
                    pygame.display.update()                             
            else:
                if is_hovering:
                    is_hovering = False
                    gameDisplay.blit(home_screen_surface, (0, 0)) # clear the screen
                    pygame.display.update()            
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if 340 + 300 > mouse[0] > 340 and 225 + 80 > mouse[1] > 225: #START GAME
                    pygame.mixer.music.load(start_noise)
                    pygame.mixer.music.play(0)
                    homescreen = False
                    return
                if 340 + 300 > mouse[0] > 340 and 362 + 80 > mouse[1] > 362: #LOAD GAME

                    pause_background = pygame.image.load('/Users/apple/Snake-Game/Snake/Assets/pause screen long.png')
                    sub_screen = pygame.Surface((1000,1000))
                    sub_screen.fill(BLACK)
                    gameDisplay.blit(sub_screen, (0, 0))
                    gameDisplay.blit(button_background, [0,-35])
                    gameDisplay.blit(background, [0,-35])
                    gameDisplay.blit(game_text, [305, 25])
                    gameDisplay.blit(start_button, [420, 240])
                    gameDisplay.blit(pause_background, [0, 25])

                    with open(file_path1, "rb") as file:
                        data = pickle.load(file)
                    save_file1_tokens = font3.render(f'tokens: {data[0].tokens}', True, (255, 255, 255)) 
                    save_file1_score = font3.render(f'score: {data[3]}', True, (255, 255, 255))
                    save_file1_saves = font3.render(f'saves left: {data[9]}', True, (255, 255, 255))

                    with open(file_path2, "rb") as file:
                        data = pickle.load(file)
                    save_file2_tokens = font3.render(f'tokens: {data[0].tokens}', True, (255, 255, 255)) 
                    save_file2_score = font3.render(f'score: {data[3]}', True, (255, 255, 255))
                    save_file2_saves = font3.render(f'saves left: {data[9]}', True, (255, 255, 255))

                    with open(file_path3, "rb") as file:
                        data = pickle.load(file)
                    save_file3_tokens = font3.render(f'tokens: {data[0].tokens}', True, (255, 255, 255)) 
                    save_file3_score = font3.render(f'score: {data[3]}', True, (255, 255, 255))
                    save_file3_saves = font3.render(f'saves left: {data[9]}', True, (255, 255, 255))

                    render_saves(save_file1_tokens,
                                save_file1_score,
                                save_file1_saves,
                                save_file2_tokens,
                                save_file2_score,
                                save_file2_saves,
                                save_file3_tokens,
                                save_file3_score,
                                save_file3_saves)

                    pygame.mixer.music.load(start_noise)
                    pygame.mixer.music.play(0)
                    pygame.display.update()
                


                    pause = True
                    file_path = None
                    is_hovering = False

                    while pause:
                        mouse = pygame.mouse.get_pos()
                        if 360 + 260 > mouse[0] > 360 and 285 + 120 > mouse[1] > 285:
                            if not is_hovering:
                                is_hovering = True
                                gameDisplay.blit(pause_background, [0, 25])
                                gameDisplay.blit(button_hover_long, (360, 275))
                                render_saves(save_file1_tokens,
                                save_file1_score,
                                save_file1_saves,
                                save_file2_tokens,
                                save_file2_score,
                                save_file2_saves,
                                save_file3_tokens,
                                save_file3_score,
                                save_file3_saves)
                                pygame.display.update()
                        elif 360 + 260 > mouse[0] > 360 and 425 + 120 > mouse[1] > 425:
                            if not is_hovering:
                                is_hovering = True
                                gameDisplay.blit(pause_background, [0, 25])
                                gameDisplay.blit(button_hover_long, (360, 415))
                                render_saves(save_file1_tokens,
                                save_file1_score,
                                save_file1_saves,
                                save_file2_tokens,
                                save_file2_score,
                                save_file2_saves,
                                save_file3_tokens,
                                save_file3_score,
                                save_file3_saves)
                                pygame.display.update()
                        elif 360 + 260 > mouse[0] > 360 and 575 + 120 > mouse[1] > 575:
                            if not is_hovering:
                                is_hovering = True
                                gameDisplay.blit(pause_background, [0, 25])
                                gameDisplay.blit(button_hover_long, (360, 565))
                                render_saves(save_file1_tokens,
                                save_file1_score,
                                save_file1_saves,
                                save_file2_tokens,
                                save_file2_score,
                                save_file2_saves,
                                save_file3_tokens,
                                save_file3_score,
                                save_file3_saves)
                                pygame.display.update()                         
                        else:
                            if is_hovering:
                                is_hovering = False
                                render_saves(save_file1_tokens,
                                save_file1_score,
                                save_file1_saves,
                                save_file2_tokens,
                                save_file2_score,
                                save_file2_saves,
                                save_file3_tokens,
                                save_file3_score,
                                save_file3_saves)
                                pygame.display.update()  
                        for event in pygame.event.get():
                            mouse = pygame.mouse.get_pos()
                            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                                if 360 + 260 > mouse[0] > 360 and 285 + 120 > mouse[1] > 285: #FILE 1
                                    pygame.mixer.music.load(start_noise)
                                    pygame.mixer.music.play(0)
                                    homescreen = False
                                    global game_loaded
                                    game_loaded = True
                                    file_path = file_path1
                                    return file_path
                                elif 360 + 260 > mouse[0] > 360 and 425 + 120 > mouse[1] > 425: #File 2
                                    pygame.mixer.music.load(start_noise)
                                    pygame.mixer.music.play(0)
                                    homescreen = False
                                    game_loaded = True                                
                                    file_path = file_path2
                                    return file_path
                                elif 360 + 260 > mouse[0] > 360 and 575 + 120 > mouse[1] > 575: #FILE 3
                                    pygame.mixer.music.load(start_noise)
                                    pygame.mixer.music.play(0)
                                    homescreen = False
                                    game_loaded = True                               
                                    file_path = file_path3
                                    return file_path
                            if (event.type == pygame.KEYDOWN and event.key == pygame.K_TAB and not is_hovering):
                                pause = False
                                load_game_bool = False


def pause_screen(saves_left):

    home = False

    pygame.mixer.music.load('/Users/apple/Snake-Game/Snake/Assets/snake pause.wav')
    pygame.mixer.music.play(0)

    button_hover_long = pygame.image.load('/Users/apple/Snake-Game/Snake/Assets/button_hover_long_screen.png').convert_alpha()
    save_hover = pygame.image.load('/Users/apple/Snake-Game/Snake/Assets/save_hover.png').convert_alpha()
    exit_hover = pygame.image.load('/Users/apple/Snake-Game/Snake/Assets/exit_hover.png').convert_alpha()
    pause_background = pygame.image.load('/Users/apple/Snake-Game/Snake/Assets/pause screen.png')
    sub_screen = pygame.Surface((395, 395))
    sub_screen.fill(BLACK)
    gameDisplay.blit(sub_screen, [310, 310])
    gameDisplay.blit(pause_background, [0, -35])

    font = pygame.font.Font(FONT, 35)
    speed = font.render(f'Speed:     {framerate}', True, WHITE)
    links = font.render(f'Links:     {len(snake.body)}', True, WHITE)
    multiplier_text = font.render(f'Multiplier:     {multiplier} x', True, WHITE)
    save_text = font.render(f'Save Game', True, WHITE)
    home_text = font.render(f'Exit to Home', True, WHITE)
    gameDisplay.blit(speed, (430,365))
    gameDisplay.blit(links, (440,440))
    gameDisplay.blit(multiplier_text, (410,515))
    gameDisplay.blit(save_text, (430,590))
    gameDisplay.blit(home_text, (420,870))
    pygame.display.update()



    pause = True
    is_hovering = False

    while pause:
        mouse = pygame.mouse.get_pos()
        if 380 + 250 > mouse[0] > 380 and 860 + 60 > mouse[1] > 860: # BACK HOME HOVER
            if not is_hovering:
                is_hovering = True
                gameDisplay.blit(exit_hover, (400, 815))
                gameDisplay.blit(home_text, (420,870))
                pygame.display.update()
        elif 410 + 160 > mouse[0] > 410 and 580 + 60 > mouse[1] > 580:
            if not is_hovering:
                is_hovering = True
                gameDisplay.blit(save_hover, (410, 577))
                gameDisplay.blit(save_text, (430,590))
                pygame.display.update()
        else:
            if is_hovering:
                is_hovering = False
                sub_screen = pygame.Surface((395, 395))
                sub_screen.fill(BLACK)
                gameDisplay.blit(sub_screen, [310, 310])
                gameDisplay.blit(pause_background, [0, -35])
                gameDisplay.blit(speed, (430,365))
                gameDisplay.blit(links, (440,440))
                gameDisplay.blit(multiplier_text, (410,515))
                gameDisplay.blit(save_text, (430,590))
                pygame.draw.rect(gameDisplay, BLACK, (320, 870, 600, 200), 0)
                gameDisplay.blit(home_text, (420,870))
                pygame.display.update()
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if 380 + 250 > mouse[0] > 380 and 860 + 60 > mouse[1] > 860: #GO BACK HOME
                    home = True
                    pause = False
                if 410 + 160 > mouse[0] > 410 and 580 + 60 > mouse[1] > 580: #SAVE GAME
                    pause_background = pygame.image.load('/Users/apple/Snake-Game/Snake/Assets/pause screen long.png')
                    sub_screen = pygame.Surface((395, 395))
                    sub_screen.fill(BLACK)
                    gameDisplay.blit(sub_screen, [310, 310])
                    gameDisplay.blit(pause_background, [-7, 45])

                    render_saves(save_file1_tokens,
                                save_file1_score,
                                save_file1_saves,
                                save_file2_tokens,
                                save_file2_score,
                                save_file2_saves,
                                save_file3_tokens,
                                save_file3_score,
                                save_file3_saves)
                    
                    pygame.mixer.music.play(0)

                    save_pause = True
                    is_hovering = False

                    while save_pause: # SAVE GAME LOOP
                        mouse = pygame.mouse.get_pos()
                        if 380 + 250 > mouse[0] > 380 and 860 + 60 > mouse[1] > 860: #BACK HOME HOVER WHEN SAVING GAME
                            if not is_hovering:
                                is_hovering = True
                                gameDisplay.blit(exit_hover, (400, 815))
                                gameDisplay.blit(home_text, (420,870))
                                pygame.display.update()
                        elif 360 + 260 > mouse[0] > 360 and 285 + 120 > mouse[1] > 285:
                            if not is_hovering:
                                is_hovering = True
                                gameDisplay.blit(button_hover_long, (360, 275))
                                render_saves(save_file1_tokens,
                                save_file1_score,
                                save_file1_saves,
                                save_file2_tokens,
                                save_file2_score,
                                save_file2_saves,
                                save_file3_tokens,
                                save_file3_score,
                                save_file3_saves)
                                pygame.display.update()
                        elif 360 + 260 > mouse[0] > 360 and 425 + 120 > mouse[1] > 425:
                            if not is_hovering:
                                is_hovering = True
                                gameDisplay.blit(button_hover_long, (360, 415))
                                render_saves(save_file1_tokens,
                                save_file1_score,
                                save_file1_saves,
                                save_file2_tokens,
                                save_file2_score,
                                save_file2_saves,
                                save_file3_tokens,
                                save_file3_score,
                                save_file3_saves)
                                pygame.display.update()
                        elif 360 + 260 > mouse[0] > 360 and 575 + 120 > mouse[1] > 575:
                            if not is_hovering:
                                is_hovering = True
                                gameDisplay.blit(button_hover_long, (360, 565))
                                render_saves(save_file1_tokens,
                                save_file1_score,
                                save_file1_saves,
                                save_file2_tokens,
                                save_file2_score,
                                save_file2_saves,
                                save_file3_tokens,
                                save_file3_score,
                                save_file3_saves)
                                pygame.display.update()                         
                        else:
                            if is_hovering:
                                is_hovering = False                    
                                sub_screen = pygame.Surface((395, 395))
                                sub_screen.fill(BLACK)
                                gameDisplay.blit(sub_screen, [310, 310])
                                gameDisplay.blit(pause_background, [-7, 45])
                                pygame.draw.rect(gameDisplay, BLACK, (320, 870, 600, 200), 0)
                                gameDisplay.blit(home_text, (420,870))
                                render_saves(save_file1_tokens,
                                save_file1_score,
                                save_file1_saves,
                                save_file2_tokens,
                                save_file2_score,
                                save_file2_saves,
                                save_file3_tokens,
                                save_file3_score,
                                save_file3_saves)
                                pygame.display.update()   
                        for event in pygame.event.get():
                            mouse = pygame.mouse.get_pos()
                            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                                if 380 + 250 > mouse[0] > 380 and 860 + 60 > mouse[1] > 860: #GO BACK HOME
                                    pygame.mixer.music.play(0)
                                    home = True
                                    save_pause = False
                                    pause = False
                                if 360 + 260 > mouse[0] > 360 and 285 + 120 > mouse[1] > 285 and saves_left > 0: #Save File 1
                                    pygame.mixer.music.play(0)
                                    saves_left -= 1
                                    save_game(file_path1, snake, framerate, multiplier, food_counter, score, elapsed_time, food_pos, token_pos, body_count, saves_left, display_bool, pause_sound_played)
                                    break
                                elif 360 + 260 > mouse[0] > 360 and 425 + 120 > mouse[1] > 425 and saves_left > 0: #Save File 2
                                    pygame.mixer.music.play(0)
                                    saves_left -= 1
                                    save_game(file_path2, snake, framerate, multiplier, food_counter, score, elapsed_time, food_pos, token_pos, body_count, saves_left, display_bool, pause_sound_played)
                                    break
                                elif 360 + 260 > mouse[0] > 360 and 575 + 120 > mouse[1] > 575 and saves_left > 0: #Save File 3
                                    pygame.mixer.music.play(0)
                                    saves_left -= 1
                                    print(saves_left)
                                    save_game(file_path3, snake, framerate, multiplier, food_counter, score, elapsed_time, food_pos, token_pos, body_count, saves_left, display_bool, pause_sound_played)
                                    break
                                elif saves_left == 0:
                                    pygame.mixer.music.load('/Users/apple/Snake-Game/Snake/Assets/snake collision.wav')
                                    pygame.mixer.music.play(0)
                                    out_of_saves = font3.render(f'No More Saves!', True, WHITE)
                                    gameDisplay.blit(out_of_saves, (425,260))
                                    pygame.display.update()
                            if (event.type == pygame.KEYDOWN and event.key == pygame.K_TAB):
                                save_pause = False
                
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_TAB):
                pause = False

    return home, saves_left

def save_game(file_path, snake, framerate, multiplier, food_counter, score, elapsed_time, food_pos, token_pos, body_count, saves_left, if_statement_run, sound_played):
    pygame.mixer.music.load('/Users/apple/Snake-Game/Snake/Assets/snake pause.wav')
    pygame.mixer.music.play(0)
    with open(file_path, "wb") as file:
        data = (snake, framerate, multiplier, food_counter, score, elapsed_time, food_pos, token_pos, body_count,saves_left, if_statement_run, sound_played)
        pickle.dump(data, file)

def load_game(file_path):
    with open(file_path, "rb") as file:
        # Load the binary file and restore the grid, score, and food_location variables
        snake, framerate, multiplier, food_counter, score, elapsed_time, food_pos, token_pos, body_count, saves_left, if_statement_run, pause_sound_played = pickle.load(file)
    return snake, framerate, multiplier, food_counter, score, elapsed_time, food_pos, token_pos, body_count, saves_left, if_statement_run, pause_sound_played

def render_saves(
save_file1_tokens,
save_file1_score,
save_file1_saves,
save_file2_tokens,
save_file2_score,
save_file2_saves,
save_file3_tokens,
save_file3_score,
save_file3_saves):
    save_file1 = font.render(f'File 1:', True, WHITE)
    save_file2 = font.render(f'File 2:', True, WHITE)
    save_file3 = font.render(f'File 3:', True, WHITE)


    gameDisplay.blit(save_file1, (390,320))
    gameDisplay.blit(save_file2, (390,460))
    gameDisplay.blit(save_file3, (390,610))

    gameDisplay.blit(save_file1_tokens, (500,290))
    gameDisplay.blit(save_file1_score, (500,330))
    gameDisplay.blit(save_file1_saves, (500,370))

    gameDisplay.blit(save_file2_tokens, (500,430))
    gameDisplay.blit(save_file2_score, (500,470))
    gameDisplay.blit(save_file2_saves, (500,510))

    gameDisplay.blit(save_file3_tokens, (500,580))
    gameDisplay.blit(save_file3_score, (500,620))
    gameDisplay.blit(save_file3_saves, (500,660))

    pygame.display.update()


def create_button(x, y, width, height, text):

    # Create a font object
    font = pygame.font.Font(FONT, 35)
    # Render the text to a surface
    text_surface = font.render(text, True, (255, 255, 255))
    gameDisplay.blit(text_surface, (x + width / 2 - text_surface.get_width() / 2, y + height / 2 - text_surface.get_height() / 2))

def draw_buttons():
        create_button(x, y1, 300, 60, f'-{round(len(snake.body) * .3)}  Links')
        create_button(x, y2, 300, 60, '-5  Speed')
        create_button(x, y3, 300, 60, '2x  Multiplier')


def button_screen():
    pause_background = pygame.image.load('/Users/apple/Snake-Game/Snake/Assets/pause screen.png')
    pause_hover = pygame.image.load('/Users/apple/Snake-Game/Snake/Assets/pause_screen_hover.png')
    sub_screen = pygame.Surface((395, 395))
    sub_screen.fill(BLACK)
    gameDisplay.blit(sub_screen, [310, 310])
    gameDisplay.blit(pause_background, [0, -35])
    print('this happened')

    # Create new buttons
    draw_buttons()
    pygame.display.update()
    is_hovering = False

    while True:
        mouse = pygame.mouse.get_pos()
        if x2 + 197 > mouse[0] > x2 and y1 + 55 > mouse[1] > y1: #BACK HOME HOVER WHEN SAVING GAME
            if not is_hovering:
                print('why')
                is_hovering = True
                gameDisplay.blit(pause_hover, (x + 50, y1))
                draw_buttons()
                pygame.display.update()
        elif x2 + 197 > mouse[0] > x2 and y2 + 55 > mouse[1] > y2: #BACK HOME HOVER WHEN SAVING GAME
            if not is_hovering:
                print('why2')
                is_hovering = True
                gameDisplay.blit(pause_hover, (x + 50, y2))
                draw_buttons()
                pygame.display.update()
        elif x2 + 197 > mouse[0] > x2 and y3 + 55 > mouse[1] > y3: #BACK HOME HOVER WHEN SAVING GAME
            if not is_hovering:
                print('why3')
                is_hovering = True
                gameDisplay.blit(pause_hover, (x + 50, y3))
                draw_buttons()
                pygame.display.update()
        else:
            if is_hovering:
                is_hovering = False                    
                sub_screen = pygame.Surface((395, 395))
                sub_screen.fill(BLACK)
                gameDisplay.blit(sub_screen, [310, 310])
                gameDisplay.blit(pause_background, [0, -35])
                draw_buttons()
                pygame.display.update()
        event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            pygame.mixer.music.load('/Users/apple/Snake-Game/Snake/Assets/snake loop food.wav')
            pygame.mixer.music.play(0)
            mouse = pygame.mouse.get_pos()
            if x2 + 197 > mouse[0] > x2 and y1 + 55 > mouse[1] > y1:
                remove_parts()
                return
            if x2 + 197 > mouse[0] > x2 and y2 + 55 > mouse[1] > y2:
                slow_snake()
                return
            if x2 + 197 > mouse[0] > x2 and y3 + 55 > mouse[1] > y3:
                multiply_score()
                return

            


def remove_parts():
    snake_body = len(snake.body)
    while len(snake.body) >= snake_body * .7:
        snake.body = snake.body[:-1]

def slow_snake():
    global framerate
    framerate = framerate - 5

def multiply_score():
    global multiplier
    multiplier = multiplier * 2

class Snake:
    def __init__(self):
        self.body = [(9, 6), (9, 7), (9, 8)]
        self.direction = "UP"
        self.score = 0
        self.tokens = 0

    def change_direction(self, direction):
        if direction == "UP" and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif direction == "DOWN" and self.direction != "LEFT":
            self.direction = "RIGHT" 
        elif direction == "LEFT" and self.direction != "DOWN":
            self.direction = "UP"
        elif direction == "RIGHT" and self.direction != "UP":
            self.direction = "DOWN"

    def move(self):

        x, y = self.body[0]

        if self.direction == "UP":
            y -= 1
        elif self.direction == "DOWN":
            y += 1
        elif self.direction == "LEFT":
            x -= 1
        elif self.direction == "RIGHT":
            x += 1

        self.body.insert(0, (x, y))

        # If the snake did not eat any food, remove the last part of the body
        if (x, y) != food_pos:
            self.body.pop()


    def check_collision(self):
        # Check if the snake hit a wall or itself
        x, y = self.body[0]

        if x < 0 or x > 19 or y < 0 or y > 19:
            return True
        if self.body[0] in self.body[1:]:
            return True
        if homescreen:
            return True

        return False
        

    def check_food(self):
        # Check if the snake ate the food
        if self.body[0] == food_pos and (self.score % 50 != 0 or self.score == 0):
            self.score += 1
            return True

        return False

    def check_token(self):
        if self.body[0] == token_pos and self.score and self.score % 50 == 0 and self.score != 0:
            self.score += 1
            self.tokens += 1
            return True
        
        return False

# Initialize pygame
pygame.init()

# Set display dimensions
display_width = 600
display_height = 600

# Initialize game display
gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.mixer.music.load('/Users/apple/Snake-Game/Snake/Assets/snake loop.wav')

first_key_pressed = False

saves_left = 3
elapsed_time = 0
framerate = 20
multiplier = 1
food_counter = 0
body_count = 0
snake = Snake()
food_pos = (random.randint(0, 19), random.randint(0, 19))
token_pos = (random.randint(0, 19), random.randint(0, 19))

# Define font
font = pygame.font.Font(FONT, 45)        
font2 = pygame.font.Font(FONT, 150)
font3 = pygame.font.Font(FONT, 25)

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [1000, 1000]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# -------- Main Program Loop -----------
display_bool = False
pause_sound_played = False
while not done:
    
    #BUTTON SCREEN BLOCK
    if not display_bool and snake.score % 10 == 1 and snake.score != 1:
        if not pause_sound_played:
            pygame.mixer.music.load('/Users/apple/Snake-Game/Snake/Assets/snake pause.wav')
            pygame.mixer.music.play(0)
            print('this happened')
            button_screen()
            pause_sound_played = True
        framerate = framerate + 5
        display_bool = True
        first_key_pressed = False

    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if not first_key_pressed:
                pygame.mixer.music.play(-1)
                first_key_pressed = True
            if event.key == pygame.K_TAB:
                home, saves_left = pause_screen(saves_left)
                first_key_pressed = False
                if home:
                    homescreen = True
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                snake.change_direction("UP")
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                snake.change_direction("DOWN")
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                snake.change_direction("LEFT")
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                snake.change_direction("RIGHT")



        elif display_bool and snake.score % 10 == 0:
            display_bool = False
            pause_sound_played = False

    # --- Game logic should go here

    if first_key_pressed:
        snake.move()
        elapsed_time += clock.tick(framerate) / 1000.0
        pygame.mixer.music.load('/Users/apple/Snake-Game/Snake/Assets/snake loop.wav')
        pygame.mixer.music.play(-1)

    if snake.check_collision():
        pygame.mixer.music.load('/Users/apple/Snake-Game/Snake/Assets/snake collision.wav')
        pygame.mixer.music.play(0)
        framerate = 20
        elapsed_time = 0
        multiplier = 1
        food_pos = (random.randint(0, 19), random.randint(0, 19))
        first_key_pressed = False
        food_counter = 0
        body_count = 0
        saves_left = 3
        snake = Snake()

    if snake.score < 20:
        x = 350
        x2 = 400
        y1 = 370
        y2 = 440
        y3 = 510 

    quicker = snake.score % 10 == 0 and snake.score != 0

    if snake.check_food():
        food_counter += multiplier
        pygame.mixer.music.load('/Users/apple/Snake-Game/Snake/Assets/snake loop food.wav')
        pygame.mixer.music.play(0)
        while (snake.score % 50 != 0 or snake.score == 0):
            food_pos = (random.randint(0, 19), random.randint(0, 19))
            if food_pos not in snake.body:
                break

    if snake.check_token():
        food_counter += 1
        pygame.mixer.music.load('/Users/apple/Snake-Game/Snake/Assets/token.wav')
        pygame.mixer.music.play(0)
        while snake.score % 50 == 1 and snake.score != 0:
            token_pos = (random.randint(0, 19), random.randint(0, 19))
            if token_pos not in snake.body and token_pos != food_pos:
                break

    

    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)

    if homescreen:
        file = home_screen()

    
    if game_loaded:
        snake, framerate, multiplier, food_counter, score, elapsed_time, food_pos, token_pos, body_count, saves_left, display_bool, pause_sound_played = load_game(file)
        game_loaded = False

    # Draw the grid
    for row in range(20):
        for column in range(20):
            color = WHITE
            if (row, column) in snake.body:
                color = GREEN
            elif (snake.score % 50 != 0 or snake.score == 0) and (row, column) == food_pos:
                color = RED
            elif snake.score % 50 == 0 and snake.score != 0 and (row, column) == token_pos:
                color = GOLD
            pygame.draw.rect(
                screen,
                color,
                [
                    (MARGIN + WIDTH) * column + MARGIN + 175,
                    (MARGIN + HEIGHT) * row + MARGIN + 175,
                    WIDTH,
                    HEIGHT,
                ],
            )    
            

    # Get score
    score = food_counter

    background = pygame.image.load('/Users/apple/Snake-Game/Snake/Assets/Snake Trees.png')
    score_text = font.render("Score: " + str(score), True, WHITE)
    time_text = font.render("{:02d}:{:02d}".format(int(elapsed_time // 60), int(elapsed_time % 60)), True, WHITE)
    game_text = font2.render("SNAKE", True, WHITE)
    token_text = font3.render("Tokens: " + str(snake.tokens), True, WHITE)
    save_text = font3.render("Saves left: " + str(saves_left), True, WHITE)


    with open(file_path1, "rb") as file:
        data = pickle.load(file)
    save_file1_tokens = font3.render(f'tokens: {data[0].tokens}', True, (255, 255, 255)) 
    save_file1_score = font3.render(f'score: {data[3]}', True, (255, 255, 255))
    save_file1_saves = font3.render(f'saves left: {data[9]}', True, (255, 255, 255))

    with open(file_path2, "rb") as file:
        data = pickle.load(file)
    save_file2_tokens = font3.render(f'tokens: {data[0].tokens}', True, (255, 255, 255)) 
    save_file2_score = font3.render(f'score: {data[3]}', True, (255, 255, 255))
    save_file2_saves = font3.render(f'saves left: {data[9]}', True, (255, 255, 255))

    with open(file_path3, "rb") as file:
        data = pickle.load(file)
    save_file3_tokens = font3.render(f'tokens: {data[0].tokens}', True, (255, 255, 255)) 
    save_file3_score = font3.render(f'score: {data[3]}', True, (255, 255, 255))
    save_file3_saves = font3.render(f'saves left: {data[9]}', True, (255, 255, 255))

    # Display score and time
    gameDisplay.blit(score_text, [50, 55])
    gameDisplay.blit(token_text, [50, 110])
    gameDisplay.blit(save_text, [50, 150])
    gameDisplay.blit(time_text, [875, 70])
    gameDisplay.blit(game_text, [320, 25])
    gameDisplay.blit(background, [0,-25])

    pygame.display.update()

    # --- Update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second

    clock.tick(framerate)