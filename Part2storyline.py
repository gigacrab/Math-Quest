import pygame
import pygame, sys
import random
from pygame.locals import *


class Screens:
    def __init__(self):
        pygame.init()
        self.small_font = pygame.font.Font('slkscr.ttf', 30)
        self.big_font = pygame.font.Font('slkscr.ttf', 40)
        self.huge_font = pygame.font.Font('slkscr.ttf', 90)
        self.super_small_font = pygame.font.Font('slkscr.ttf', 20)
        self.running = True
        self.screen = pygame.display.set_mode([1080, 600])
        self.clock = pygame.time.Clock()
        self.robot1 = pygame.image.load("Picture/Robot_2ndImage.png")
        self.robot_hand1 = pygame.image.load('Picture/RobotHand_1stImage.png')
        self.robot_angry = pygame.image.load('Picture/Robot_angry.png')
        self.next_button = pygame.image.load('Buttons/ButtonNext.png')
        self.text_box = pygame.image.load('OtherPictures&Screen/TextBox_Storyline.png')
        self.alien_attack_pic = pygame.image.load('Picture/astronaut_scared_of_alien.png')
        self.small_text_box = pygame.image.load('OtherPictures&Screen/TextBox_WithRobotIcon.png')
        self.alien_green = pygame.image.load('Picture/AlienGreen.png')
        self.alien_green_defeated = pygame.image.load('Picture/Defeated_AlienGreen.png')
        self.alien_yellow_defeated = pygame.image.load('Picture/Defeated_AlienYellow.png')
        self.alien_orange_defeated = pygame.image.load('Picture/Defeated_AlienOrange.png')
        self.alien_purple_defeated = pygame.image.load('Picture/Defeated_AlienPurple.png')
        self.alien_pink_defeated = pygame.image.load('Picture/Defeated_AlienPink.png')
        self.alien_blue_defeated = pygame.image.load('Picture/Defeated_AlienBlue.png')
        self.alien_scientist_defeated = pygame.image.load('Picture/Defeated_AlienGreen_Scientist.png')
        self.cloak_barry_defeated = pygame.image.load('Picture/BarryCloak_defeated.png')
        self.real_barry_defeated = pygame.image.load('Picture/BarryReal_defeated.png')
        self.back_button = pygame.image.load('Buttons/ButtonBack.png')
        self.cloak = pygame.image.load('Picture/BarryCloak.png')
        self.cloak_defeated = pygame.image.load('Picture/BarryCloak_defeated.png')
        self.barry = pygame.image.load('Picture/BarryReal.png')
        self.barry_defeated = pygame.image.load('Picture/BarryReal_defeated.png')
        self.deny_button = pygame.image.load('Buttons/ButtonDeny.png')
        self.accept_button = pygame.image.load('Buttons/ButtonAccept.png')
        self.peace_image = pygame.image.load('OtherPictures&Screen/peace_screen.png')
        self.semi_trans_pause = pygame.image.load("OtherPictures&Screen/semiTransparent_pause.png")
        self.rip_barry = pygame.image.load('OtherPictures&Screen/rip_barry.png')
        self.furthest_screen = 0
        self.current_screen = 1
        self.furthest_screen_barry = 0
        self.current_screen_barry = 1
        self.current_screen_cloak = 1
        self.furthest_screen_cloak = 0
        self.player_name = ''
        self.dw_skip = True
        self.ran_b4 = False
        self.ran4 = False
        self.screen_8_skip = False

    def next(self):
        self.screen.blit(self.next_button, (822, 530))
        self.next_button_rect = self.next_button.get_rect()
        self.next_button_rect.topleft = (822, 530)
        pygame.display.update()

    def back(self):
        self.screen.blit(self.back_button, (10, 530))
        self.back_button_rect = self.back_button.get_rect()
        self.back_button_rect.topleft = (10, 530)
        pygame.display.update()

    def reminders(self):
        self.reminder = self.small_font.render('*[Enter] or [next] button to go to next dialog', True, (255, 255, 255))
        self.reminder2 = self.small_font.render('*[Enter] to fast forward dialog', True, (255, 255, 255))
        self.screen.blit(self.reminder, (103, 0))
        self.screen.blit(self.reminder2, (103, 30))

    def display_text_animation(self, string, x, y, colour, font):
        self.text = ''
        i = 0
        if self.ran_b4:
            pass
        elif not self.ran_b4:
            while i < len(string):
                self.text += string[i]
                if font == 's'.lower():
                    self.text_surface = self.small_font.render(self.text, True, (colour))
                elif font == 'b'.lower():
                    self.text_surface = self.big_font.render(self.text, True, (colour))
                elif font == 'h'.lower():
                    self.text_surface = self.huge_font.render(self.text, True, (colour))
                elif font == 'ss'.lower():
                    self.text_surface = self.super_small_font.render(self.text, True, (colour))
                self.text_rect = self.text_surface.get_rect()
                self.text_rect.y = y
                self.text_rect.left = x
                self.screen.blit(self.text_surface, self.text_rect)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.dw_skip = False
                    elif event.type == pygame.QUIT:
                        exit()
                if self.dw_skip:
                    pygame.time.wait(50)
                    i += 1
                elif not self.dw_skip:
                    i += 1

    def screen_1(self):
        self.screen.fill('BLACK')
        self.reminders()
        self.screen.blit(self.robot1, (10, 85))
        self.screen.blit(self.text_box, (0, 350))
        self.display_text_animation('robot:', 53, 360, 'RED', 'b')
        self.display_text_animation('Greetings, adventurer. Welcome to Math ', 213, 365, 'WHITE', 's')
        self.display_text_animation('Quest, where you will experience a whole ', 213, 400, 'WHITE', 's')
        self.display_text_animation('new world full of math.. and aliens.', 213, 435, 'WHITE', 's')
        self.next()
        self.dw_skip = True
        self.ran_b4 = True

    def enter_name(self):
        self.screen.fill('BLACK')
        self.reminders()
        self.remind_en = self.small_font.render('*press [Enter] to submit, name can only consist ', True, (0, 0, 255))
        self.remind_en2 = self.small_font.render('of 10 characters, only letters or numbers', True, (0, 0, 255))
        self.screen.blit(self.remind_en, (103, 60))
        self.screen.blit(self.remind_en2, (128, 90))
        self.enter_name_text = self.big_font.render('Enter name:', True, (255, 255, 255))
        self.screen.blit(self.enter_name_text, (100, 200))
        self.T_player_name = self.big_font.render(str(self.player_name), True, (255, 255, 255))
        self.screen.blit(self.T_player_name, (400, 200))
        self.ran_b4 = True
        self.dw_skip = True

    def screen_3(self, player_name):
        self.screen.fill('BLACK')
        self.reminders()
        self.screen.blit(self.robot1, (10, 85))
        self.screen.blit(self.text_box, (0, 350))
        self.display_text_animation('robot:', 53, 360, 'RED', 'b')
        self.display_text_animation(f'A warm welcome to you, {player_name}. This', 213, 365, 'WHITE', 's')
        self.display_text_animation('story takes place in a spaceship, whereby...', 213, 400, 'WHITE', 's')
        self.next()
        self.dw_skip = True
        self.ran_b4 = True

    def screen_4(self):
        self.screen.fill('BLACK')
        self.screen.blit(self.alien_attack_pic, (0, 0))
        self.screen.blit(self.small_text_box, (150, 10))
        self.display_text_animation('robot:', 303, 60, 'RED', 'b')
        self.display_text_animation('you will be constantly ', 455, 60, 'WHITE', 's')
        self.display_text_animation('attacked by aliens', 455, 90, 'WHITE', 's')
        self.back()
        self.next()
        self.dw_skip = True
        self.ran_b4 = True

    def screen_5(self):
        self.screen.fill('BLACK')
        self.reminders()
        self.screen.blit(self.robot1, (10, 85))
        self.screen.blit(self.text_box, (0, 350))
        self.display_text_animation('robot:', 53, 360, 'RED', 'b')
        self.display_text_animation('And since these nasty aliens came, your', 213, 365, 'WHITE', 's')
        self.display_text_animation('good friend, Barry, went missing.. You', 213, 390, 'WHITE', 's')
        self.display_text_animation('must defend your fellow astronauts from', 213, 415, 'WHITE', 's')
        self.display_text_animation('the aliens and find out what happened ', 213, 440, 'WHITE', 's')
        self.display_text_animation('to Barry! (by solving math questions). ', 213, 465, 'WHITE', 's')
        self.display_text_animation('Defeat all the aliens to beat the game!', 213, 490, 'WHITE', 's')
        self.back()
        self.next()
        self.dw_skip = True
        self.ran_b4 = True

    def screen_6(self):
        self.screen.fill('BLACK')
        self.reminders()
        self.screen.blit(self.robot1, (10, 85))
        self.screen.blit(self.alien_green, (750, 35))
        self.screen.blit(self.text_box, (0, 350))
        self.display_text_animation('robot:', 53, 360, 'RED', 'b')
        self.display_text_animation("Look! There's one alien right there!", 213, 365, 'WHITE', 's')
        self.back()
        self.next()
        self.dw_skip = True
        self.ran_b4 = True

    def screen_7(self):
        self.screen.fill('BLACK')
        self.reminders()
        self.screen.blit(self.robot1, (10, 85))
        self.screen.blit(self.alien_green, (750, 35))
        self.screen.blit(self.text_box, (0, 350))
        self.display_text_animation('robot:', 53, 360, 'RED', 'b')
        self.display_text_animation("Try solving a math question to defeat it!", 213, 365, 'WHITE', 's')
        self.back()
        self.next()
        self.dw_skip = True
        self.ran_b4 = True

    def screen_8(self):
        self.screen.fill('BLACK')
        self.input_box_rect = self.input_box.get_rect()
        self.input_box_rect.topleft = (90, 170)
        self.display_text_animation(f'{self.number1} + {self.number2} = ?', 90, 80, 'WHITE', 'h')
        self.addition_answer = self.big_font.render(f'{self.player_name}', True, (0, 0, 0))
        self.screen.blit(self.input_box, (90, 230))
        self.screen.blit(self.addition_answer, (100, 250))
        self.remind = self.small_font.render('Press [Enter] to submit answer', True, (255, 255, 255))
        self.screen.blit(self.remind, (90, 180))
        self.correct_answer = self.number1 + self.number2
        self.dw_skip = True
        self.ran_b4 = True

    def screen_crt(self):
        self.screen.fill('BLACK')
        self.display_text_animation('Correct!', 250, 235, 'WHITE', 'h')
        self.display_text_animation('V', 750, 235, 'GREEN', 'h')
        self.dw_skip = True
        self.ran_b4 = True

    def screen_wrg(self):
        self.screen.fill('BLACK')
        self.display_text_animation('Wrong!', 300, 235, 'WHITE', 'h')
        self.display_text_animation('x', 700, 235, 'RED', 'h')
        self.dw_skip = True
        self.ran_b4 = True

    def screen_8_crt(self):
        if not self.dw_skip:
            self.screen_8_skip = True
        self.screen.fill('BLACK')
        self.reminders()
        self.screen.blit(self.robot1, (10, 85))
        self.screen.blit(self.text_box, (0, 350))
        self.display_text_animation('robot:', 53, 360, 'RED', 'b')
        self.display_text_animation('correct! Now, upon getting a question ', 213, 365, 'WHITE', 's')
        self.display_text_animation('correct, a certain power will be channelled ', 213, 390, 'WHITE', 's')
        self.display_text_animation('to you in order to defeat the enemy, try it! ', 213, 415, 'WHITE', 's')
        if self.screen_8_skip:
            self.dw_skip = False
        else:
            self.dw_skip = True
        self.display_text_animation('Note: You will also receive some points along the ', 53, 450, 'BLUE', 's')
        self.display_text_animation('way, but be careful though because getting', 156, 475, 'BLUE', 's')
        self.display_text_animation('the question wrong, might cost you', 156, 500, 'BLUE', 's')
        self.next()
        self.dw_skip = True
        self.ran_b4 = True

    def alien_defeat(self, type):
        self.screen.fill('BLACK')
        self.reminders()
        if type == 'green':
            self.screen.blit(self.alien_green_defeated, (750, 35))
        elif type == 'blue':
            self.screen.blit(self.alien_blue_defeated, (750, 35))
        elif type == 'purple':
            self.screen.blit(self.alien_purple_defeated, (750, 35))
        elif type == 'pink':
            self.screen.blit(self.alien_pink_defeated, (750, 35))
        elif type == 'orange':
            self.screen.blit(self.alien_orange_defeated, (750, 35))
        elif type == 'yellow':
            self.screen.blit(self.alien_yellow_defeated, (750, 35))
        elif type == 'scientist':
            self.screen.blit(self.alien_scientist_defeated, (750, 35))
        elif type == 'cloak':
            self.screen.blit(self.cloak_barry_defeated, (610, 35))
        elif type == 'barry':
            self.screen.blit(self.real_barry_defeated, (750, 35))
        self.display_text_animation('enemy', 220, 200, 'RED', 'h')
        self.display_text_animation('defeated! ', 130, 300, 'RED', 'h')
        self.next()
        self.dw_skip = True
        self.ran_b4 = True

    def screen_8_wrg(self):
        self.screen.fill('BLACK')
        self.reminders()
        self.screen.blit(self.robot1, (10, 85))
        self.screen.blit(self.text_box, (0, 350))
        self.display_text_animation('robot:', 53, 360, 'RED', 'b')
        self.display_text_animation('Sorry, your answer was wrong.. Please ', 213, 365, 'WHITE', 's')
        self.display_text_animation('try again!', 213, 400, 'WHITE', 's')
        self.next()
        self.dw_skip = True
        self.ran_b4 = True

    def screen_9(self):
        self.screen.fill('BLACK')
        self.reminders()
        self.screen.blit(self.robot1, (10, 85))
        self.screen.blit(self.text_box, (0, 350))
        self.display_text_animation('robot:', 53, 360, 'RED', 'b')
        self.display_text_animation("There you go! And that's how you defeat", 213, 365, 'WHITE', 's')
        self.display_text_animation('these aliens and save your fellow', 213, 400, 'WHITE', 's')
        self.display_text_animation('astronauts, let begin the real game, shall ', 213, 435, 'WHITE', 's')
        self.display_text_animation('we? ', 213, 470, 'WHITE', 's')
        self.back()
        self.next()
        self.dw_skip = True
        self.ran_b4 = True

    def final_boss_1(self):
        self.screen.fill('BLACK')
        self.reminders()
        self.screen.blit(self.robot1, (10, 85))
        self.screen.blit(self.text_box, (0, 350))
        self.display_text_animation('robot:', 53, 360, 'RED', 'b')
        self.display_text_animation('Here we are, the final boss.. ', 213, 365, 'WHITE', 's')
        self.next()
        self.dw_skip = True
        self.ran_b4 = True

    def final_boss_2(self):
        self.screen.fill('BLACK')
        self.reminders()
        self.screen.blit(self.robot1, (10, 85))
        self.screen.blit(self.cloak, (620, 35))
        self.screen.blit(self.text_box, (0, 350))
        self.display_text_animation('???:', 53, 360, 'DARK GREEN', 'b')
        self.display_text_animation('you dare interfere with my plan?! you shall ', 153, 365, 'WHITE', 's')
        self.display_text_animation('cease to exist!', 153, 400, 'WHITE', 's')
        self.next()
        self.dw_skip = True
        self.ran_b4 = True

    def final_boss_reveal_1(self):
        self.screen.fill('BLACK')
        self.reminders()
        self.screen.blit(self.cloak_defeated, (620, 35))
        self.screen.blit(self.text_box, (0, 350))
        self.display_text_animation('???:', 53, 360, 'DARK GREEN', 'b')
        self.display_text_animation('aarrhh!...', 153, 365, 'WHITE', 's')
        self.next()
        self.dw_skip = True
        self.ran_b4 = True

    def final_boss_reveal_2(self):
        self.screen.fill('BLACK')
        self.reminders()
        self.screen.blit(self.robot_angry, (10, 85))
        self.screen.blit(self.text_box, (0, 350))
        self.display_text_animation('robot:', 53, 360, 'RED', 'b')
        self.display_text_animation("now lets see who's the real one behind all ", 213, 365, 'WHITE', 's')
        self.display_text_animation("of this! ", 213, 400, 'WHITE', 's')
        self.next()
        self.dw_skip = True
        self.ran_b4 = True

    def final_boss_reveal_3(self):
        self.screen.fill('BLACK')
        self.reminders()
        self.screen.blit(self.robot1, (10, 85))
        self.screen.blit(self.barry, (720, 35))
        self.screen.blit(self.text_box, (0, 350))
        self.display_text_animation('robot:', 53, 360, 'RED', 'b')
        self.display_text_animation("barry?! but why??", 213, 365, 'WHITE', 's')
        self.next()
        self.dw_skip = True
        self.ran_b4 = True

    def final_boss_reveal_4(self, player_name):
        self.screen.fill('BLACK')
        self.reminders()
        self.screen.blit(self.barry, (720, 35))
        self.screen.blit(self.text_box, (0, 350))
        self.display_text_animation('barry:', 53, 360, 'BLUE', 'b')
        self.display_text_animation("sigh...because i always hated humanity! so i", 213, 365, 'WHITE', 's')
        self.display_text_animation('mind controlled these aliens to be part of ', 213, 390, 'WHITE', 's')
        self.display_text_animation('my master plan,and i wont stop until all', 213, 415, 'WHITE', 's')
        self.display_text_animation(f'is eliminated!! {player_name}, despite you', 213, 440, 'WHITE', 's')
        self.display_text_animation("being my only true friend, you're still in", 213, 465, 'WHITE', 's')
        self.display_text_animation('my way. and so, ill eliminate all humanity ', 213, 490, 'WHITE','s')
        self.display_text_animation('starting with you! ', 213, 515, 'WHITE', 's')
        self.next()
        self.dw_skip = True
        self.ran_b4 = True

    def final_boss_defeated(self):
        self.screen.fill('BLACK')
        self.reminders()
        self.screen.blit(self.barry_defeated, (610, 35))
        self.screen.blit(self.text_box, (0, 350))
        self.display_text_animation('barry:', 53, 360, 'BLUE', 'b')
        self.display_text_animation("i.. am.. defeated.. ", 213, 365, 'WHITE', 's')
        self.next()
        self.dw_skip = True
        self.ran_b4 = True

    def final_boss_defeated_2(self):
        self.screen.fill('BLACK')
        self.reminders()
        self.screen.blit(self.barry_defeated, (610, 35))
        self.screen.blit(self.text_box, (0, 350))
        self.display_text_animation('barry:', 53, 360, 'BLUE', 'b')
        self.display_text_animation("now that you know what im capable", 213, 365, 'WHITE', 's')
        self.display_text_animation('of, solve this final math question', 213, 400, 'WHITE', 's')
        self.display_text_animation('and perish me.. while you still can...', 213, 435, 'WHITE', 's')
        self.display_text_animation('you: ', 194, 482, 'YELLOW', 'b')
        self.screen.blit(self.deny_button, (542, 480))
        self.deny_button_rect = self.deny_button.get_rect()
        self.deny_button_rect.topleft = (542, 480)
        self.screen.blit(self.accept_button, (300, 480))
        self.accept_button_rect = self.accept_button.get_rect()
        self.accept_button_rect.topleft = (300, 480)
        pygame.display.update()
        self.dw_skip = True
        self.ran_b4 = True

    def final_boss_defeated_deny(self):
        self.screen.fill('BLACK')
        self.reminders()
        self.screen.blit(self.barry_defeated, (610, 35))
        self.screen.blit(self.text_box, (0, 350))
        self.display_text_animation('barry:', 53, 360, 'BLUE', 'b')
        self.display_text_animation("what foolishness, even after what ive", 213, 365, 'WHITE', 's')
        self.display_text_animation('brought apon you, yet you still do not', 213, 400, 'WHITE', 's')
        self.display_text_animation('have the will to finish me?! heh..', 213, 435, 'WHITE', 's')
        self.display_text_animation('heh.. goodbye old friend..aaaahahaa..', 213, 470, 'WHITE', 's')
        self.next()
        self.dw_skip = True
        self.ran_b4 = True

    def final_boss_defeated_accept(self):
        self.screen.fill('BLACK')
        self.reminders()
        self.screen.blit(self.barry_defeated, (610, 35))
        self.screen.blit(self.text_box, (0, 350))
        self.display_text_animation('barry:', 53, 360, 'BLUE', 'b')
        self.display_text_animation("what foolishness, even after what ive", 213, 365, 'WHITE', 's')
        self.display_text_animation('brought apon you, yet you still do not', 213, 400, 'WHITE', 's')
        self.display_text_animation('have the will to finish me?! heh..', 213, 435, 'WHITE', 's')
        self.display_text_animation('heh.. goodbye old friend..aaaahahaa..', 213, 470, 'WHITE', 's')
        self.next()
        self.dw_skip = True
        self.ran_b4 = True

    def final_boss_defeated_accept_crt(self):
        self.screen.fill('BLACK')
        self.reminders()
        self.screen.blit(self.barry_defeated, (610, 35))
        self.screen.blit(self.text_box, (0, 350))
        self.display_text_animation('barry:', 53, 360, 'BLUE', 'b')
        self.display_text_animation("i knew you'd would've done it, so long..", 213, 365, 'WHITE', 's')
        self.display_text_animation("old friend..aaaahahaa..", 213, 400, 'WHITE', 's')
        self.next()
        self.dw_skip = True
        self.ran_b4 = True

    def final_boss_defeated_accept_wrg(self, answer):
        self.screen.fill('BLACK')
        self.reminders()
        self.screen.blit(self.barry_defeated, (610, 35))
        self.screen.blit(self.text_box, (0, 350))
        self.display_text_animation('barry:', 53, 360, 'BLUE', 'b')
        self.display_text_animation(f"the answer was {answer}. you purposely got it", 213, 365,
                                    'WHITE', 's')
        self.display_text_animation("incorrect to offer me a second chance..", 213, 400, 'WHITE', 's')
        self.display_text_animation('but i am not accepting it.. so long.. old', 213, 435, 'WHITE', 's')
        self.display_text_animation('friend..aaaahahaa.. ', 213, 470, 'WHITE', 's')
        self.next()
        self.dw_skip = True
        self.ran_b4 = True

    def grave_barry(self):
        self.screen.blit(self.rip_barry, (0, 0))
        self.reminders()
        self.next()

    def ending_screen(self):
        self.screen.fill('BLACK')
        self.screen.blit(self.peace_image, (0, 0))
        self.screen.blit(self.small_text_box, (150, 10))
        self.display_text_animation('robot:', 303, 60, 'RED', 'b')
        self.display_text_animation('and so the aliens were free from', 460, 60, 'WHITE', 'ss')
        self.display_text_animation('the mind control and they lived', 460, 80, 'WHITE', 'ss')
        self.display_text_animation('peacefully with the astronauts.', 460, 100, 'WHITE', 'ss')
        self.next()
        self.dw_skip = True
        self.ran_b4 = True

    def ending_screen_2(self):
        self.screen.fill('BLACK')
        self.display_text_animation('THE END', 330, 270, 'WHITE', 'h')
        self.dw_skip = True
        self.ran_b4 = True

    def ending_screen_3(self):
        self.screen.fill('BLACK')
        self.reminders()
        self.screen.blit(self.robot1, (10, 85))
        self.screen.blit(self.text_box, (0, 350))
        self.display_text_animation('robot:', 53, 360, 'RED', 'b')
        self.display_text_animation("Fantastic job! you've beaten the game!", 213, 365, 'WHITE', 's')
        self.display_text_animation("now you are free to explore the game", 213, 400, 'WHITE', 's')
        self.display_text_animation("however you like! Have fun and enjoy!", 213, 435, 'WHITE', 's')
        self.display_text_animation("(you will also receive infinite lives)", 213, 470, 'BLUE', 's')
        self.next()
        self.dw_skip = True
        self.ran_b4 = True

    def explain_level_menu(self):
        self.screen.blit(self.robot_hand1, (10, 85))
        self.screen.blit(self.text_box, (0, 350))
        self.display_text_animation('robot:', 53, 360, 'RED', 'b')
        self.display_text_animation("You will receive 5 lives throughout this ", 213, 365, 'WHITE', 's')
        self.display_text_animation('entire game. However, if you lose in any', 213, 400, 'WHITE', 's')
        self.display_text_animation('level, you will lose a life, lose all of them ', 213, 435, 'WHITE', 's')
        self.display_text_animation('and its game over, so be careful! ', 213, 470, 'WHITE', 's')
        self.next()
        self.dw_skip = True
        self.ran_b4 = True

    def explain_level_menu_2(self):
        self.screen.blit(self.robot1, (10, 85))
        if not self.ran4:
            self.screen.blit(self.semi_trans_pause, (0, 0))
            self.ran4 = True
        self.screen.blit(self.text_box, (0, 350))
        self.display_text_animation('robot:', 53, 360, 'RED', 'b')
        self.display_text_animation('This is the pause button, use it when you', 213, 365, 'WHITE', 's')
        self.display_text_animation('want to stop or resume the music and', 213, 400, 'WHITE', 's')
        self.display_text_animation('sound effects or return to home screen', 213, 435, 'WHITE', 's')
        self.next()
        self.dw_skip = True
        self.ran_b4 = True

    def explain_level_menu_3(self):
        self.screen.blit(self.small_text_box, (150, 10))
        self.display_text_animation('robot:', 303, 60, 'RED', 'b')
        self.display_text_animation('This will be your character, use', 460, 60, 'WHITE', 'ss')
        self.display_text_animation('the left, right, up and down keys', 460, 80, 'WHITE', 'ss')
        self.display_text_animation('to move around!', 460, 100, 'WHITE', 'ss')
        self.next()
        self.dw_skip = True
        self.ran_b4 = True

    def explain_level_menu_4(self):
        self.screen.blit(self.small_text_box, (150, 10))
        self.display_text_animation('robot:', 303, 60, 'RED', 'b')
        self.display_text_animation("to enter levels, get your character", 455, 60, 'WHITE', 'ss')
        self.display_text_animation('to be standing on the desired', 455, 80, 'WHITE', 'ss')
        self.display_text_animation('level and press [Enter] to enter it', 455, 100, 'WHITE', 'ss')
        self.next()
        self.dw_skip = True
        self.ran_b4 = True

    def explain_level_menu_5(self):
        self.screen.blit(self.small_text_box, (150, 10))
        self.display_text_animation('robot:', 303, 60, 'RED', 'b')
        self.display_text_animation("good luck and", 455, 60, 'WHITE', 's')
        self.display_text_animation('have fun!', 455, 90, 'WHITE', 's')
        self.next()
        self.dw_skip = True
        self.ran_b4 = True

    def crt_screen2(self):
        self.screen.fill('BLACK')
        self.reminders()
        self.display_text_animation('Correct!', 250, 235, 'WHITE', 'h')
        self.display_text_animation('V', 750, 235, 'GREEN', 'h')
        self.display_text_animation('you can now advance to the next level!', 150, 335, 'DARK GREEN', 's')
        self.dw_skip = True
        self.ran_b4 = True

    def crt_screen3(self):
        self.screen.fill('BLACK')
        self.reminders()
        self.display_text_animation('Correct!', 250, 235, 'WHITE', 'h')
        self.display_text_animation('V', 750, 235, 'GREEN', 'h')
        self.dw_skip = True
        self.ran_b4 = True

    def wrg_screen2(self):
        self.screen.fill('BLACK')
        self.reminders()
        self.display_text_animation('Wrong!', 300, 235, 'WHITE', 'h')
        self.display_text_animation('x', 700, 235, 'RED', 'h')
        self.display_text_animation("you lose a life :(", 380, 335, 'DARK RED', 's')
        self.dw_skip = True
        self.ran_b4 = True

    def game_over(self):
        self.screen.fill('BLACK')
        self.reminders()
        self.display_text_animation('game over', 250, 235, 'RED', 'h')
        self.display_text_animation("you will have to start all over from the beginning!", 63, 335, 'DARK RED', 's')
        self.dw_skip = True
        self.ran_b4 = True






