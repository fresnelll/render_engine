import random
from PIL import Image
import math

class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vec3(self.x * scalar, self.y * scalar, self.z * scalar)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def length(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        length = self.length()
        return Vec3(self.x / length, self.y / length, self.z / length)

class Sphere:
    def __init__(self, center, radius, color):
        self.center = center
        self.radius = radius
        self.color = color

def ray_sphere_intersection(ray, sphere):
    oc = ray.origin - sphere.center
    a = ray.direction.dot(ray.direction)
    b = 2.0 * oc.dot(ray.direction)
    c = oc.dot(oc) - sphere.radius * sphere.radius
    discriminant = b * b - 4 * a * c
    if discriminant > 0:
        root = (-b - math.sqrt(discriminant)) / (2.0 * a)
        if root > 0:
            hit_point = ray.origin + ray.direction * root
            outward_normal = (hit_point - sphere.center).normalize()  # Corrected line
            return (True, hit_point, outward_normal, sphere.color)
    return (False, None, None, None)

class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

def color(ray, spheres):
    for sphere in spheres:
        intersection = ray_sphere_intersection(ray, sphere)
        if intersection[0]:
            return intersection[3]
    unit_direction = ray.direction.normalize()
    t = 0.5 * (unit_direction.y + 1.0)
    return Vec3((1.0 - t) * 1.0 + t * 0.5, (1.0 - t) * 1.0 + t * 0.7, (1.0 - t) * 1.0 + t * 1.0)

def main():
    # Image settings
    image_width = 200
    image_height = 100
    max_color = 255

    # Camera settings
    viewport_height = 2.0
    viewport_width = 4.0
    focal_length = 1.0
    origin = Vec3(0, 0, 0)
    horizontal = Vec3(viewport_width, 0, 0)
    vertical = Vec3(0, viewport_height, 0)
    lower_left_corner = origin - horizontal * 0.5 - vertical * 0.5 - Vec3(0, 0, focal_length)

    # Scene setup
    spheres = [
        Sphere(Vec3(0, 0, -1), 0.5, Vec3(1, 0, 0)),
        Sphere(Vec3(0, -100.5, -1), 100, Vec3(0, 1, 0)),
    ]

    # Render
    image = Image.new('RGB', (image_width, image_height))
    for j in range(image_height - 1, -1, -1):
        for i in range(0, image_width):
            u = i / (image_width - 1)
            v = j / (image_height - 1)
            ray = Ray(
                origin,
                lower_left_corner + horizontal * u + vertical * v - origin
            )
            pixel_color = color(ray, spheres)
            ir = int(max_color * pixel_color.x)
            ig = int(max_color * pixel_color.y)
            ib = int(max_color * pixel_color.z)
            image.putpixel((i, image_height - j - 1), (ir, ig, ib))

    image.save('output.png')

if __name__ == '__main__':
    main()
