import tkinter as tk
import random
import math

W = 700
H = 700

root = tk.Tk()
root.title("Cute Doraemon Particle Art")
root.configure(bg="black")

canvas = tk.Canvas(
    root,
    width=W,
    height=H,
    bg="black",
    highlightthickness=0
)
canvas.pack()

particles = []


class Particle:
    def __init__(self, x, y, color, size=3):
        self.tx = x
        self.ty = y

        self.x = random.randint(0, W)
        self.y = random.randint(0, H)

        self.color = color
        self.size = size
        self.speed = random.uniform(0.045, 0.075)

        self.dot = canvas.create_oval(
            self.x,
            self.y,
            self.x + size,
            self.y + size,
            fill=color,
            outline=""
        )

    def move(self):
        self.x += (self.tx - self.x) * self.speed
        self.y += (self.ty - self.y) * self.speed

        canvas.coords(
            self.dot,
            self.x,
            self.y,
            self.x + self.size,
            self.y + self.size
        )


def particle(x, y, color, size=3):
    particles.append(Particle(x, y, color, size))


def ellipse(cx, cy, rx, ry, color, amount):
    for _ in range(amount):
        a = random.random() * math.pi * 2
        r = math.sqrt(random.random())

        x = cx + math.cos(a) * rx * r
        y = cy + math.sin(a) * ry * r

        particle(x, y, color, random.choice([2, 2, 3]))


def circle(cx, cy, r, color, amount):
    ellipse(cx, cy, r, r, color, amount)


def line(x1, y1, x2, y2, color, amount):
    for _ in range(amount):
        t = random.random()

        x = x1 + (x2 - x1) * t
        y = y1 + (y2 - y1) * t

        particle(x, y, color, 2)


# ==========================================
# CUTE SMALL DORAEMON
# ==========================================

# HEAD
ellipse(
    350, 300,
    135, 125,
    "#159FE8",
    700
)

# WHITE FACE
ellipse(
    350, 325,
    105, 88,
    "#FFFFFF",
    450
)


# ==========================================
# EYES
# ==========================================

# left eye
ellipse(
    315, 255,
    23, 34,
    "#FFFFFF",
    100
)

# right eye
ellipse(
    385, 255,
    23, 34,
    "#FFFFFF",
    100
)

# pupils
ellipse(
    315, 265,
    9, 17,
    "#111111",
    55
)

ellipse(
    385, 265,
    9, 17,
    "#111111",
    55
)


# ==========================================
# NOSE
# ==========================================

circle(
    350, 305,
    12,
    "#E83242",
    80
)


# ==========================================
# MOUTH
# ==========================================

line(
    350, 318,
    350, 355,
    "#111111",
    45
)

# smile
for _ in range(100):
    t = random.random()

    x = 350 + (t - 0.5) * 120
    y = 355 + 30 * ((2 * t - 1) ** 2)

    particle(
        x,
        y,
        "#111111",
        2
    )


# ==========================================
# WHISKERS
# ==========================================

line(280, 315, 220, 300, "#111111", 45)
line(280, 330, 215, 330, "#111111", 45)
line(280, 345, 220, 360, "#111111", 45)

line(420, 315, 480, 300, "#111111", 45)
line(420, 330, 485, 330, "#111111", 45)
line(420, 345, 480, 360, "#111111", 45)


# ==========================================
# BODY
# ==========================================

ellipse(
    350, 470,
    95, 120,
    "#159FE8",
    420
)


# WHITE BELLY
ellipse(
    350, 475,
    70, 70,
    "#FFFFFF",
    250
)


# ==========================================
# COLLAR
# ==========================================

line(
    270, 400,
    430, 400,
    "#E83242",
    100
)


# ==========================================
# BELL
# ==========================================

circle(
    350, 425,
    17,
    "#FFD43B",
    80
)

line(
    342, 425,
    358, 425,
    "#8A6500",
    20
)


# ==========================================
# POCKET
# ==========================================

ellipse(
    350, 490,
    48, 28,
    "#159FE8",
    100
)


# ==========================================
# ARMS
# ==========================================

ellipse(
    250, 465,
    30, 55,
    "#159FE8",
    130
)

ellipse(
    450, 465,
    30, 55,
    "#159FE8",
    130
)


# ==========================================
# FEET
# ==========================================

ellipse(
    300, 585,
    45, 22,
    "#FFFFFF",
    100
)

ellipse(
    400, 585,
    45, 22,
    "#FFFFFF",
    100
)


# ==========================================
# THREE CUTE HEARTS
# ==========================================

def heart(cx, cy, scale):

    for _ in range(80):

        t = random.random() * math.pi * 2

        x = 16 * math.sin(t) ** 3
        y = (
            13 * math.cos(t)
            - 5 * math.cos(2 * t)
            - 2 * math.cos(3 * t)
            - math.cos(4 * t)
        )

        x = cx + x * scale
        y = cy - y * scale

        particle(
            x + random.uniform(-3, 3),
            y + random.uniform(-3, 3),
            "#FF5C9A",
            2
        )


heart(280, 125, 2.5)
heart(350, 90, 3.2)
heart(420, 125, 2.5)


# ==========================================
# FEW GLOWING FLOATING PARTICLES
# ==========================================

for _ in range(180):

    x = random.randint(100, 600)
    y = random.randint(70, 630)

    particle(
        x,
        y,
        random.choice([
            "#159FE8",
            "#FFFFFF",
            "#FF5C9A"
        ]),
        1
    )


# ==========================================
# ANIMATION
# ==========================================

def animate():

    for p in particles:
        p.move()

    root.after(16, animate)


animate()

root.mainloop()
