import pygame
import random
import sys
import math

pygame.init()

# =========================
# CONFIGURACIÓN
# =========================
ANCHO = 600
ALTO = 400
TAM = 20

FPS = 60
VELOCIDAD_INICIAL = 150      # milisegundos entre movimientos
VELOCIDAD_MINIMA = 60        # límite máximo de velocidad
ACELERACION = 5              # cuánto aumenta cada vez que come

NEGRO = (15, 15, 15)
VERDE = (0, 255, 120)
VERDE_CLARO = (0, 255, 180)
ROJO = (255, 70, 70)
BLANCO = (255, 255, 255)

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("🐍 Viborita PRO")
clock = pygame.time.Clock()
fuente = pygame.font.SysFont("consolas", 22)

particulas = []


# =========================
# FUNCIONES
# =========================
def dibujar_grid():
    for x in range(0, ANCHO, TAM):
        pygame.draw.line(pantalla, (25, 25, 25), (x, 0), (x, ALTO))
    for y in range(0, ALTO, TAM):
        pygame.draw.line(pantalla, (25, 25, 25), (0, y), (ANCHO, y))


def generar_comida():
    return (
        random.randrange(0, ANCHO - TAM, TAM),
        random.randrange(0, ALTO - TAM, TAM),
    )


def crear_particulas(x, y):
    for _ in range(15):
        particulas.append([
            x + TAM // 2,
            y + TAM // 2,
            random.uniform(-2, 2),
            random.uniform(-2, 2),
            random.randint(10, 20)
        ])


def actualizar_particulas():
    for p in particulas[:]:
        p[0] += p[2]
        p[1] += p[3]
        p[4] -= 1
        pygame.draw.circle(pantalla, VERDE_CLARO, (int(p[0]), int(p[1])), 3)
        if p[4] <= 0:
            particulas.remove(p)


def mostrar_puntaje(p):
    texto = fuente.render(f"Puntaje: {p}", True, BLANCO)
    pantalla.blit(texto, (10, 10))


def game_over_animacion():
    for alpha in range(0, 255, 8):
        overlay = pygame.Surface((ANCHO, ALTO))
        overlay.set_alpha(alpha)
        overlay.fill((0, 0, 0))
        pantalla.blit(overlay, (0, 0))
        pygame.display.update()
        pygame.time.delay(10)


# =========================
# JUEGO PRINCIPAL
# =========================
def juego():
    x = ANCHO // 2
    y = ALTO // 2

    dx = TAM
    dy = 0

    vibora = []
    longitud = 1

    comida_x, comida_y = generar_comida()

    VELOCIDAD_MOVIMIENTO = VELOCIDAD_INICIAL
    ultimo_movimiento = pygame.time.get_ticks()

    frame = 0

    while True:
        clock.tick(FPS)
        frame += 1

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and dx == 0:
                    dx = -TAM
                    dy = 0
                elif evento.key == pygame.K_RIGHT and dx == 0:
                    dx = TAM
                    dy = 0
                elif evento.key == pygame.K_UP and dy == 0:
                    dy = -TAM
                    dx = 0
                elif evento.key == pygame.K_DOWN and dy == 0:
                    dy = TAM
                    dx = 0

        tiempo_actual = pygame.time.get_ticks()

        # Movimiento controlado por tiempo
        if tiempo_actual - ultimo_movimiento > VELOCIDAD_MOVIMIENTO:
            x += dx
            y += dy
            ultimo_movimiento = tiempo_actual

            # Colisión bordes
            if x < 0 or x >= ANCHO or y < 0 or y >= ALTO:
                game_over_animacion()
                return

            cabeza = [x, y]
            vibora.append(cabeza)

            if len(vibora) > longitud:
                vibora.pop(0)

            # Colisión consigo misma
            for segmento in vibora[:-1]:
                if segmento == cabeza:
                    game_over_animacion()
                    return

            # Comer comida
            if x == comida_x and y == comida_y:
                comida_x, comida_y = generar_comida()
                longitud += 1
                crear_particulas(x, y)

                # Aumentar velocidad progresivamente
                if VELOCIDAD_MOVIMIENTO > VELOCIDAD_MINIMA:
                    VELOCIDAD_MOVIMIENTO -= ACELERACION

        # ================= RENDER =================
        pantalla.fill(NEGRO)
        dibujar_grid()

        # Comida pulsante
        pulso = abs(math.sin(frame * 0.1)) * 5
        pygame.draw.rect(
            pantalla,
            ROJO,
            (comida_x - pulso/2, comida_y - pulso/2, TAM + pulso, TAM + pulso),
            border_radius=8
        )

        # Dibujar vibora con degradado
        for i, segmento in enumerate(vibora):
            intensidad = 255 - (len(vibora) - i) * 5
            color = (0, max(60, intensidad), 120)
            pygame.draw.rect(
                pantalla,
                color,
                (segmento[0], segmento[1], TAM, TAM),
                border_radius=6
            )

        # Ojos
        if vibora:
            cabeza = vibora[-1]
            pygame.draw.circle(pantalla, BLANCO, (cabeza[0] + 5, cabeza[1] + 6), 3)
            pygame.draw.circle(pantalla, BLANCO, (cabeza[0] + TAM - 5, cabeza[1] + 6), 3)

        actualizar_particulas()
        mostrar_puntaje(longitud - 1)

        pygame.display.update()


# =========================
# LOOP GLOBAL
# =========================
while True:
    juego()
