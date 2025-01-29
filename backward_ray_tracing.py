import pygame
import time
import numpy as np

# Constants
width, height = 800, 600
background_color = (255, 255, 255)
ray_color = (0, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Backward Ray Tracing Example")

# Define scene (spheres and light)
spheres = [(np.array([0, 0, -5]), 1), (np.array([2, -1, -4]), 0.5)]
light_position = np.array([3, 3, 1])
light_intensity = 0.8
# Ray tracing function
def shadow_ray(origin, direction, spheres):
    for sphere in spheres:
        center, radius = sphere
        oc = center - origin
        a = np.dot(direction, direction)
        b = 2.0 * np.dot(oc, direction)
        c = np.dot(oc, oc) - radius ** 2
        discriminant = b ** 2 - 4 * a * c

        if discriminant > 0:
            return True

    return False

# Measure render time for backward ray tracing
start_time_backward = time.time()

for y in range(height):
    for x in range(width):
        ray_origin = np.array([0, 0, 0])
        ray_direction = np.array([x - width / 2, y - height / 2, 0]) / width
        to_light = light_position - ray_origin
        to_light_direction = to_light / np.linalg.norm(to_light)

        if not shadow_ray(ray_origin, to_light_direction, spheres):
            # No shadow, calculate illumination
            dot_product = np.dot(to_light_direction, ray_direction)
            intensity = max(dot_product, 0) * light_intensity
            pixel_color = [c * intensity for c in ray_color]
            screen.set_at((x, y), pixel_color)

pygame.display.flip()

backward_render_time = time.time() - start_time_backward
print(f"Backward Ray Tracing Render Time: {backward_render_time} seconds")

# Event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
