import pygame
import os
from constants import BASEPATH, BLACK, WHITE, H1, H4, H5, H6, SAVEFILE1, SAVEFILE2, SAVEFILE3, WINDOW_SIZE, MARGIN, WIDTH, HEIGHT
from enum import Enum
from variables import Variables
from helpers import transformTypeToColor
from grid import CellType

variables = Variables()

class RewardType(Enum):
    Links = 1,
    Speed = 2,
    Multiplier = 3

class DisplayType(Enum):
    Home = 1,
    Game = 2,
    Reward = 3,
    Pause = 4

class Display:
    def __init__(self):
        self._current_display = DisplayType.Home
        self._display_width = 600
        self._display_height = 600
        self._game_display = pygame.display.set_mode((self._display_width, self._display_height))

    def initDisplay(self) -> None:
        self._screen = pygame.display.set_mode(WINDOW_SIZE)
        self._screen.fill(BLACK)

    def getCurrentDisplay(self) -> DisplayType:
        return self._current_display

    def showRewardScreen(self) -> RewardType:
        self._current_display = DisplayType.Reward
        pause_background = pygame.image.load(os.path.join(BASEPATH, 'Assets/pause screen.png'))
        sub_screen = pygame.Surface((395, 395))
        sub_screen.fill(BLACK)
        self._game_display.blit(sub_screen, [310, 310])
        self._game_display.blit(pause_background, [0, -35])

        # Create new buttons
        self.draw_buttons()
        pygame.display.update()

        while True:
            event = pygame.event.wait()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pygame.mixer.music.load(os.path.join(BASEPATH, 'Assets/snake loop food.wav'))
                pygame.mixer.music.play(0)
                mouse = pygame.mouse.get_pos()
                if 650 > mouse[0] > 350 and 430 > mouse[1] > 370:
                    self._current_display = DisplayType.Game
                    return RewardType.Links
                if 650 > mouse[0] > 350 and 500 > mouse[1] > 440:
                    self._current_display = DisplayType.Game
                    return RewardType.Speed
                if 650 > mouse[0] > 350 and 570 > mouse[1] > 510:
                    self._current_display = DisplayType.Game
                    return RewardType.Multiplier
    
    def showHomeScreen(self) -> None:
        self._current_display = DisplayType.Home
        pygame.mixer.music.load(os.path.join(BASEPATH, 'Assets/snake music.wav'))
        pygame.mixer.music.play(-1)
        home_screen_surface = pygame.Surface((1000, 1000))
        pygame.draw.rect(self._game_display, BLACK, (500, 500, 500, 500), 0)
        background = pygame.image.load(os.path.join(BASEPATH, 'Assets/main_screen2.png'))
        # button = pygame.image.load(os.path.join(BASEPATH, 'Assets/button background.png'))
        button_background = pygame.image.load(os.path.join(BASEPATH, 'Assets/button_background_background.png'))
        game_text = H1.render("SNAKE", True, WHITE)
        start_button = H4.render("New Game", True, WHITE)
        load_button = H4.render("Load Game", True, WHITE)
        token_shop = H4.render("Token Shop", True, WHITE)
        game_info = H4.render("Game Info", True, WHITE)

        home_screen_surface.blit(button_background, [0,-35])
        home_screen_surface.blit(background, [0,-35])
        home_screen_surface.blit(game_text, [305, 25])
        home_screen_surface.blit(start_button, [420, 240])
        home_screen_surface.blit(load_button, [415, 380])
        home_screen_surface.blit(token_shop, [405, 520])
        home_screen_surface.blit(game_info, [415, 660])

        self._game_display.blit(home_screen_surface, (0, 0))
        pygame.display.update()

        while True:
            event = pygame.event.wait()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse = pygame.mouse.get_pos()
                if 420 + 300 > mouse[0] > 420 and 240 + 80 > mouse[1] > 240: #START GAME
                    pygame.mixer.music.load(os.path.join(BASEPATH, 'Assets/start noise1.wav'))
                    pygame.mixer.music.play(0)
                    self._current_display = DisplayType.Game
                    return
                if 415 + 300 > mouse[0] > 415 and 380 + 80 > mouse[1] > 380: #LOAD GAME
                    pause_background = pygame.image.load(os.path.join(BASEPATH, 'Assets/pause screen.png'))
                    sub_screen = pygame.Surface((395, 395))
                    sub_screen.fill(BLACK)
                    self._game_display.blit(sub_screen, [310, 310])
                    self._game_display.blit(pause_background, [0, -35])
                    save_file1 = H4.render(f'File 1:', True, WHITE)
                    save_file2 = H4.render(f'File 2:', True, WHITE)
                    save_file3 = H4.render(f'File 3:', True, WHITE)

                    if os.path.exists(SAVEFILE1):
                        save_file1_text = H6.render(f'score:', True, WHITE)
                    else:
                        save_file1_text = H6.render(f'new file', True, WHITE)
                    if os.path.exists(SAVEFILE2):
                        save_file2_text = H6.render(f'score:', True, WHITE)
                    else:
                        save_file2_text = H6.render(f'new file', True, WHITE)
                    if os.path.exists(SAVEFILE3):
                        save_file3_text = H6.render(f'score:', True, WHITE)
                    else:
                        save_file3_text = H6.render(f'new file', True, WHITE)

                    self._game_display.blit(save_file1, (390,390))
                    self._game_display.blit(save_file2, (390,490))
                    self._game_display.blit(save_file3, (390,590))
                    self._game_display.blit(save_file1_text, (500,397))
                    self._game_display.blit(save_file2_text, (500,497))
                    self._game_display.blit(save_file3_text, (500,597))
                    pygame.mixer.music.load(os.path.join(BASEPATH, 'Assets/start noise1.wav'))
                    pygame.mixer.music.play(0)
                    pygame.display.update()

                    pygame.draw.rect(self._game_display, BLACK, (478, 387, 110, 50), 0)
                    pygame.draw.rect(self._game_display, BLACK, (478, 487, 110, 50), 0)
                    pygame.draw.rect(self._game_display, BLACK, (478, 587, 110, 50), 0)

                    pause = True
                    file_path = None

                    while pause:
                        for event in pygame.event.get():
                            mouse = pygame.mouse.get_pos()
                            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                                if 478 + 110 > mouse[0] > 478 and 387 + 50 > mouse[1] > 387: #START GAME
                                    pygame.mixer.music.load(os.path.join(BASEPATH, 'Assets/start noise1.wav'))
                                    pygame.mixer.music.play(0)
                                    self._current_display = DisplayType.Game                                    
                                    game_loaded = True
                                    file_path = SAVEFILE1
                                    return file_path
                                elif 478 + 110 > mouse[0] > 478 and 487 + 50 > mouse[1] > 387: #START GAME
                                    pygame.mixer.music.load(os.path.join(BASEPATH, 'Assets/start noise1.wav'))
                                    pygame.mixer.music.play(0)
                                    self._current_display = DisplayType.Game                                    
                                    game_loaded = True                                
                                    file_path = SAVEFILE2
                                    return file_path
                                elif 478 + 110 > mouse[0] > 478 and 587 + 50 > mouse[1] > 387: #START GAME
                                    pygame.mixer.music.load(os.path.join(BASEPATH, 'Assets/start noise1.wav'))
                                    pygame.mixer.music.play(0)
                                    self._current_display = DisplayType.Game                                    
                                    game_loaded = True                               
                                    file_path = SAVEFILE3
                                    return file_path

    def showPauseScreen(self) -> None:
        self._screen.fill(BLACK)
        self._current_display = DisplayType.Pause
        pygame.mixer.music.load(os.path.join(BASEPATH, 'Assets/snake pause.wav'))
        pygame.mixer.music.play(0)

        pause_background = pygame.image.load(os.path.join(BASEPATH, 'Assets/pause screen.png'))
        sub_screen = pygame.Surface((395, 395))
        sub_screen.fill(BLACK)
        self._game_display.blit(sub_screen, [310, 310])
        self._game_display.blit(pause_background, [0, -35])

        speed = H5.render(f'Speed:     {variables.framerate}', True, WHITE)
        # links = H5.render(f'Links:     {len(snake.body)}', True, WHITE)
        links = H5.render(f'Links:     3', True, WHITE)
        multiplier_text = H5.render(f'Multiplier:     {variables.multiplier} x', True, WHITE)
        save_text = H5.render(f'Save Game', True, WHITE)
        self._game_display.blit(speed, (430,365))
        self._game_display.blit(links, (440,440))
        self._game_display.blit(multiplier_text, (410,515))
        self._game_display.blit(save_text, (430,590))
        pygame.display.update()

        pause = True

        while pause:
            for event in pygame.event.get():
                mouse = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if 430 + 300 > mouse[0] > 420 and 590 + 80 > mouse[1] > 590: #START GAME
                        pause_background = pygame.image.load(os.path.join(BASEPATH, 'Assets/pause screen.png'))
                        sub_screen = pygame.Surface((395, 395))
                        sub_screen.fill(BLACK)
                        self._game_display.blit(sub_screen, [310, 310])
                        self._game_display.blit(pause_background, [0, -35])
                        save_file1 = H5.render(f'File 1:', True, WHITE)
                        save_file2 = H5.render(f'File 2:', True, WHITE)
                        save_file3 = H5.render(f'File 3:', True, WHITE)

                        if os.path.exists(SAVEFILE1):
                            save_file1_text = H6.render(f'score:', True, WHITE)
                        else:
                            save_file1_text = H6.render(f'new file', True, WHITE)
                        if os.path.exists(SAVEFILE2):
                            save_file2_text = H6.render(f'score:', True, WHITE)
                        else:
                            save_file2_text = H6.render(f'new file', True, WHITE)
                        if os.path.exists(SAVEFILE3):
                            save_file3_text = H6.render(f'score:', True, WHITE)
                        else:
                            save_file3_text = H6.render(f'new file', True, WHITE)

                        self._game_display.blit(save_file1, (390,390))
                        self._game_display.blit(save_file2, (390,490))
                        self._game_display.blit(save_file3, (390,590))
                        self._game_display.blit(save_file1_text, (500,397))
                        self._game_display.blit(save_file2_text, (500,497))
                        self._game_display.blit(save_file3_text, (500,597))
                        pygame.mixer.music.load(os.path.join(BASEPATH, 'Assets/start noise1.wav'))
                        pygame.mixer.music.play(0)
                        pygame.display.update()

                        pygame.draw.rect(self._game_display, BLACK, (478, 387, 110, 50), 0)
                        pygame.draw.rect(self._game_display, BLACK, (478, 487, 110, 50), 0)
                        pygame.draw.rect(self._game_display, BLACK, (478, 587, 110, 50), 0)

                        pause = True

                        while pause:
                            for event in pygame.event.get():
                                mouse = pygame.mouse.get_pos()
                                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                                    if 478 + 110 > mouse[0] > 478 and 387 + 50 > mouse[1] > 387: #START GAME
                                        # save_game(SAVEFILE1, snake, framerate, multiplier, food_counter, score, elapsed_time, food_pos, token_pos, body_count, given_reward)
                                        return
                                    elif 478 + 110 > mouse[0] > 478 and 487 + 50 > mouse[1] > 387: #START GAME
                                        # save_game(SAVEFILE2, snake, framerate, multiplier, food_counter, score, elapsed_time, food_pos, token_pos, body_count, given_reward)
                                        return
                                    elif 478 + 110 > mouse[0] > 478 and 587 + 50 > mouse[1] > 387: #START GAME
                                        # save_game(SAVEFILE3, snake, framerate, multiplier, food_counter, score, elapsed_time, food_pos, token_pos, body_count, given_reward)
                                        return
                    
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_TAB):
                    self._current_display = DisplayType.Game
                    pause = False
    
    def showGameScreen(self, grid, food_pos, score, elapsed_time, snake) -> None:
        self._screen.fill(BLACK)

        for x, row in enumerate(grid.getGrid()):
            for y, cell in enumerate(row):
                if food_pos == (x,y):
                    pygame.draw.rect(
                        self._screen,
                        transformTypeToColor(CellType.FOOD),
                        [
                            (MARGIN + WIDTH) * y + MARGIN + 175,
                            (MARGIN + HEIGHT) * x + MARGIN + 175,
                            WIDTH,
                            HEIGHT,
                        ],
                    )
                else:
                    pygame.draw.rect(
                        self._screen,
                        transformTypeToColor(cell),
                        [
                            (MARGIN + WIDTH) * y + MARGIN + 175,
                            (MARGIN + HEIGHT) * x + MARGIN + 175,
                            WIDTH,
                            HEIGHT,
                        ],
                    )

        background = pygame.image.load(os.path.join(BASEPATH, 'Assets/Snake Background1.png'))
        score_text = H4.render("Score: " + str(score), True, WHITE)
        time_text = H4.render("{:02d}:{:02d}".format(int(elapsed_time // 60), int(elapsed_time % 60)), True, WHITE)
        game_text = H1.render("SNAKE", True, WHITE)
        token_text = H6.render("Tokens:" + str(snake.tokens), True, WHITE)

        # Display score and time
        self._game_display.blit(score_text, [50, 65])
        self._game_display.blit(token_text, [50, 125])
        self._game_display.blit(time_text, [875, 70])
        self._game_display.blit(game_text, [320, 25])
        self._game_display.blit(background, [0,-25])
        
    def draw_buttons(self):
        self.create_button(350, 370, 300, 60, '-3 Links')
        self.create_button(350, 440, 300, 60, '-5 Speed')
        self.create_button(350, 510, 300, 60, '2x Multiplier')

    def create_button(self, x, y, width, height, text):
        # Render the text to a surface
        text_surface = H5.render(text, True, WHITE)
        self._game_display.blit(text_surface, (x + width / 2 - text_surface.get_width() / 2, y + height / 2 - text_surface.get_height() / 2))