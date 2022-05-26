import pygame
import math
import random
import support
import settings
from tiles import AnimatedTile


class Enemy(AnimatedTile):
    def __init__(self, size, x, y, display_surface):
        super().__init__(size, x, y, '../graphics/enemy/run')
        self.rect.y += size - self.image.get_size()[1]
        self.speed = random.randint(3, 5)
        self.line = [255, 0, 0]
        self.shoot = 0
        self.display_surface = display_surface
        self.bullets_shot = []
        self.bullet = {
            "age": 0,
            "animations": support.import_folder('../graphics/bullet'),
            "animation state": 0,
            "angle": 0
        }

    def attack(self, screen, player_x: int, player_y: int):
        origin = [self.rect.x, self.rect.y]
        difference = [abs(player_x - origin[0]), abs(player_y - origin[1])]
        norm = math.sqrt(difference[0] ** 2 + difference[1] ** 2)

        if norm < 600:
            pygame.draw.line(screen, self.line, (origin[0], origin[1]), (player_x, player_y))
            self.shoot = 0 if self.shoot == 100 else self.shoot + 1
            if not self.shoot:
                new_bullet = self.bullet
                new_bullet["origin"] = [self.rect.x, self.rect.y]
                new_bullet["speed"] = norm
                new_bullet["angle"] = 0  # SOH CAH TOA
                self.bullets_shot.append(new_bullet)

    def reverse_image(self):
        if self.speed > 0:
            self.image = pygame.transform.flip(self.image, True, False)

    def reverse(self):
        self.speed *= -1

    def update(self, shift):
        self.rect.x += shift
        self.rect.x += self.speed
        self.animate()
        self.reverse_image()

        for bullet in self.bullets_shot:

            index = bullet["animation state"]
            image = bullet["animations"][index]
            bullet["animation state"] = index + 1 if index > len(bullet["animations"])-1 else 0

            speed = bullet["speed"]
            angle = bullet["angle"]
            bullet["age"] += 1 / 60
            time = bullet["age"]
            origin = bullet["origin"]

            x = origin[0] + time * math.cos(angle) * speed
            y = origin[1] + time * math.sin(angle) * speed + 0.5*settings.gravity * time**2

            self.display_surface.blit(image, (x, y))
