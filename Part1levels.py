import pygame as pyg
import random
from Part2storyline import Screens
storyline = Screens()

class Manager(object):
    def __init__(self):
        pyg.init()
        self.running = True
        self.x = 1080
        self.y = 600
        self.point = 5
        self.level = 1
        self.level_now = 1
        self.answer_type = False
        self.enterlevel = False
        self.player_answer = ""
        self.player_name = ''
        self.enemy_type = 'green'
        self.clock = pyg.time.Clock()
        self.screen = pyg.display.set_mode([self.x, self.y])
        # picture for main menu
        self.start = pyg.image.load("Buttons/ButtonStart.png")
        self.logo = pyg.image.load("OtherPictures&Screen/MathQuestLogo.png")
        # picture for level menu
        self.level_menu = pyg.image.load("OtherPictures&Screen/LevelMenu.png")
        self.heart_box = pyg.image.load("OtherPictures&Screen/HeartBox.png")
        self.heart1 = pyg.image.load("OtherPictures&Screen/Heart.png")
        self.heart0 = pyg.image.load("OtherPictures&Screen/HeartEmpty.png")
        self.word = pyg.font.Font("slkscr.ttf", 40)
        self.player_textbox = pyg.image.load("OtherPictures&Screen/player_answer_textbox.png")
        #picture for level on and off
        self.level1 = pyg.image.load("LevelButtons(1-10)/level 1.png")
        self.level2 = pyg.image.load("LevelButtons(1-10)/level 2.png")
        self.level3 = pyg.image.load("LevelButtons(1-10)/level 3.png")
        self.level4 = pyg.image.load("LevelButtons(1-10)/level 4.png")
        self.level5 = pyg.image.load("LevelButtons(1-10)/level 5.png")
        self.level6 = pyg.image.load("LevelButtons(1-10)/level 6.png")
        self.level7 = pyg.image.load("LevelButtons(1-10)/level 7.png")
        self.level8 = pyg.image.load("LevelButtons(1-10)/level 8.png")
        self.level9 = pyg.image.load("LevelButtons(1-10)/level 9.png")
        self.level10 = pyg.image.load("LevelButtons(1-10)/level 10.png")
        self.level1_0 = pyg.image.load("LevelButtons(1-10)/level 1 grey.png")
        self.level2_0 = pyg.image.load("LevelButtons(1-10)/level 2 grey.png")
        self.level3_0 = pyg.image.load("LevelButtons(1-10)/level 3 grey.png")
        self.level4_0 = pyg.image.load("LevelButtons(1-10)/level 4 grey.png")
        self.level5_0 = pyg.image.load("LevelButtons(1-10)/level 5 grey.png")
        self.level6_0 = pyg.image.load("LevelButtons(1-10)/level 6 grey.png")
        self.level7_0 = pyg.image.load("LevelButtons(1-10)/level 7 grey.png")
        self.level8_0 = pyg.image.load("LevelButtons(1-10)/level 8 grey.png")
        self.level9_0 = pyg.image.load("LevelButtons(1-10)/level 9 grey.png")
        self.level10_0 = pyg.image.load("LevelButtons(1-10)/level 10 grey.png")
        self.leveltextbox = pyg.image.load("Picture/TextBox.png")
        self.alienPink = pyg.image.load("Picture/AlienPink.png")
        self.alienGreen = pyg.image.load("Picture/AlienGreen.png")
        self.alienGreen_Scientist = pyg.image.load("Picture/AlienGreen_Scientist.png")
        self.alienBlue = pyg.image.load("Picture/AlienBlue.png")
        self.alienPurple = pyg.image.load("Picture/AlienPurple.png")
        self.alienYellow = pyg.image.load("Picture/AlienYellow.png")
        self.alienOrange = pyg.image.load("Picture/AlienOrange.png")
        self.barryCloak = pyg.image.load("Picture/BarryCloak.png")
        self.alienGreen_Scientist0 = pyg.image.load("Picture/Defeated_AlienGreen_Scientist.png")
        self.barryCloak0 = pyg.image.load("Picture/BarryCloak_defeated.png")
        self.barryReal0 = pyg.image.load("Picture/BarryReal_defeated.png")
        self.alienPink_sprite = pyg.image.load("Picture/Sprite_AlienPink.png")
        self.alienGreen_sprite = pyg.image.load("Picture/Sprite_AlienGreen.png")
        self.alienGreen_Scientist_sprite = pyg.image.load("Picture/Sprite_AlienGreen_Scientist.png")
        self.alienBlue_sprite = pyg.image.load("Picture/Sprite_AlienBlue.png")
        self.alienPurple_sprite = pyg.image.load("Picture/Sprite_AlienPurple.png")
        self.alienYellow_sprite = pyg.image.load("Picture/Sprite_AlienYellow.png")
        self.alienOrange_sprite = pyg.image.load("Picture/Sprite_AlienOrange.png")
        self.alienBlack_sprite = pyg.image.load("Picture/Sprite_AlienBlack.png")
        self.barryReal = pyg.image.load("Picture/BarryReal.png")
        # picture for setting
        self.semi_trans = pyg.image.load("OtherPictures&Screen/Background_SemiTransparent.png")
        self.semi_trans_player = pyg.image.load("OtherPictures&Screen/semiTransparent_player.png")
        self.setting = pyg.image.load("Buttons/ButtonSettings.png")
        self.setting_windows = pyg.image.load("OtherPictures&Screen/ScreenSettings.png")
        self.quit_setting = pyg.image.load("Buttons/ButtonQuit_settings.png")
        self.continue_setting = pyg.image.load("Buttons/ButtonContinue_settings.png")
        self.erase_setting = pyg.image.load("Buttons/ButtonEraseGameData.png")
        # picture for quit
        self.warning = pyg.image.load("OtherPictures&Screen/ScreenQuit.png")
        self.quit = pyg.image.load("Buttons/ButtonQuit_ScreenQuit.png")
        self.cancel = pyg.image.load("Buttons/ButtonCancel.png")
        # picture for pause
        self.continue_button = pyg.image.load("Buttons/ButtonContinue.png")
        self.pause = pyg.image.load("Buttons/ButtonPause.png")
        self.pause_screen = pyg.image.load("OtherPictures&Screen/ScreenPaused_big.png")
        self.pause_screen_for_menu = pyg.image.load("OtherPictures&Screen/ScreenPaused_big2.png")
        self.back = pyg.image.load("Buttons/ButtonBack.png")
        self.back_to_main = pyg.image.load("Buttons/ButtonReturnToHomeScreen.png")
        # picture for music icon
        self.music_button_on = pyg.image.load("Buttons/ButtonMusic.png")
        self.music_button_off = pyg.image.load("Buttons/ButtonMusic_off.png")
        self.music_button = pyg.image.load('Buttons/ButtonMusic_off.png')
        self.exit_button = pyg.image.load('Buttons/ButtonExit_ScreenPaused.png')
        self.soundE_button = pyg.image.load('Buttons/ButtonSoundEffects_off.png')
        self.soundE_button_on = pyg.image.load('Buttons/ButtonSoundEffects_on.png')
        self.soundE_button_off = pyg.image.load('Buttons/ButtonSoundEffects_off.png')
        self.music = pyg.mixer.music.load('Music/music.wav')
        self.button_sound = pyg.mixer.Sound('Music/button_sound.wav')
        self.music_playing = False
        self.soundE_playing = False
        self.LEFT_KEY, self.RIGHT_KEY, self.UP_KEY, self.DOWN_KEY, self.FACING_FRONT, self.FACING_LEFT, \
            self.FACING_RIGHT, self.FACING_BACK = False, False, False, False, False, False, False, False
        self.load_frames()
        self.rect = self.idle_frames_front[0].get_rect()
        self.rect.midbottom = (240, 244)
        self.current_frame = 0
        self.last_updated = 0
        self.playerX = 0
        self.playerY = 0
        self.state = 'idle'
        self.current_image = self.idle_frames_front[0]
        self.ran = False
        self.ran2 = False
        self.ran3 = False
        self.ran4 = False
        self.ran5 = False
        self.ran6 = False
        self.ran_defeat_screen = False
        self.ran_game_over = False
        self.ran_crt_wrg = False
        self.storyline = False
        self.storyline_barry = False
        self.storyline_cloak = False
        self.stop = False
        self.stop_barry = False
        self.stop_en = False
        self.stop_barry_2 = False
        self.defeat_level10 = False
        self.finish_game = False
        self.lost_in_barryr = False
        self.game_finished = False

    def buttons(self):
        storyline.back_button_rect = storyline.back_button.get_rect()
        storyline.back_button_rect.topleft = (10, 530)
        storyline.next_button_rect = storyline.next_button.get_rect()
        storyline.next_button_rect.topleft = (822, 530)
        storyline.deny_button_rect = storyline.deny_button.get_rect()
        storyline.deny_button_rect.topleft = (542, 480)
        storyline.accept_button_rect = storyline.accept_button.get_rect()
        storyline.accept_button_rect.topleft = (300, 480)

    def randomNum(self):
        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)
        self.num3 = random.randint(1, 100)
        self.num4 = random.randint(1, 100)
        self.num5 = random.randint(1, 1000)
        self.num6 = random.randint(1, 1000)

    def music_icon(self, screen):
        if screen == 'settings_screen':
            self.screen.blit(self.music_button, (551, 410))
            self.music_button_rect = self.music_button.get_rect()
            self.music_button_rect.topleft = (551, 410)
        elif screen == 'pause_screen':
            self.screen.blit(self.music_button, (551, 370))
            self.music_button_rect = self.music_button.get_rect()
            self.music_button_rect.topleft = (551, 370)

    def sound_effects_icon(self, screen):
        if screen == 'settings_screen':
            self.screen.blit(self.soundE_button, (455, 410))
            self.soundE_button_rect = self.soundE_button.get_rect()
            self.soundE_button_rect.topleft = (455, 410)
        elif screen == 'pause_screen':
            self.screen.blit(self.soundE_button, (455, 370))
            self.soundE_button_rect = self.soundE_button.get_rect()
            self.soundE_button_rect.topleft = (455, 370)

    def sound_effects_player(self):
        if self.soundE_playing:
            self.button_sound.play()

    def quitScreen(self):
        self.mainMenu()
        self.quit_rect = self.quit.get_rect()
        self.cancel_rect = self.cancel.get_rect()
        self.quit_rect.topleft = (self.x / 2 - 458 / 2 + 20, self.y / 2 + 275 / 2 - 79)
        self.cancel_rect.topleft = (self.x/2 - 458 / 2 + 20 + 202 + 20, self.y/ 2 + 275 / 2 - 79)
        self.screen.blit(self.semi_trans, (0, 0))
        self.screen.blit(self.warning, (self.x/2 - 458/2, self.y/2 - 275/2))
        self.screen.blit(self.quit, (self.x / 2 - 458 / 2 + 20, self.y / 2 + 275 / 2 - 79))
        self.screen.blit(self.cancel, (self.x/2 - 458 / 2 + 20 + 202 + 20, self.y/ 2 + 275 / 2 - 79))

    def settingScreen(self):
        self.mainMenu()
        self.screen.blit(self.semi_trans, (0, 0))
        self.erase_setting_rect = self.erase_setting.get_rect()
        self.erase_setting_rect.topleft = (self.x / 2 - 401/2, self.y / 2 + 461/2 - (20 + (32*2))*3 + 35)
        self.quit_setting_rect = self.quit_setting.get_rect()
        self.quit_setting_rect.topleft = (self.x / 2 - 401/2, self.y / 2 + 461/2 - (20 + (32*2))*4 + 45)
        self.continue_button_rect = self.continue_setting.get_rect()
        self.continue_button_rect.topleft = (self.x / 2 - 401 / 2, self.y / 2 + 461 / 2 - (20 + (32 * 2)) * 5 + 55)
        self.screen.blit(self.setting_windows, (self.x/2 - 445/2, self.y/2 - 461/2))
        self.screen.blit(self.quit_setting, (self.x / 2 - 401/2, self.y / 2 + 461/2 - (20 + (32*2))*4 + 45))
        self.screen.blit(self.continue_setting, (self.x / 2 - 401/2, self.y / 2 + 461/2 - (20 + (32*2))*5 + 55))
        self.screen.blit(self.erase_setting, (self.x / 2 - 401/2, self.y / 2 + 461/2 - (20 + (32*2))*3 + 35))
        self.music_icon('settings_screen')
        self.sound_effects_icon('settings_screen')

    def pauseButton(self):
        self.pause_rect = pyg.rect.Rect(self.x - 74, 20, 48, 56)
        self.screen.blit(self.pause, (self.x - 74, 20))

    def pauseScreenForMenu(self):
        if not self.ran:
            self.screen.blit(self.semi_trans, (0, 0))
            self.ran = True
        self.back_rect = self.back.get_rect()
        self.back_rect.topleft = (self.x / 2 - 248 / 2, 218)
        self.back_to_main_rect = self.back_to_main.get_rect()
        self.back_to_main_rect.topleft = (self.x / 2 - 361 / 2 + 18, 278)
        self.screen.blit(self.pause_screen_for_menu, (self.x / 2 - 418 / 2, 145))
        self.screen.blit(self.back, (self.x / 2 - 248 / 2, 218))
        self.screen.blit(self.back_to_main, (self.x / 2 - 361 / 2 + 18, 278))
        self.music_icon('pause_screen')
        self.sound_effects_icon('pause_screen')

    def pauseScreenForLevel(self):
        self.screen.blit(self.level_menu, (0, 0))
        self.screen.blit(self.semi_trans, (0, 0))
        self.exit_button_rect = self.exit_button.get_rect()
        self.exit_button_rect.topleft = (self.x / 2 - 248 / 2, 265)
        self.continue_button_rect = self.continue_button.get_rect()
        self.continue_button_rect.topleft = (self.x / 2 - 248 / 2, 324)
        self.screen.blit(self.pause_screen, (self.x / 2 - 418 / 2, 600 / 2 - 300 / 2))
        self.screen.blit(self.exit_button, (self.x / 2 - 248 / 2, 245))
        self.screen.blit(self.continue_button, (self.x / 2 - 248 / 2, 309))
        self.music_icon('pause_screen')
        self.sound_effects_icon('pause_screen')


    def load_frames(self):
        front_stand = pyg.image.load('Picture/Sprite_Astronaut_FrontStand.png')
        front_stand2 = pyg.image.load('Picture/Sprite_Astronaut_FrontStand2.png')
        front_walk1 = pyg.image.load('Picture/Sprite_Astronaut_FrontWalk1.png')
        front_walk2 = pyg.image.load('Picture/Sprite_Astronaut_FrontWalk2.png')
        left_stand = pyg.image.load('Picture/Sprite_Astronaut_LeftStand.png')
        left_stand2 = pyg.image.load('Picture/Sprite_Astronaut_LeftStand2.png')
        left_walk1 = pyg.image.load('Picture/Sprite_Astronaut_LeftWalk1.png')
        left_walk2 = pyg.image.load('Picture/Sprite_Astronaut_LeftWalk2.png')
        right_stand = pyg.image.load('Picture/Sprite_Astronaut_RightStand.png')
        right_stand2 = pyg.image.load('Picture/Sprite_Astronaut_RightStand2.png')
        right_walk1 = pyg.image.load('Picture/Sprite_Astronaut_RightWalk1.png')
        right_walk2 = pyg.image.load('Picture/Sprite_Astronaut_RightWalk2.png')
        back_stand = pyg.image.load('Picture/Sprite_Astronaut_BackStand.png')
        back_stand2 = pyg.image.load('Picture/Sprite_Astronaut_BackStand2.png')
        back_walk1 = pyg.image.load('Picture/Sprite_Astronaut_BackWalk1.png')
        back_walk2 = pyg.image.load('Picture/Sprite_astronaut_BackWalk2.png')
        self.idle_frames_front = [front_stand, front_stand2]
        self.walking_frames_front = [front_walk1, front_stand, front_walk2]
        self.idle_frames_left = [left_stand, left_stand2]
        self.walking_frames_left = [left_walk1, left_stand, left_walk2]
        self.idle_frames_right = [right_stand, right_stand2]
        self.walking_frames_right = [right_walk1, right_stand, right_walk2]
        self.idle_frames_back = [back_stand, back_stand2]
        self.walking_frames_back = [back_walk1, back_stand, back_walk2]

    def set_state(self):
        self.state = 'idle'
        if self.playerX > 0:
            self.state = 'moving right'
        elif self.playerX < 0:
            self.state = 'moving left'
        elif self.playerY > 0:
            self.state = 'moving up'
        elif self.playerY < 0:
            self.state = 'moving down'

    def animate(self):
        now = pyg.time.get_ticks()
        if self.state == 'idle':
            if now - self.last_updated > 200:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.idle_frames_front)
                if self.FACING_LEFT:
                    self.current_image = self.idle_frames_left[self.current_frame]
                elif self.FACING_RIGHT:
                    self.current_image = self.idle_frames_right[self.current_frame]
                elif self.FACING_FRONT:
                    self.current_image = self.idle_frames_front[self.current_frame]
                elif self.FACING_BACK:
                    self.current_image = self.idle_frames_back[self.current_frame]
        else:
            if now - self.last_updated > 100:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.walking_frames_front)
                if self.state == 'moving left':
                    self.current_image = self.walking_frames_left[self.current_frame]
                elif self.state == 'moving right':
                    self.current_image = self.walking_frames_right[self.current_frame]
                elif self.state == 'moving up':
                    self.current_image = self.walking_frames_front[self.current_frame]
                elif self.state == 'moving down':
                    self.current_image = self.walking_frames_back[self.current_frame]

    def update(self):
        self.playerX = 0
        self.playerY = 0
        if self.LEFT_KEY:
            self.playerX = -2
        elif self.RIGHT_KEY:
            self.playerX = 2
        elif self.DOWN_KEY:
            self.playerY = 2
        elif self.UP_KEY:
            self.playerY = -2
        self.rect.x += self.playerX
        self.rect.y += self.playerY
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= 1058:
            self.rect.x = 1058
        elif self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= 568:
            self.rect.y = 568
        self.set_state()
        self.animate()

    def mainMenu(self):
        self.screen.fill("BLACK")
        self.setting_rect = pyg.rect.Rect(self.x - 74, 20, 55, 55)
        self.screen.blit(self.setting, (self.x - 74, 20))
        self.start_rect = self.start.get_rect()
        self.start_rect.topleft = (self.x/2 - 248/2, self.y/2)
        self.screen.blit(self.logo, (self.x / 2 - 589 / 2, 20))
        self.screen.blit(self.start, (self.x/2 - 248/2, self.y/2))

    def levelMenu(self):
        self.screen.blit(self.level_menu, (0, 0))
        self.pauseButton()
        self.screen.blit(self.heart_box, (1080/2 - 323/2, 2))
        self.heart_y = 17
        self.heart_x = (1080/2 - 323/2) + 17
        if self.point == 5:
            self.screen.blit(self.heart1, (self.heart_x, self.heart_y))
            self.screen.blit(self.heart1, (self.heart_x + (55+5), self.heart_y))
            self.screen.blit(self.heart1, (self.heart_x + (55+5)*2, self.heart_y))
            self.screen.blit(self.heart1, (self.heart_x + (55+5)*3, self.heart_y))
            self.screen.blit(self.heart1, (self.heart_x + (55+5)*4, self.heart_y))
        elif self.point == 4:
            self.screen.blit(self.heart1, (self.heart_x, self.heart_y))
            self.screen.blit(self.heart1, (self.heart_x + (55 + 5), self.heart_y))
            self.screen.blit(self.heart1, (self.heart_x + (55 + 5) * 2, self.heart_y))
            self.screen.blit(self.heart1, (self.heart_x + (55 + 5) * 3, self.heart_y))
            self.screen.blit(self.heart0, (self.heart_x + (55 + 5) * 4, self.heart_y))
        elif self.point == 3:
            self.screen.blit(self.heart1, (self.heart_x, self.heart_y))
            self.screen.blit(self.heart1, (self.heart_x + (55 + 5), self.heart_y))
            self.screen.blit(self.heart1, (self.heart_x + (55 + 5) * 2, self.heart_y))
            self.screen.blit(self.heart0, (self.heart_x + (55 + 5) * 3, self.heart_y))
            self.screen.blit(self.heart0, (self.heart_x + (55 + 5) * 4, self.heart_y))
        elif self.point == 2:
            self.screen.blit(self.heart1, (self.heart_x, self.heart_y))
            self.screen.blit(self.heart1, (self.heart_x + (55 + 5), self.heart_y))
            self.screen.blit(self.heart0, (self.heart_x + (55 + 5) * 2, self.heart_y))
            self.screen.blit(self.heart0, (self.heart_x + (55 + 5) * 3, self.heart_y))
            self.screen.blit(self.heart0, (self.heart_x + (55 + 5) * 4, self.heart_y))
        elif self.point == 1:
            self.screen.blit(self.heart1, (self.heart_x, self.heart_y))
            self.screen.blit(self.heart0, (self.heart_x + (55 + 5), self.heart_y))
            self.screen.blit(self.heart0, (self.heart_x + (55 + 5) * 2, self.heart_y))
            self.screen.blit(self.heart0, (self.heart_x + (55 + 5) * 3, self.heart_y))
            self.screen.blit(self.heart0, (self.heart_x + (55 + 5) * 4, self.heart_y))

        self.level1_rect = self.level1.get_rect()
        self.level1_rect.topleft = (166, 298)
        self.screen.blit(self.alienGreen_sprite, (143, 300))
        self.screen.blit(self.level2_0, (224, 348))
        self.screen.blit(self.level3_0, (310, 382))
        self.screen.blit(self.level4_0, (418, 404))
        self.screen.blit(self.level5_0, (517, 411))
        self.screen.blit(self.level6_0, (642, 399))
        self.screen.blit(self.level7_0, (750, 376))
        self.screen.blit(self.level8_0, (825, 336))
        self.screen.blit(self.level9_0, (860, 284))
        self.screen.blit(self.level10_0, (439, 100))

        if self.level > 1:
            self.level2_rect = self.level2.get_rect()
            self.level2_rect.topleft = (224, 348)
            self.screen.blit(self.level2, (224, 348))
            self.screen.blit(self.alienBlue_sprite, (199, 349))

        if self.level > 2:
            self.level3_rect = self.level3.get_rect()
            self.level3_rect.topleft = (310, 382)
            self.screen.blit(self.level3, (310, 382))
            self.screen.blit(self.alienPink_sprite, (285, 385))

        if self.level > 3:
            self.level4_rect = self.level4.get_rect()
            self.level4_rect.topleft = (418, 404)
            self.screen.blit(self.level4, (418, 404))
            self.screen.blit(self.alienYellow_sprite, (397, 408))

        if self.level > 4:
            self.level5_rect = self.level5.get_rect()
            self.level5_rect.topleft = (517, 411)
            self.screen.blit(self.level5, (517, 411))
            self.screen.blit(self.alienPurple_sprite, (498, 416))

        if self.level > 5:
            self.level6_rect = self.level6.get_rect()
            self.level6_rect.topleft = (642, 399)
            self.screen.blit(self.level6, (642, 399))
            self.screen.blit(self.alienGreen_Scientist_sprite, (623, 407))

        if self.level > 6:
            self.level7_rect = self.level7.get_rect()
            self.level7_rect.topleft = (750, 376)
            self.screen.blit(self.level7, (750, 376))
            self.screen.blit(self.alienGreen_sprite, (735, 384))

        if self.level > 7:
            self.level8_rect = self.level8.get_rect()
            self.level8_rect.topleft = (825, 336)
            self.screen.blit(self.level8, (825, 336))
            self.screen.blit(self.alienOrange_sprite, (810, 345))

        if self.level > 8:
            self.level9_rect = self.level9.get_rect()
            self.level9_rect.topleft = (860, 284)
            self.screen.blit(self.level9, (860, 284))
            self.screen.blit(self.alienBlue_sprite, (841, 286))

        if self.level > 9:
            self.level10_rect = self.level10.get_rect()
            self.level10_rect.topleft = (439, 100)
            self.screen.blit(self.level10, (439, 100))
            self.screen.blit(self.alienBlack_sprite, (530, 58))

        self.screen.blit(self.current_image, self.rect)
        pyg.display.update()

    def tutorial_level(self):
        self.screen.fill('BLACK')
        self.remind = storyline.small_font.render('*Press [Enter] to submit answer', True, (255, 255, 255))
        self.screen.blit(self.remind, (90, 70))
        self.screen.blit(self.leveltextbox, (90, 100))
        self.answer = 1 + 1
        self.screen.blit(self.alienGreen, (723, 20))
        self.T_question = storyline.huge_font.render('1 + 1 =', True, (255, 255, 255))
        self.T_player_answer = storyline.huge_font.render(str(self.player_answer), True, (255, 255, 255))
        self.screen.blit(self.T_question, (110, 120))
        self.screen.blit(self.player_textbox, (90, 400))
        self.screen.blit(self.T_player_answer, (110, 460))
        return self.answer

    def chat(self, level_now, fnum, snum, operator):
        alien_color = self.alienGreen
        self.answer_type = True
        if level_now == 1 or level_now == 6:
            alien_color = self.alienGreen
        elif level_now == 2 or level_now == 9:
            alien_color = self.alienBlue
        elif level_now == 3:
            alien_color = self.alienPink
        elif level_now == 4:
            alien_color = self.alienYellow
        elif level_now == 5:
            alien_color = self.alienPurple
        elif level_now == 7:
            alien_color = self.alienGreen_Scientist
        elif level_now == 8:
            alien_color = self.alienOrange
        elif level_now == 10:
            alien_color = self.barryCloak
        elif level_now == 11:
            alien_color = self.barryReal
        elif level_now == 12:
            alien_color = self.barryReal0
        self.answer_type = True
        if operator == "+":
            self.answer = fnum + snum
        elif operator == "-":
            while snum > fnum:
                self.randomNum()
                if level_now == 3:
                    fnum = self.num3
                    snum = self.num1
                elif level_now == 4:
                    fnum = self.num3
                    snum = self.num4
                elif level_now == 6:
                    fnum = self.num5
                    snum = self.num6
            self.answer = fnum - snum
        elif operator == "/":
            while fnum % snum != 0:
                self.randomNum()
                if level_now == 9:
                    fnum = self.num3
                    snum = self.num1
                elif level_now == 8:
                    fnum = self.num3
                    snum = self.num4
                elif level_now == 11:
                    fnum = self.num5
                    snum = self.num2
            self.answer = fnum / snum
        elif operator == "*":
            self.answer = fnum * snum

        self.screen.blit(self.level_menu, (0, 0))
        self.screen.blit(self.semi_trans, (0, 0))
        if level_now < 11:
            self.pauseButton()
        self.remind = storyline.small_font.render('*Press [Enter] to submit answer', True, (255, 255, 255))
        self.screen.blit(self.remind, (90, 70))
        self.screen.blit(self.leveltextbox, (90, 100))
        if level_now == 10:
            self.screen.blit(alien_color, (610, 35))
        else:
            self.screen.blit(alien_color, (723, 20))
        if level_now > 10:
            level_now = 10
        self.T_level = self.word.render("Level" + str(level_now), True, (255, 255, 255))
        if operator == '*':
            operator = 'x'
        self.T_question = storyline.huge_font.render(str(fnum) + str(operator) + str(snum) + "=", True, (255, 255, 255))
        self.T_player_answer = storyline.huge_font.render(str(self.player_answer), True, (255, 255, 255))
        self.screen.blit(self.T_level, (20, 20))
        self.screen.blit(self.T_question, (110, 120))
        self.screen.blit(self.player_textbox, (90, 400))
        self.screen.blit(self.T_player_answer, (110, 460))
        self.current_level = level_now
        return self.answer

    def correctWrong(self, level_now):
        if level_now == 1:
            self.enemy_type = 'green'
        elif level_now == 2:
            self.enemy_type = 'blue'
        elif level_now == 3:
            self.enemy_type = 'pink'
        elif level_now == 4:
            self.enemy_type = 'yellow'
        elif level_now == 5:
            self.enemy_type = 'purple'
        elif level_now == 6:
            self.enemy_type = 'scientist'
        elif level_now == 7:
            self.enemy_type = 'green'
        elif level_now == 8:
            self.enemy_type = 'orange'
        elif level_now == 9:
            self.enemy_type = 'blue'
        elif level_now == 10:
            self.enemy_type = 'cloak'
        if not self.ran_crt_wrg:
            try:
                if int(self.player_answer) == int(self.answer) and not storyline.ran_b4 and level_now == 10:
                    self.T_level = self.word.render("Level" + str(level_now), True, (255, 255, 255))
                    self.screen.blit(self.T_level, (20, 20))
                    storyline.crt_screen3()
                elif int(self.player_answer) != int(self.answer) and not storyline.ran_b4:
                    self.T_level = self.word.render("Level" + str(level_now), True, (255, 255, 255))
                    self.screen.blit(self.T_level, (20, 20))
                    storyline.wrg_screen2()
                else:
                    self.T_level = self.word.render("Level" + str(level_now), True, (255, 255, 255))
                    self.screen.blit(self.T_level, (20, 20))
                    storyline.crt_screen2()
            except ValueError:
                self.display = 'level'
                pass
            self.ran_crt_wrg = True

    def main(self):
        self.buttons()
        self.randomNum()
        self.display = "mainMenu"
        while self.running:
            self.clock.tick(60)
            if self.display == 'levelMenu':
                self.update()
                self.levelMenu()
                pyg.display.update()
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    self.running = False
                if event.type == pyg.KEYDOWN:
                    if event.key == pyg.KMOD_ALT and pyg.K_F4:
                        self.running = False

                if self.display == "mainMenu":
                    self.mainMenu()
                    if event.type == pyg.MOUSEBUTTONDOWN:
                        if self.start_rect.collidepoint(event.pos):
                            self.sound_effects_player()
                            if not self.storyline:
                                while not self.storyline and self.running:
                                    for event in pyg.event.get():
                                        if event.type == pyg.QUIT:
                                            self.running = False
                                        if event.type == pyg.KEYDOWN:
                                            if event.key == pyg.K_TAB:
                                                self.storyline = True
                                                storyline.ran_b4 = False
                                                break
                                            if event.key == pyg.K_RETURN:
                                                if storyline.current_screen == 9:
                                                    self.stop = False
                                                    storyline.ran_b4 = False
                                                    self.player_answer = ''
                                                    storyline.current_screen = 8
                                                elif storyline.current_screen == 2:
                                                    self.stop_en = False
                                                    storyline.ran_b4 = False
                                                    storyline.current_screen = 3
                                                else:
                                                    storyline.current_screen += 1
                                                    if storyline.furthest_screen < storyline.current_screen:
                                                        storyline.furthest_screen = storyline.current_screen
                                                        storyline.ran_b4 = False
                                                    elif storyline.furthest_screen >= storyline.current_screen:
                                                        storyline.ran_b4 = False
                                                        storyline.dw_skip = False
                                        if event.type == pyg.MOUSEBUTTONDOWN:
                                            if storyline.next_button_rect.collidepoint(event.pos):
                                                self.sound_effects_player()
                                                if storyline.current_screen == 9:
                                                    self.stop = False
                                                    storyline.ran_b4 = False
                                                    self.player_answer = ''
                                                    storyline.current_screen = 8
                                                else:
                                                    storyline.current_screen += 1
                                                    if storyline.furthest_screen < storyline.current_screen:
                                                        storyline.furthest_screen = storyline.current_screen
                                                        storyline.ran_b4 = False
                                                    elif storyline.furthest_screen >= storyline.current_screen:
                                                        storyline.ran_b4 = False
                                                        storyline.dw_skip = False
                                            elif storyline.back_button_rect.collidepoint(event.pos):
                                                self.sound_effects_player()
                                                storyline.current_screen -= 1
                                                storyline.ran_b4 = False
                                                storyline.dw_skip = False

                                        if storyline.current_screen == 1 and not storyline.ran_b4:
                                            storyline.screen_1()
                                        elif storyline.current_screen == 2 and not storyline.ran_b4:
                                            while not self.storyline and self.running and not self.stop_en:
                                                for event in pyg.event.get():
                                                    storyline.enter_name()
                                                    pyg.display.update()
                                                    if event.type == pyg.QUIT:
                                                        self.running = False
                                                    if event.type == pyg.KEYDOWN:
                                                        if event.key == pyg.K_BACKSPACE:
                                                            storyline.player_name = storyline.player_name[:-1]
                                                        elif event.key == pyg.K_a:
                                                            storyline.player_name = storyline.player_name[:9] + 'a'
                                                        elif event.key == pyg.K_b:
                                                            storyline.player_name = storyline.player_name[:9] + 'b'
                                                        elif event.key == pyg.K_c:
                                                            storyline.player_name = storyline.player_name[:9] + 'c'
                                                        elif event.key == pyg.K_d:
                                                            storyline.player_name = storyline.player_name[:9] + 'd'
                                                        elif event.key == pyg.K_e:
                                                            storyline.player_name = storyline.player_name[:9] + 'e'
                                                        elif event.key == pyg.K_f:
                                                            storyline.player_name = storyline.player_name[:9] + 'f'
                                                        elif event.key == pyg.K_g:
                                                            storyline.player_name = storyline.player_name[:9] + 'g'
                                                        elif event.key == pyg.K_h:
                                                            storyline.player_name = storyline.player_name[:9] + 'h'
                                                        elif event.key == pyg.K_i:
                                                            storyline.player_name = storyline.player_name[:9] + 'i'
                                                        elif event.key == pyg.K_j:
                                                            storyline.player_name = storyline.player_name[:9] + 'k'
                                                        elif event.key == pyg.K_l:
                                                            storyline.player_name = storyline.player_name[:9] + 'l'
                                                        elif event.key == pyg.K_m:
                                                            storyline.player_name = storyline.player_name[:9] + 'm'
                                                        elif event.key == pyg.K_n:
                                                            storyline.player_name = storyline.player_name[:9] + 'n'
                                                        elif event.key == pyg.K_o:
                                                            storyline.player_name = storyline.player_name[:9] + 'o'
                                                        elif event.key == pyg.K_p:
                                                            storyline.player_name = storyline.player_name[:9] + 'p'
                                                        elif event.key == pyg.K_q:
                                                            storyline.player_name = storyline.player_name[:9] + 'q'
                                                        elif event.key == pyg.K_r:
                                                            storyline.player_name = storyline.player_name[:9] + 'r'
                                                        elif event.key == pyg.K_s:
                                                            storyline.player_name = storyline.player_name[:9] + 's'
                                                        elif event.key == pyg.K_t:
                                                            storyline.player_name = storyline.player_name[:9] + 't'
                                                        elif event.key == pyg.K_u:
                                                            storyline.player_name = storyline.player_name[:9] + 'u'
                                                        elif event.key == pyg.K_v:
                                                            storyline.player_name = storyline.player_name[:9] + 'v'
                                                        elif event.key == pyg.K_w:
                                                            storyline.player_name = storyline.player_name[:9] + 'w'
                                                        elif event.key == pyg.K_x:
                                                            storyline.player_name = storyline.player_name[:9] + 'x'
                                                        elif event.key == pyg.K_y:
                                                            storyline.player_name = storyline.player_name[:9] + 'y'
                                                        elif event.key == pyg.K_z:
                                                            storyline.player_name = storyline.player_name[:9] + 'z'
                                                        elif event.key == pyg.K_0:
                                                            storyline.player_name = storyline.player_name[:9] + "0"
                                                        elif event.key == pyg.K_1:
                                                            storyline.player_name = storyline.player_name[:9] + "1"
                                                        elif event.key == pyg.K_2:
                                                            storyline.player_name = storyline.player_name[:9] + "2"
                                                        elif event.key == pyg.K_3:
                                                            storyline.player_name = storyline.player_name[:9] + "3"
                                                        elif event.key == pyg.K_4:
                                                            storyline.player_name = storyline.player_name[:9] + "4"
                                                        elif event.key == pyg.K_5:
                                                            storyline.player_name = storyline.player_name[:9] + "5"
                                                        elif event.key == pyg.K_6:
                                                            storyline.player_name = storyline.player_name[:9] + "6"
                                                        elif event.key == pyg.K_7:
                                                            storyline.player_name = storyline.player_name[:9] + "7"
                                                        elif event.key == pyg.K_8:
                                                            storyline.player_name = storyline.player_name[:9] + "8"
                                                        elif event.key == pyg.K_9:
                                                            storyline.player_name = storyline.player_name[:9] + "9"
                                                        elif event.key == pyg.K_SPACE:
                                                            storyline.player_name = storyline.player_name[:9] + " "
                                                        elif event.key == pyg.K_RETURN:
                                                            if storyline.player_name == '':
                                                                pass
                                                            else:
                                                                storyline.current_screen = 3
                                                                self.stop_en = True
                                            storyline.ran_b4 = False
                                        elif storyline.current_screen == 3 and not storyline.ran_b4:
                                            storyline.screen_3(storyline.player_name)
                                        elif storyline.current_screen == 4 and not storyline.ran_b4:
                                            storyline.screen_4()
                                        elif storyline.current_screen == 5 and not storyline.ran_b4:
                                            storyline.screen_5()
                                        elif storyline.current_screen == 6 and not storyline.ran_b4:
                                            storyline.screen_6()
                                        elif storyline.current_screen == 7 and not storyline.ran_b4:
                                            storyline.screen_7()
                                        elif storyline.current_screen == 8 and not storyline.ran_b4:
                                            while not self.storyline and self.running and not self.stop:
                                                for event in pyg.event.get():
                                                    self.tutorial_level()
                                                    pyg.display.update()
                                                    if event.type == pyg.QUIT:
                                                        self.running = False
                                                    if event.type == pyg.KEYDOWN:
                                                        if event.key == pyg.K_BACKSPACE:
                                                            self.player_answer = self.player_answer[:-1]
                                                        elif event.key == pyg.K_0:
                                                            self.player_answer = self.player_answer[:4] + "0"
                                                        elif event.key == pyg.K_1:
                                                            self.player_answer = self.player_answer[:4] + "1"
                                                        elif event.key == pyg.K_2:
                                                            self.player_answer = self.player_answer[:4] + "2"
                                                        elif event.key == pyg.K_3:
                                                            self.player_answer = self.player_answer[:4] + "3"
                                                        elif event.key == pyg.K_4:
                                                            self.player_answer = self.player_answer[:4] + "4"
                                                        elif event.key == pyg.K_5:
                                                            self.player_answer = self.player_answer[:4] + "5"
                                                        elif event.key == pyg.K_6:
                                                            self.player_answer = self.player_answer[:4] + "6"
                                                        elif event.key == pyg.K_7:
                                                            self.player_answer = self.player_answer[:4] + "7"
                                                        elif event.key == pyg.K_8:
                                                            self.player_answer = self.player_answer[:4] + "8"
                                                        elif event.key == pyg.K_9:
                                                            self.player_answer = self.player_answer[:4] + "9"
                                                        elif event.key == pyg.K_RETURN:
                                                            try:
                                                                if int(self.player_answer) == int(self.answer):
                                                                    storyline.current_screen = 10
                                                                    self.stop = True
                                                                else:
                                                                    storyline.current_screen = 9
                                                                    self.stop = True
                                                            except ValueError:
                                                                self.display = 'level'
                                                                pass

                                        elif storyline.current_screen == 9 and not storyline.ran_b4:
                                            storyline.screen_8_wrg()
                                        elif storyline.current_screen == 10 and not storyline.ran_b4:
                                            storyline.screen_8_crt()
                                            self.player_answer = ''
                                        elif storyline.current_screen == 11 and not storyline.ran_b4:
                                            storyline.alien_defeat(self.enemy_type)
                                        elif storyline.current_screen == 12 and not storyline.ran_b4:
                                            storyline.screen_9()
                                        elif storyline.current_screen == 13 and not storyline.ran_b4:
                                            self.screen.fill('BLACK')
                                            self.screen.blit(self.heart_box, (1080 / 2 - 323 / 2, 2))
                                            self.heart_y = 17
                                            self.heart_x = (1080 / 2 - 323 / 2) + 17
                                            self.screen.blit(self.heart1, (self.heart_x, self.heart_y))
                                            self.screen.blit(self.heart1, (self.heart_x + (55 + 5), self.heart_y))
                                            self.screen.blit(self.heart1, (self.heart_x + (55 + 5) * 2, self.heart_y))
                                            self.screen.blit(self.heart1, (self.heart_x + (55 + 5) * 3, self.heart_y))
                                            self.screen.blit(self.heart1, (self.heart_x + (55 + 5) * 4, self.heart_y))
                                            storyline.explain_level_menu()
                                        elif storyline.current_screen == 14 and not storyline.ran_b4:
                                            self.screen.fill('BLACK')
                                            self.screen.blit(self.heart_box, (1080 / 2 - 323 / 2, 2))
                                            self.heart_y = 17
                                            self.heart_x = (1080 / 2 - 323 / 2) + 17
                                            self.screen.blit(self.heart1, (self.heart_x, self.heart_y))
                                            self.screen.blit(self.heart1, (self.heart_x + (55 + 5), self.heart_y))
                                            self.screen.blit(self.heart1, (self.heart_x + (55 + 5) * 2, self.heart_y))
                                            self.screen.blit(self.heart1, (self.heart_x + (55 + 5) * 3, self.heart_y))
                                            self.screen.blit(self.heart1, (self.heart_x + (55 + 5) * 4, self.heart_y))
                                            self.screen.blit(self.pause, (self.x - 74, 20))
                                            storyline.explain_level_menu_2()
                                        elif storyline.current_screen == 15 and not storyline.ran_b4:
                                            if not self.ran5:
                                                self.levelMenu()
                                                self.screen.blit(self.semi_trans_player, (0, 0))
                                                self.ran5 = True
                                            storyline.explain_level_menu_3()
                                        elif storyline.current_screen == 16 and not storyline.ran_b4:
                                            if not self.ran6:
                                                self.levelMenu()
                                                self.ran6 = True
                                            storyline.explain_level_menu_4()
                                        elif storyline.current_screen == 17 and not storyline.ran_b4:
                                            if not self.ran2:
                                                self.levelMenu()
                                                self.ran2 = True
                                            storyline.explain_level_menu_5()
                                        if storyline.current_screen > 17:
                                            self.storyline = True
                                            storyline.ran_b4 = False
                                        pyg.display.update()
                            if self.storyline:
                                self.levelMenu()
                                self.randomNum()
                                self.display = "levelMenu"
                        elif self.setting_rect.collidepoint(event.pos):
                            self.sound_effects_player()
                            self.settingScreen()
                            self.display = "settingScreen"

                elif self.display == "settingScreen":
                    self.settingScreen()
                    if event.type == pyg.MOUSEBUTTONDOWN:
                        if self.quit_setting_rect.collidepoint(event.pos):
                            self.sound_effects_player()
                            self.quitScreen()
                            self.display = "exitScreen"
                        elif self.continue_button_rect.collidepoint(event.pos):
                            self.sound_effects_player()
                            self.mainMenu()
                            self.display = "mainMenu"
                        elif self.erase_setting_rect.collidepoint(event.pos):
                            self.sound_effects_player()
                            self.point = 5
                            self.level = 1
                            self.level_now = 1
                            self.current_frame = 0
                            self.last_updated = 0
                            self.playerX = 0
                            self.playerY = 0
                            self.rect.x = 200
                            self.rect.y = 200
                            self.music_playing = False
                            self.soundE_playing = False
                            self.state = 'idle'
                            self.current_image = self.idle_frames_front[0]
                            self.rect.midbottom = (240, 244)
                            self.ran = False
                            self.ran2 = False
                            self.ran3 = False
                            self.ran4 = False
                            self.ran5 = False
                            self.ran6 = False
                            self.ran_crt_wrg = False
                            self.ran_defeat_screen = False
                            self.ran_game_over = False
                            self.storyline = False
                            self.storyline_barry = False
                            self.storyline_cloak = False
                            self.stop = False
                            self.stop_barry = False
                            self.stop_en = False
                            self.stop_barry_2 = False
                            self.defeat_level10 = False
                            self.finish_game = False
                            self.lost_in_barryr = False
                            self.game_finished = False
                            storyline.furthest_screen = 0
                            storyline.current_screen = 1
                            storyline.furthest_screen_barry = 0
                            storyline.current_screen_barry = 1
                            storyline.current_screen_cloak = 1
                            storyline.furthest_screen_cloak = 0
                            storyline.player_name = ''
                            storyline.dw_skip = True
                            storyline.ran_b4 = False
                            storyline.ran4 = False
                            self.player_answer = ""
                            self.player_name = ''
                            self.mainMenu()
                            self.display = "mainMenu"
                        if self.music_button_rect.collidepoint(event.pos) and self.music_playing:
                            self.sound_effects_player()
                            self.sound_effects_player()
                            self.music_button = self.music_button_off
                            pyg.mixer.music.stop()
                            self.music_playing = False
                        elif self.music_button_rect.collidepoint(event.pos) and not self.music_playing:
                            self.sound_effects_player()
                            self.sound_effects_player()
                            self.music_button = self.music_button_on
                            pyg.mixer.music.play(-1)
                            self.music_playing = True
                        if self.soundE_button_rect.collidepoint(event.pos) and self.soundE_playing:
                            self.sound_effects_player()
                            self.soundE_button = self.soundE_button_off
                            self.soundE_playing = False
                        elif self.soundE_button_rect.collidepoint(event.pos) and not self.soundE_playing:
                            self.sound_effects_player()
                            self.soundE_button = self.soundE_button_on
                            self.soundE_playing = True

                elif self.display == "exitScreen":
                    self.quitScreen()
                    if event.type == pyg.MOUSEBUTTONDOWN:
                        if self.quit_rect.collidepoint(event.pos):
                            self.sound_effects_player()
                            self.running = False
                        elif self.cancel_rect.collidepoint(event.pos):
                            self.sound_effects_player()
                            self.settingScreen()
                            self.display = "settingScreen"

                elif self.display == "levelMenu":
                    self.levelMenu()
                    if event.type == pyg.MOUSEBUTTONDOWN:
                        if self.pause_rect.collidepoint(event.pos):
                            self.sound_effects_player()
                            self.pauseScreenForMenu()
                            self.display = "pauseScreen"

                    if event.type == pyg.KEYDOWN:
                        if event.key == pyg.K_LEFT:
                            self.LEFT_KEY, self.FACING_LEFT = True, True
                        elif event.key == pyg.K_RIGHT:
                            self.RIGHT_KEY, self.FACING_RIGHT = True, True
                        elif event.key == pyg.K_UP:
                            self.UP_KEY, self.FACING_BACK = True, True
                        elif event.key == pyg.K_DOWN:
                            self.DOWN_KEY, self.FACING_FRONT = True, True
                        elif event.key == pyg.K_RETURN:
                            self.player_answer = ""
                            self.answer = ""
                            self.randomNum()
                            if self.level > 0:
                                if self.rect.colliderect(self.level1_rect):
                                    self.level_now = 1
                                    self.chat(self.level_now, self.num1, self.num2, "+")
                                    self.display = "level"

                            if self.level > 1:
                                if self.rect.colliderect(self.level2_rect):
                                    self.level_now = 2
                                    self.chat(self.level_now, self.num3, self.num4, "+")
                                    self.display = "level"

                            if self.level > 2:
                                if self.rect.colliderect(self.level3_rect):
                                    self.level_now = 3
                                    self.chat(self.level_now, self.num3, self.num1, "-")
                                    self.display = "level"

                            if self.level > 3:
                                if self.rect.colliderect(self.level4_rect):
                                    self.level_now = 4
                                    self.chat(self.level_now, self.num3, self.num4, "-")
                                    self.display = "level"

                            if self.level > 4:
                                if self.rect.colliderect(self.level5_rect):
                                    self.level_now = 5
                                    self.chat(self.level_now, self.num5, self.num6, "+")
                                    self.display = "level"

                            if self.level > 5:
                                if self.rect.colliderect(self.level6_rect):
                                    self.level_now = 6
                                    self.chat(self.level_now, self.num5, self.num6, "-")
                                    self.display = "level"

                            if self.level > 6:
                                if self.rect.colliderect(self.level7_rect):
                                    self.level_now = 7
                                    self.chat(self.level_now, self.num1, self.num2, "*")
                                    self.display = "level"

                            if self.level > 7:
                                if self.rect.colliderect(self.level8_rect):
                                    self.level_now = 8
                                    self.chat(self.level_now, self.num3, self.num4, "/")
                                    self.display = "level"

                            if self.level > 8:
                                if self.rect.colliderect(self.level9_rect):
                                    self.level_now = 9
                                    self.chat(self.level_now, self.num3, self.num1, "/")
                                    self.display = "level"

                            if self.level > 9:
                                if self.rect.colliderect(self.level10_rect):
                                    self.level_now = 10
                                    self.display = "level"

                    if event.type == pyg.KEYUP:
                        if event.key == pyg.K_LEFT:
                            self.LEFT_KEY = False
                            self.FACING_FRONT, self.FACING_BACK, self.FACING_RIGHT = False, False, False
                        elif event.key == pyg.K_RIGHT:
                            self.RIGHT_KEY = False
                            self.FACING_FRONT, self.FACING_BACK, self.FACING_LEFT = False, False, False
                        elif event.key == pyg.K_UP:
                            self.UP_KEY = False
                            self.FACING_FRONT, self.FACING_LEFT, self.FACING_RIGHT = False, False, False
                        elif event.key == pyg.K_DOWN:
                            self.DOWN_KEY = False
                            self.FACING_LEFT, self.FACING_BACK, self.FACING_RIGHT = False, False, False

                elif self.display == "pauseScreen":
                    self.pauseScreenForMenu()
                    if event.type == pyg.MOUSEBUTTONDOWN:
                        if self.back_rect.collidepoint(event.pos):
                            self.sound_effects_player()
                            self.levelMenu()
                            self.display = "levelMenu"
                            self.ran = False
                        if self.back_to_main_rect.collidepoint(event.pos):
                            self.sound_effects_player()
                            self.mainMenu()
                            self.display = "mainMenu"
                            self.ran = False
                        if self.music_button_rect.collidepoint(event.pos) and self.music_playing:
                            self.sound_effects_player()
                            self.music_button = self.music_button_off
                            pyg.mixer.music.stop()
                            self.music_playing = False
                        elif self.music_button_rect.collidepoint(event.pos) and not self.music_playing:
                            self.sound_effects_player()
                            self.music_button = self.music_button_on
                            pyg.mixer.music.play(-1)
                            self.music_playing = True
                        if self.soundE_button_rect.collidepoint(event.pos) and self.soundE_playing:
                            self.sound_effects_player()
                            self.soundE_button = self.soundE_button_off
                            self.soundE_playing = False
                        elif self.soundE_button_rect.collidepoint(event.pos) and not self.soundE_playing:
                            self.sound_effects_player()
                            self.soundE_button = self.soundE_button_on
                            self.soundE_playing = True

                elif self.display == "pauseScreenForLevel":
                    self.pauseScreenForLevel()
                    if event.type == pyg.MOUSEBUTTONDOWN:
                        if self.exit_button_rect.collidepoint(event.pos):
                            self.sound_effects_player()
                            self.levelMenu()
                            self.display = "levelMenu"
                            self.ran2 = False
                        if self.continue_button_rect.collidepoint(event.pos):
                            self.sound_effects_player()
                            self.display = "level"
                            self.ran2 = False
                        if self.music_button_rect.collidepoint(event.pos) and self.music_playing:
                            self.sound_effects_player()
                            self.sound_effects_player()
                            self.music_button = self.music_button_off
                            pyg.mixer.music.stop()
                            self.music_playing = False
                        elif self.music_button_rect.collidepoint(event.pos) and not self.music_playing:
                            self.sound_effects_player()
                            self.sound_effects_player()
                            self.music_button = self.music_button_on
                            pyg.mixer.music.play(-1)
                            self.music_playing = True
                        if self.soundE_button_rect.collidepoint(event.pos) and self.soundE_playing:
                            self.sound_effects_player()
                            self.sound_effects_player()
                            self.soundE_button = self.soundE_button_off
                            self.soundE_playing = False
                        elif self.soundE_button_rect.collidepoint(event.pos) and not self.soundE_playing:
                            self.sound_effects_player()
                            self.sound_effects_player()
                            self.soundE_button = self.soundE_button_on
                            self.soundE_playing = True

                elif self.display == "level":
                    self.LEFT_KEY, self.RIGHT_KEY, self.UP_KEY, self.DOWN_KEY = False, False, False, False
                    if self.answer_type:
                        if event.type == pyg.KEYDOWN:
                            if event.key == pyg.K_BACKSPACE:
                                self.player_answer = self.player_answer[:-1]
                            elif event.key == pyg.K_0:
                                self.player_answer = self.player_answer[:4] + "0"
                            elif event.key == pyg.K_1:
                                self.player_answer = self.player_answer[:4] + "1"
                            elif event.key == pyg.K_2:
                                self.player_answer = self.player_answer[:4] + "2"
                            elif event.key == pyg.K_3:
                                self.player_answer = self.player_answer[:4] + "3"
                            elif event.key == pyg.K_4:
                                self.player_answer = self.player_answer[:4] + "4"
                            elif event.key == pyg.K_5:
                                self.player_answer = self.player_answer[:4] + "5"
                            elif event.key == pyg.K_6:
                                self.player_answer = self.player_answer[:4] + "6"
                            elif event.key == pyg.K_7:
                                self.player_answer = self.player_answer[:4] + "7"
                            elif event.key == pyg.K_8:
                                self.player_answer = self.player_answer[:4] + "8"
                            elif event.key == pyg.K_9:
                                self.player_answer = self.player_answer[:4] + "9"
                            elif event.key == pyg.K_RETURN:
                                self.display = "correctWrong" + str(self.level_now)
                                self.ran_crt_wrg = False
                                try:
                                    if int(self.player_answer) == int(self.answer):
                                        if self.level == self.level_now:
                                            self.level += 1
                                        elif self.level_now != self.level:
                                            pass
                                    else:
                                        self.point -= 1
                                except ValueError:
                                    self.display = 'level'
                                    pass
                    if self.level_now == 1:
                        self.chat(self.level_now, self.num1, self.num2, "+")
                    elif self.level_now == 2:
                        self.chat(self.level_now, self.num3, self.num4, "+")
                    elif self.level_now == 3:
                        self.chat(self.level_now, self.num3, self.num1, "-")
                    elif self.level_now == 4:
                        self.chat(self.level_now, self.num3, self.num4, "-")
                    elif self.level_now == 5:
                        self.chat(self.level_now, self.num5, self.num6, "+")
                    elif self.level_now == 6:
                        self.chat(self.level_now, self.num5, self.num6, "-")
                    elif self.level_now == 7:
                        self.chat(self.level_now, self.num3, self.num4, "*")
                    elif self.level_now == 8:
                        self.chat(self.level_now, self.num3, self.num4, "/")
                    elif self.level_now == 9:
                        self.chat(self.level_now, self.num3, self.num1, "/")
                    elif self.level_now == 10:
                        while not self.storyline_cloak and self.running:
                            for event in pyg.event.get():
                                if event.type == pyg.QUIT:
                                    self.running = False
                                if event.type == pyg.KEYDOWN:
                                    if event.key == pyg.K_RETURN:
                                        if storyline.current_screen_cloak == 2:
                                            self.storyline_cloak = True
                                            storyline.ran_b4 = False
                                        storyline.current_screen_cloak += 1
                                        if storyline.furthest_screen_cloak < storyline.current_screen_cloak:
                                            storyline.furthest_screen_cloak = storyline.current_screen_cloak
                                            storyline.ran_b4 = False
                                        elif storyline.furthest_screen_cloak >= storyline.current_screen_cloak:
                                            storyline.ran_b4 = False
                                            storyline.dw_skip = False
                                if event.type == pyg.MOUSEBUTTONDOWN:
                                    if storyline.next_button_rect.collidepoint(event.pos):
                                        self.sound_effects_player()
                                        storyline.current_screen_cloak += 1
                                        if storyline.furthest_screen_cloak < storyline.current_screen_cloak:
                                            storyline.furthest_screen_cloak = storyline.current_screen_cloak
                                            storyline.ran_b4 = False
                                        elif storyline.furthest_screen_cloak >= storyline.current_screen_cloak:
                                            storyline.ran_b4 = False
                                            storyline.dw_skip = False
                            if storyline.current_screen_cloak == 1 and not storyline.ran_b4:
                                storyline.final_boss_1()
                            elif storyline.current_screen_cloak == 2 and not storyline.ran_b4:
                                storyline.final_boss_2()
                        self.lost_in_barryr = False
                        self.chat(self.level_now, self.num3, self.num4, "*")

                    if event.type == pyg.MOUSEBUTTONDOWN:
                        if self.pause_rect.collidepoint(event.pos):
                            self.sound_effects_player()
                            self.pauseScreenForLevel()
                            self.display = "pauseScreenForLevel"

                elif self.display == "correctWrong"+str(self.level_now):
                    self.correctWrong(self.level_now)
                    if event.type == pyg.KEYDOWN:
                        if event.key == pyg.K_RETURN:
                            storyline.ran_b4 = False
                            if self.level_now == 10:
                                self.correctWrong(self.level_now)
                            if self.player_answer == '':
                                pass
                            elif int(self.player_answer) == int(self.answer) and not storyline.ran_b4 \
                                    and self.level > 10 and self.current_level == 10:
                                if not self.storyline_barry:
                                    self.player_answer = ''
                                    while not self.storyline_barry and self.running:
                                        if self.lost_in_barryr:
                                            break
                                        for event in pyg.event.get():
                                            if event.type == pyg.QUIT:
                                                self.running = False
                                            if event.type == pyg.KEYDOWN:
                                                if event.key == pyg.K_RETURN:
                                                    if storyline.current_screen_barry == 8:
                                                        pass
                                                    elif storyline.current_screen_barry == 9:
                                                        storyline.ran_b4 = False
                                                        storyline.current_screen_barry = 13
                                                    elif storyline.current_screen_barry == 11:
                                                        storyline.ran_b4 = False
                                                        storyline.current_screen_barry = 13
                                                    else:
                                                        storyline.current_screen_barry += 1
                                                        if storyline.furthest_screen_barry < storyline.current_screen_barry:
                                                            storyline.furthest_screen_barry = storyline.current_screen_barry
                                                            storyline.ran_b4 = False
                                                        elif storyline.furthest_screen_barry >= storyline.current_screen_barry:
                                                            storyline.ran_b4 = False
                                                            storyline.dw_skip = False
                                            if event.type == pyg.MOUSEBUTTONDOWN:
                                                if storyline.next_button_rect.collidepoint(event.pos):
                                                    self.sound_effects_player()
                                                    if storyline.current_screen_barry == 9:
                                                        storyline.ran_b4 = False
                                                        storyline.current_screen_barry = 13
                                                    elif storyline.current_screen_barry == 11:
                                                        storyline.ran_b4 = False
                                                        storyline.current_screen_barry = 13
                                                    else:
                                                        storyline.current_screen_barry += 1
                                                        if storyline.furthest_screen_barry < storyline.current_screen_barry:
                                                            storyline.furthest_screen_barry = storyline.current_screen_barry
                                                            storyline.ran_b4 = False
                                                        elif storyline.furthest_screen_barry >= storyline.current_screen_barry:
                                                            storyline.ran_b4 = False
                                                            storyline.dw_skip = False
                                                elif storyline.deny_button_rect.collidepoint(event.pos):
                                                    if storyline.current_screen_barry == 8:
                                                        self.sound_effects_player()
                                                        storyline.current_screen_barry = 9
                                                        storyline.final_boss_defeated_deny()
                                                        if storyline.furthest_screen_barry < storyline.current_screen_barry:
                                                            storyline.furthest_screen_barry = storyline.current_screen_barry
                                                            storyline.ran_b4 = False
                                                        elif storyline.furthest_screen_barry >= storyline.current_screen_barry:
                                                            storyline.ran_b4 = False
                                                            storyline.dw_skip = False
                                                elif storyline.accept_button_rect.collidepoint(event.pos):
                                                    if storyline.current_screen_barry == 8:
                                                        self.sound_effects_player()
                                                        storyline.current_screen_barry = 10
                                                        self.chat(12, self.num1, self.num2, '+')
                                                        if storyline.furthest_screen_barry < storyline.current_screen_barry:
                                                            storyline.furthest_screen_barry = storyline.current_screen_barry
                                                            storyline.ran_b4 = False
                                                        elif storyline.furthest_screen_barry >= storyline.current_screen_barry:
                                                            storyline.ran_b4 = False
                                                            storyline.dw_skip = False

                                            if storyline.current_screen_barry == 1 and not storyline.ran_b4:
                                                storyline.final_boss_reveal_1()
                                            elif storyline.current_screen_barry == 2 and not storyline.ran_b4:
                                                storyline.final_boss_reveal_2()
                                            elif storyline.current_screen_barry == 3 and not storyline.ran_b4:
                                                storyline.final_boss_reveal_3()
                                            elif storyline.current_screen_barry == 4 and not storyline.ran_b4:
                                                storyline.final_boss_reveal_4(self.player_name)
                                            elif storyline.current_screen_barry == 5 and not storyline.ran_b4:
                                                while not self.storyline_barry and self.running and not self.stop_barry:
                                                    if self.lost_in_barryr:
                                                        break
                                                    for event in pyg.event.get():
                                                        self.chat(11, self.num5, self.num2, '/')
                                                        pyg.display.update()
                                                        if event.type == pyg.QUIT:
                                                            self.running = False
                                                        if event.type == pyg.KEYDOWN:
                                                            if event.key == pyg.K_BACKSPACE:
                                                                self.player_answer = self.player_answer[:-1]
                                                            elif event.key == pyg.K_0:
                                                                self.player_answer = self.player_answer[:4] + "0"
                                                            elif event.key == pyg.K_1:
                                                                self.player_answer = self.player_answer[:4] + "1"
                                                            elif event.key == pyg.K_2:
                                                                self.player_answer = self.player_answer[:4] + "2"
                                                            elif event.key == pyg.K_3:
                                                                self.player_answer = self.player_answer[:4] + "3"
                                                            elif event.key == pyg.K_4:
                                                                self.player_answer = self.player_answer[:4] + "4"
                                                            elif event.key == pyg.K_5:
                                                                self.player_answer = self.player_answer[:4] + "5"
                                                            elif event.key == pyg.K_6:
                                                                self.player_answer = self.player_answer[:4] + "6"
                                                            elif event.key == pyg.K_7:
                                                                self.player_answer = self.player_answer[:4] + "7"
                                                            elif event.key == pyg.K_8:
                                                                self.player_answer = self.player_answer[:4] + "8"
                                                            elif event.key == pyg.K_9:
                                                                self.player_answer = self.player_answer[:4] + "9"
                                                            elif event.key == pyg.K_RETURN:
                                                                if self.player_answer == '':
                                                                    pass
                                                                elif int(self.player_answer) == int(self.answer):
                                                                    storyline.current_screen_barry = 6
                                                                    self.player_answer = ''
                                                                    self.stop_barry = True
                                                                elif int(self.player_answer) != int(self.answer):
                                                                    self.display = "correctWrong" + str(self.level_now)
                                                                    self.lost_in_barryr = True
                                                                    self.ran_crt_wrg = False
                                                                    break
                                            elif storyline.current_screen_barry == 6 and not storyline.ran_b4:
                                                storyline.crt_screen3()
                                            elif storyline.current_screen_barry == 7 and not storyline.ran_b4:
                                                storyline.final_boss_defeated()
                                            elif storyline.current_screen_barry == 8 and not storyline.ran_b4:
                                                storyline.final_boss_defeated_2()
                                            elif storyline.current_screen_barry == 9 and not storyline.ran_b4:
                                                storyline.final_boss_defeated_deny()
                                            elif storyline.current_screen_barry == 10 and not storyline.ran_b4:
                                                while not self.storyline_barry and self.running and not self.stop_barry_2:
                                                    for event in pyg.event.get():
                                                        self.chat(12, self.num1, self.num2, '+')
                                                        pyg.display.update()
                                                        if event.type == pyg.QUIT:
                                                            self.running = False
                                                        if event.type == pyg.KEYDOWN:
                                                            if event.key == pyg.K_BACKSPACE:
                                                                self.player_answer = self.player_answer[:-1]
                                                            elif event.key == pyg.K_0:
                                                                self.player_answer = self.player_answer[:4] + "0"
                                                            elif event.key == pyg.K_1:
                                                                self.player_answer = self.player_answer[:4] + "1"
                                                            elif event.key == pyg.K_2:
                                                                self.player_answer = self.player_answer[:4] + "2"
                                                            elif event.key == pyg.K_3:
                                                                self.player_answer = self.player_answer[:4] + "3"
                                                            elif event.key == pyg.K_4:
                                                                self.player_answer = self.player_answer[:4] + "4"
                                                            elif event.key == pyg.K_5:
                                                                self.player_answer = self.player_answer[:4] + "5"
                                                            elif event.key == pyg.K_6:
                                                                self.player_answer = self.player_answer[:4] + "6"
                                                            elif event.key == pyg.K_7:
                                                                self.player_answer = self.player_answer[:4] + "7"
                                                            elif event.key == pyg.K_8:
                                                                self.player_answer = self.player_answer[:4] + "8"
                                                            elif event.key == pyg.K_9:
                                                                self.player_answer = self.player_answer[:4] + "9"
                                                            elif event.key == pyg.K_RETURN:
                                                                try:
                                                                    if int(self.player_answer) == int(self.answer):
                                                                        storyline.current_screen_barry = 12
                                                                        self.player_answer = ''
                                                                        self.stop_barry_2 = True
                                                                    else:
                                                                        storyline.current_screen_barry = 11
                                                                        self.stop_barry_2 = True
                                                                except ValueError:
                                                                    pass
                                                storyline.ran_b4 = False
                                            elif storyline.current_screen_barry == 11 and not storyline.ran_b4:
                                                storyline.final_boss_defeated_accept_wrg(self.answer)
                                            elif storyline.current_screen_barry == 12 and not storyline.ran_b4:
                                                storyline.final_boss_defeated_accept_crt()
                                            elif storyline.current_screen_barry == 13 and not storyline.ran_b4:
                                                storyline.grave_barry()
                                            elif storyline.current_screen_barry == 14 and not storyline.ran_b4:
                                                storyline.ending_screen()
                                            elif storyline.current_screen_barry == 15 and not storyline.ran_b4:
                                                storyline.ending_screen_2()
                                            elif storyline.current_screen_barry == 16 and not storyline.ran_b4:
                                                storyline.ending_screen_3()
                                            if storyline.current_screen_barry > 16:
                                                self.display = 'levelMenu'
                                                self.storyline_barry = True
                                                storyline.ran_b4 = False
                                                self.rect.x = 200
                                                self.rect.y = 200
                                                self.FACING_RIGHT = False
                                                self.FACING_BACK = False
                                                self.FACING_LEFT = False
                                                self.FACING_FRONT = True
                                                self.game_finished = True
                                            pyg.display.update()

                                else:
                                    if int(self.player_answer) == int(self.answer):
                                        storyline.alien_defeat(self.enemy_type)
                                        self.display = 'defeatScreen'
                                        self.ran_defeat_screen = True

                            elif int(self.player_answer) == int(self.answer) and not storyline.ran_b4:
                                storyline.alien_defeat(self.enemy_type)
                                self.display = 'defeatScreen'
                                self.ran_defeat_screen = True
                            else:
                                if self.point == 0:
                                    storyline.game_over()
                                    self.display = 'gameOver'
                                    self.ran_game_over = True
                                else:
                                    self.levelMenu()
                                    self.display = 'levelMenu'
                                    storyline.ran_b4 = False


                elif self.display == 'defeatScreen':
                    if not self.ran_defeat_screen:
                        storyline.alien_defeat(self.enemy_type)
                    if event.type == pyg.KEYDOWN:
                        if event.key == pyg.K_RETURN:
                            storyline.ran_b4 = False
                            self.levelMenu()
                            self.display = 'levelMenu'
                    if event.type == pyg.MOUSEBUTTONDOWN:
                        if storyline.next_button_rect.collidepoint(event.pos):
                            storyline.ran_b4 = False
                            self.levelMenu()
                            self.display = 'levelMenu'


                elif self.display == 'gameOver':
                    if not self.ran_game_over:
                        storyline.game_over()
                    if event.type == pyg.KEYDOWN:
                        if event.key == pyg.K_RETURN:
                            self.sound_effects_player()
                            self.point = 5
                            self.level = 1
                            self.level_now = 1
                            self.current_frame = 0
                            self.last_updated = 0
                            self.playerX = 0
                            self.playerY = 0
                            self.rect.x = 200
                            self.rect.y = 200
                            self.music_playing = False
                            self.soundE_playing = False
                            self.state = 'idle'
                            self.current_image = self.idle_frames_front[0]
                            self.rect.midbottom = (240, 244)
                            self.ran = False
                            self.ran2 = False
                            self.ran3 = False
                            self.ran4 = False
                            self.ran5 = False
                            self.ran6 = False
                            self.ran_crt_wrg = False
                            self.ran_defeat_screen = False
                            self.ran_game_over = False
                            self.storyline_barry = False
                            self.storyline_cloak = False
                            self.stop = False
                            self.stop_barry = False
                            self.stop_en = False
                            self.stop_barry_2 = False
                            self.defeat_level10 = False
                            self.finish_game = False
                            self.lost_in_barryr = False
                            self.game_finished = False
                            storyline.furthest_screen = 0
                            storyline.current_screen = 1
                            storyline.furthest_screen_barry = 0
                            storyline.current_screen_barry = 1
                            storyline.current_screen_cloak = 1
                            storyline.furthest_screen_cloak = 0
                            storyline.player_name = ''
                            storyline.dw_skip = True
                            storyline.ran_b4 = False
                            storyline.ran4 = False
                            self.player_answer = ""
                            self.FACING_RIGHT = False
                            self.FACING_BACK = False
                            self.FACING_LEFT = False
                            self.FACING_FRONT = True
                            self.levelMenu()
                            self.display = 'levelMenu'

                if self.game_finished:
                    self.point = 5

            pyg.display.update()

main1 = Manager()
main1.main()
