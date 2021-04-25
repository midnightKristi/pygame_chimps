import pygame
from loaders import *
from sprites import *

# If fonts cannot be loaded, give warning
if not pygame.font:
    print("Warning, fonts disabled")

# If sounds mixer cannot be loaded, give warning
if not pygame.mixer:
    print("Warning, sound disabled")


def main():
    # Dimension of the game window
    display_size = (468, 60)

    # Fps of game
    frame_per_sec = 60

    # Initialise pygame
    pygame.init()

    # Initialise game window
    game_screen = pygame.display.set_mode(display_size)
    pygame.display.set_caption("Chimps")
    # Hide mouse in game window
    pygame.mouse.set_visible(0)

    # Game background
    background = pygame.Surface(game_screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    # Game background text
    if pygame.font:
        # None = default font
        font_setting = pygame.font.Font(None, 24)
        title_text = font_setting.render("Slap the Chimp", 1, (250, 250, 250))
        title_position = title_text.get_rect(centerx=background.get_width() / 2)
        background.blit(title_text, title_position)

    game_screen.blit(background, (0, 0))
    pygame.display.flip()

    # Load sounds
    whiff_sound = load_sound('gasp.wav')
    punched_sound = load_sound('punched.wav')

    # Load sprites
    chimp = Chimp()
    fist = Fist()
    all_sprites = pygame.sprite.RenderPlain((fist, chimp))

    # Load clock
    clock = pygame.time.Clock()

    # Main loop
    while True:
        # Run at 60fps
        clock.tick(frame_per_sec)

        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == MOUSEBUTTONDOWN:
                if fist.punch(chimp):
                    punched_sound.play()
                    chimp.punched()
                else:
                    whiff_sound.play()
            elif event.type == MOUSEBUTTONUP:
                fist.unpunch()

        all_sprites.update()

        game_screen.blit(background, (0, 0))
        all_sprites.draw(game_screen)
        pygame.display.flip()

    pygame.quit()

