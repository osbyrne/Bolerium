import pygame
import os


def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()


def img_maker(folder_name: str, image_name: str, width: int, height: int):
    return pygame.transform.scale(
        pygame.image.load(
            os.path.join(
                os.path.join(
                    os.path.dirname(__file__),
                    folder_name),
                image_name)),
        (width, height)
    )


def sound_player(folder: str, filename: str):
    return pygame.mixer.Sound(
        os.path.join(
            os.path.join(os.path.dirname(__file__), folder), filename))


def txt(text: str, color: list, font_seize: float):
    return pygame.font.SysFont(
        "georgia", int(font_seize)).render(text, True, color)


def pause():
    for action in pygame.event.get():
        if action.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_p]:
            while True:
                run_pause()
                for action in pygame.event.get():
                    if action.type == pygame.KEYDOWN:
                        pygame.mouse.set_visible(False)
                        return None


def run_pause():
    pass
