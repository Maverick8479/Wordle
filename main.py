import random

import pygame
from settings import *
from sprites import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        background = pygame.image.load('WORDLE.png')
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.create_word_list()
        self.letters_text = UIElement(100, 700, "Not Enough Letters", BLACK)
        self.not_in_list = UIElement(110, 700, "Not in word list", BLACK )

    def create_word_list(self):
        with open("words.txt", "r") as file:
            self.words_list = file.read().splitlines()
        
        for i, word in enumerate(self.words_list):
            self.words_list[i] = word.upper()
        # print(self.words_list)

    def new(self):
        self.word = random.choice(self.words_list).upper()
        print(self.word)
        self.text = ""
        self.current_row = 0
        self.tiles = []
        self.create_tiles()
        self.flip = True
        self.not_enough_letters = False
        self.not_in_word_list = False
        self.timer = 0

    def create_tiles(self):
        for row in range(6):
            self.tiles.append([])
            for col in range(5):
                self.tiles[row].append(Tile((col * (TILESIZE + GAPSIZE)) + MARGIN_X, (row * (TILESIZE + GAPSIZE)) + MARGIN_Y))

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.add_letter()

    def add_letter(self):
        # empty all the letter in the current row
        for tile in self.tiles[self.current_row]:
            tile.letter = ""

        # add the letters typed to the current row
        for i, letter in enumerate(self.text):
            self.tiles[self.current_row][i].letter = letter
            self.tiles[self.current_row][i].create_font()

    def draw_tiles(self):
        for row in self.tiles:
            for tile in row:
                tile.draw(self.screen)

    def draw(self):
        # self.screen.fill(BGCOLOUR)
        #background
        self.screen.blit(background,(0,0))
        # display the not enough letters text
        if self.not_enough_letters:
            self.timer += 1
            self.letters_text.fade_in()
            if self.timer > 90:
                self.not_enough_letters = False
                self.timer = 0
        else:
            self.letters_text.fade_out()

        
        if self.not_in_word_list:
            self.timer += 1
            self.not_in_list.fade_in()
            if self.timer > 90:
                self.not_in_word_list = False
                self.timer = 0
                self.clearRow()
        else:
            self.not_in_list.fade_out()
        self.not_in_list.draw(self.screen)
        self.letters_text.draw(self.screen)

        self.draw_tiles()

        pygame.display.flip()

    def row_animation(self, str="not enough letters"):
        # row shaking if not enough letters is inputted
        if str == "not enough letters":
            self.not_enough_letters = True
        else:
            self.not_in_word_list = True
        start_pos = self.tiles[0][0].x
        amount_move = 4
        move = 3
        screen_copy = self.screen.copy()
        # screen_copy.fill(BGCOLOUR)
        #background
        screen_copy.blit(background,(0,0))
        for row in self.tiles:
            for tile in row:
                if row != self.tiles[self.current_row]:
                    tile.draw(screen_copy)

        while True:
            while self.tiles[self.current_row][0].x < start_pos + amount_move:
                self.screen.blit(screen_copy, (0, 0))
                for tile in self.tiles[self.current_row]:
                    tile.x += move
                    tile.draw(self.screen)
                self.clock.tick(FPS)
                pygame.display.flip()

            while self.tiles[self.current_row][0].x > start_pos - amount_move:
                self.screen.blit(screen_copy, (0, 0))
                for tile in self.tiles[self.current_row]:
                    tile.x -= move
                    tile.draw(self.screen)
                self.clock.tick(FPS)
                pygame.display.flip()

            amount_move -= 2
            if amount_move < 0:
                break

    def box_animation(self):
        # tile scale animation for every letter inserted
        for tile in self.tiles[self.current_row]:
            if tile.letter == "":
                screen_copy = self.screen.copy()
                for start, end, step in ((0, 6, 1), (0, -6, -1)):
                    for size in range(start, end, 2*step):
                        self.screen.blit(screen_copy, (0, 0))
                        tile.x -= size
                        tile.y -= size
                        tile.width += size * 2
                        tile.height += size * 2
                        surface = pygame.Surface((tile.width, tile.height))
                        surface.fill((250, 236, 232))
                        #background
                        self.screen.blit(surface, (tile.x, tile.y))
                        tile.draw(self.screen)
                        pygame.display.flip()
                        self.clock.tick(FPS)
                    self.add_letter()
                break

    def reveal_animation(self, tile, colour):
        # reveal colours animation when user input the whole word
        screen_copy = self.screen.copy()

        while True:
            surface = pygame.Surface((tile.width + 5, tile.height + 5))
            # surface.fill(BGCOLOUR)
            #background
            self.screen.blit(background,(0,0))
            # screen_copy.blit(background,(0,0))
            screen_copy.blit(surface, (tile.x, tile.y))
            self.screen.blit(screen_copy, (0, 0))
            if self.flip:
                tile.y += 6
                tile.height -= 12
                tile.font_y += 4
                tile.font_height = max(tile.font_height - 8, 0)
            else:
                tile.colour = colour
                tile.y -= 6
                tile.height += 12
                tile.font_y -= 4
                tile.font_height = min(tile.font_height + 8, tile.font_size)
            if tile.font_height == 0:
                self.flip = False

            tile.draw(self.screen)
            pygame.display.update()
            self.clock.tick(FPS)

            if tile.font_height == tile.font_size:
                self.flip = True
                break

    def check_letters(self):
        # algorithm to check if the letters inputted correspond to any of the letters in the actual word
        copy_word = [x for x in self.word]
        for i, user_letter in enumerate(self.text):
            colour = LIGHTGREY
            for j, letter in enumerate(copy_word):
                if user_letter == letter:
                    colour = YELLOW
                    if i == j:
                        colour = GREEN
                    copy_word[j] = ""
                    break
            # reveal animation
            self.reveal_animation(self.tiles[self.current_row][i], colour)
    
    def clearRow(self):
        self.text = ""

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit(0)
                if event.key == pygame.K_RETURN:
                    if len(self.text) == 5 and self.text in self.words_list:
                        # check all letters
                        self.check_letters()

                        # if the text is correct or the player has used all his turns
                        if self.text == self.word or self.current_row + 1 == 6:
                            # player lose, lose message is sent
                            if self.text != self.word:
                                self.end_screen_text = UIElement(100, 680, f"THE WORD WAS: {self.word}", RED)

                            # player win, send win message
                            else:
                                self.end_screen_text = UIElement(100, 680, "YOU GUESSED RIGHT", GREEN)

                            # restart the game
                            self.playing = False
                            self.end_screen()
                            break

                        self.current_row += 1
                        self.text = ""

                    else:
                        if len(self.text) != 5:
                            #   row animation, not enough letters message
                            self.row_animation()
                        else:
                            self.row_animation("not in word list")

                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]

                else:
                    if len(self.text) < 5 and event.unicode.isalpha():
                        self.text += event.unicode.upper()
                        self.box_animation()

    def end_screen(self):
        play_again = UIElement(85, 725, "PRESS ENTER TO PLAY AGAIN", BLACK, 30)
        exit = UIElement(85, 750, "PRESS ESCAPE TO EXIT", BLACK, 30)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit(0)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return

                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit(0)

            # self.screen.fill(BGCOLOUR)
            #background
            self.screen.blit(background,(0,0))
            self.draw_tiles()
            self.end_screen_text.fade_in()
            self.end_screen_text.draw(self.screen)
            play_again.fade_in()
            play_again.draw(self.screen)
            exit.fade_in()
            exit.draw(self.screen)
            pygame.display.flip()


game = Game()
while True:
    game.new()
    game.run()
