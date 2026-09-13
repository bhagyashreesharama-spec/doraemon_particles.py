import tkinter as tk
import random
import math

# ==========================================
# DORAEMON PARTICLE ANIMATION
# Python standard library only
# ==========================================

WIDTH = 900
HEIGHT = 900

root = tk.Tk()
root.title("Doraemon - Particle Art")
root.configure(bg="black")

canvas = tk.Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    bg="black",
    highlightthickness=0
)
canvas.pack()

particles = []


# ==========================================
# PARTICLE
# ==========================================

class Particle:
    def __init__(self, target_x, target_y, color, size):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)

        self.tx = target_x
        self.ty = target_y

        self.color = color
        self.size = size

        self.speed = random.uniform(0.035, 0.065)
        self.phase = random.uniform(0, math.pi * 2)

        self.id = canvas.create_oval(
            self.x,
            self.y,
            self.x + size,
            self.y + size,
            fill=color,
            outline=""
        )

    def update(self):

        dx = self.tx - self.x
        dy = self.ty - self.y

        self.x += dx * self.speed
        self.y += dy * self.speed

        # Very small floating movement
        self.x += math.sin(self.phase) * 0.08
        self.y += math.cos(self.phase) * 0.08

        canvas.coords(
            self.id,
            self.x,
            self.y,
            self.x + self.size,
            self.y + self.size
        )


# ==========================================
# CREATE PARTICLES
# ==========================================

def add_particle(x, y, color, size=2):

    particles.append(
        Particle(x, y, color, size)
    )


# ==========================================
# FILLED ELLIPSE
# ==========================================

def ellipse(cx, cy, rx, ry, color, count):

    for _ in range(count):

        angle = random.uniform(0, math.pi * 2)

        r = math.sqrt(random.random())

        x = cx + math.cos(angle) * rx * r
        y = cy + math.sin(angle) * ry * r

        add_particle(
            x,
            y,
            color,
            random.choice([2, 2, 2, 3])
        )


# ==========================================
# FILLED CIRCLE
# ==========================================

def circle(cx, cy, radius, color, count):

    for _ in range(count):

        angle = random.uniform(0, math.pi * 2)

        r = radius * math.sqrt(random.random())

        x = cx + math.cos(angle) * r
        y = cy + math.sin(angle) * r

        add_particle(
            x,
            y,
            color,
            random.choice([2, 2, 3])
        )


# ==========================================
# LINE
# ==========================================

def line(x1, y1, x2, y2, color, count):

    for _ in range(count):

        t = random.random()

        x = x1 + (x2 - x1) * t
        y = y1 + (y2 - y1) * t

        x += random.uniform(-2, 2)
        y += random.uniform(-2, 2)

        add_particle(
            x,
            y,
            color,
            2
        )


# ==========================================
# DORAEMON HEAD
# ==========================================

# Main blue head
ellipse(
    450,
    350,
    220,
    200,
    "#129FE8",
    1000
)


# Slight darker outer edge
for _ in range(350):

    angle = random.uniform(0, math.pi * 2)

    x = 450 + math.cos(angle) * 220
    y = 350 + math.sin(angle) * 200

    add_particle(
        x,
        y,
        "#087DC2",
        2
    )


# ==========================================
# WHITE FACE
# ==========================================

ellipse(
    450,
    390,
    175,
    145,
    "#FFFFFF",
    650
)


# ==========================================
# EYES
# ==========================================

# White eyes
ellipse(
    390,
    305,
    38,
    55,
    "#FFFFFF",
    180
)

ellipse(
    510,
    305,
    38,
    55,
    "#FFFFFF",
    180
)


# Black pupils
ellipse(
    390,
    320,
    14,
    27,
    "#111111",
    90
)

ellipse(
    510,
    320,
    14,
    27,
    "#111111",
    90
)


# Eye shine
circle(
    386,
    309,
    5,
    "#FFFFFF",
    25
)

circle(
    506,
    309,
    5,
    "#FFFFFF",
    25
)


# ==========================================
# NOSE
# ==========================================

circle(
    450,
    375,
    21,
    "#E93645",
    120
)

circle(
    444,
    369,
    5,
    "#FFFFFF",
    25
)


# ==========================================
# MOUTH
# ==========================================

# Vertical line
line(
    450,
    398,
    450,
    455,
    "#111111",
    80
)


# Left smile
for _ in range(140):

    t = random.random()

    x = 450 - 115 * t
    y = 455 + 45 * (t ** 2)

    add_particle(
        x,
        y,
        "#111111",
        2
    )


# Right smile
for _ in range(140):

    t = random.random()

    x = 450 + 115 * t
    y = 455 + 45 * (t ** 2)

    add_particle(
        x,
        y,
        "#111111",
        2
    )


# ==========================================
# WHISKERS
# ==========================================

# Left
line(340, 370, 220, 345, "#111111", 90)
line(335, 395, 205, 395, "#111111", 90)
line(340, 420, 220, 445, "#111111", 90)

# Right
line(560, 370, 680, 345, "#111111", 90)
line(565, 395, 695, 395, "#111111", 90)
line(560, 420, 680, 445, "#111111", 90)


# ==========================================
# BODY
# ==========================================

ellipse(
    450,
    620,
    155,
    175,
    "#129FE8",
    600
)


# ==========================================
# WHITE BELLY
# ==========================================

ellipse(
    450,
    625,
    115,
    105,
    "#FFFFFF",
    400
)


# ==========================================
# ARMS
# ==========================================

ellipse(
    295,
    610,
    50,
    90,
    "#129FE8",
    220
)

ellipse(
    605,
    610,
    50,
    90,
    "#129FE8",
    220
)


# ==========================================
# RED COLLAR
# ==========================================

line(
    315,
    525,
    585,
    525,
    "#E52B38",
    220
)


# ==========================================
# YELLOW BELL
# ==========================================

circle(
    450,
    555,
    28,
    "#FFD43B",
    150
)

line(
    435,
    557,
    465,
    557,
    "#8A6500",
    45
)


# ==========================================
# POCKET
# ==========================================

ellipse(
    450,
    645,
    78,
    45,
    "#129FE8",
    180
)


# Pocket lower outline
for _ in range(130):

    angle = random.uniform(0, math.pi)

    x = 450 + math.cos(angle) * 78
    y = 645 + math.sin(angle) * 45

    add_particle(
        x,
        y,
        "#087DC2",
        2
    )


# ==========================================
# FEET
# ==========================================

ellipse(
    370,
    790,
    78,
    38,
    "#FFFFFF",
    230
)

ellipse(
    530,
    790,
    78,
    38,
    "#FFFFFF",
    230
)


# ==========================================
# HEART FUNCTION
# ==========================================

def heart(cx, cy, scale, color, count):

    points = []

    for i in range(400):

        t = 2 * math.pi * i / 400

        x = 16 * math.sin(t) ** 3

        y = (
            13 * math.cos(t)
            - 5 * math.cos(2 * t)
            - 2 * math.cos(3 * t)
            - math.cos(4 * t)
        )

        x = cx + x * scale
        y = cy - y * scale

        points.append((x, y))

    for _ in range(count):

        x, y = random.choice(points)

        x += random.uniform(-7, 7)
        y += random.uniform(-7, 7)

        add_particle(
            x,
            y,
            color,
            random.choice([2, 2, 3])
        )


# ==========================================
# CUTE PINK HEARTS
# ==========================================

heart(
    325,
    125,
    4.2,
    "#FF4F9A",
    160
)

heart(
    450,
    75,
    5.5,
    "#FF77B7",
    200
)

heart(
    575,
    125,
    4.2,
    "#FF4F9A",
    160
)


# ==========================================
# RANDOM FLOATING PARTICLES
# ==========================================

for _ in range(450):

    x = random.randint(60, 840)
    y = random.randint(40, 850)

    color = random.choice([
        "#129FE8",
        "#37B7F2",
        "#FFFFFF",
        "#FF4F9A"
    ])

    add_particle(
        x,
        y,
        color,
        random.choice([1, 1, 2])
    )


# ==========================================
# ANIMATION
# ==========================================

def animate():

    for particle in particles:
        particle.update()

    root.after(16, animate)


animate()

root.mainloop()
