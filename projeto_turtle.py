
import turtle
import math
import random
import time

# CONFIGURAÇÃO DA TELA
tela = turtle.Screen()
tela.setup(900, 700)
tela.bgcolor("#050510")
tela.title("🌈 Arco-íris Pixel por Pixel")
tela.tracer(0)

caneta = turtle.Turtle()
caneta.hideturtle()
caneta.penup()
caneta.speed(0)

# CORES DO ARCO-ÍRIS
cores = [
    "#ff2020",
    "#ff7b00",
    "#ffe600",
    "#20ff40",
    "#00cfff",
    "#304bff",
    "#b52bff"
]

# DESENHAR TEXTO
def escrever(x, y, texto, tamanho, cor):
    caneta.goto(x, y)
    caneta.color(cor)
    caneta.write(
        texto,
        align="center",
        font=("Arial", tamanho, "bold")
    )

# DESENHAR UM PIXEL
def pixel(x, y, cor, tamanho=7):
    caneta.goto(x, y)
    caneta.dot(tamanho, cor)

# FUNDO ESTRELADO
random.seed(10)

for i in range(100):
    x = random.randint(-430, 430)
    y = random.randint(-20, 320)
    pixel(x, y, random.choice([
        "#ffffff", "#6868ff", "#00dfff"
    ]), random.randint(2, 4))

# TÍTULO
escrever(0, 290, "ARCO-ÍRIS PIXEL ART", 22, "#ffffff")
escrever(0, 260, "✨ UM PIXEL DE CADA VEZ ✨", 10, "#a9b5ff")

tela.update()
time.sleep(1)

# DESENHAR O ARCO-ÍRIS
centro_x = 0
centro_y = -175
raio_externo = 265
largura_faixa = 18
passo = 8

for faixa, cor in enumerate(cores):
    raio = raio_externo - faixa * largura_faixa

    # Desenha a faixa de fora para dentro
    for x in range(-raio, raio + 1, passo):
        y_quadrado = raio**2 - x**2

        if y_quadrado >= 0:
            y = math.sqrt(y_quadrado)

            px = centro_x + x
            py = centro_y + y

            # Brilho por trás de cada pixel
            pixel(px, py, cor, 12)
            pixel(px, py, cor, 7)

            tela.update()
            time.sleep(0.002)

# NUVENS PIXELADAS NAS PONTAS
def nuvem(cx, cy):
    pontos = [
        (-30, 0), (-22, 8), (-14, 0),
        (-10, 14), (0, 18), (10, 12),
        (18, 5), (28, 0), (20, -8),
        (8, -10), (-5, -8), (-20, -8)
    ]

    for dx, dy in pontos:
        pixel(cx + dx, cy + dy, "#38aaff", 18)
        pixel(cx + dx, cy + dy, "#ffffff", 10)
        tela.update()
        time.sleep(0.025)

nuvem(-250, -165)
nuvem(250, -165)

# ESTRELAS BRILHANTES
def estrela(x, y, cor):
    pixel(x, y, cor, 12)
    caneta.goto(x, y - 12)
    caneta.color(cor)
    caneta.pensize(2)
    caneta.pendown()
    caneta.goto(x, y + 12)
    caneta.penup()

    caneta.goto(x - 8, y)
    caneta.pendown()
    caneta.goto(x + 8, y)
    caneta.penup()

for x, y, cor in [
    (-330, 50, "#ffe34d"),
    (-180, 180, "#ffffff"),
    (0, 40, "#00dfff"),
    (180, 160, "#ffe34d"),
    (330, 60, "#ffffff"),
    (-350, -30, "#b52bff"),
    (300, -20, "#00dfff")
]:
    estrela(x, y, cor)
    tela.update()
    time.sleep(0.15)

# REFLEXO COLORIDO NO CHÃO
for i, cor in enumerate(cores):
    x = -250 + i * 75

    for linha in range(5):
        for deslocamento in range(-18, 19, 6):
            intensidade = random.choice([0.3, 0.5, 0.8, 1])

            # Simula pixels refletidos na água
            pixel(
                x + deslocamento,
                -215 - linha * 9,
                cor,
                random.randint(2, 6)
            )

        tela.update()
        time.sleep(0.04)

# MENSAGEM FINAL
escrever(0, -285, "PRONTO! 🌈✨", 20, "#ffffff")
escrever(0, -315, "Criado pixel por pixel com Python", 10, "#9da8ff")

tela.update()
turtle.done()
