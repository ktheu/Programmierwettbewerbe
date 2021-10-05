import pygame, sys, random
pygame.init()

def getX(k):  
  # returns: x-Koordinate der k-ten Zelle 
  return abstandZumRand + (k % N) * (abstand + size)

def getY(k):
  # returns: y-Koordinate der k-ten Zelle
  return abstandZumRand + int(k / N) * (abstand + size);

def innerhalb(x, y, k):
  # True, wenn die Position x und y innerhalb der k-ten Zelle ist
  xk = getX(k);
  yk = getY(k);
  return xk <= x <= xk + size and yk <= y <= yk + size;

def nb(k):
    # returns: eine Liste mit den Indizes der Nachbarn von Index k
    tmp = []
    if (k + N) < N * N: tmp.append(k + N);
    if (k - N) >= 0: tmp.append(k - N);
    if k % N < N - 1: tmp.append(k + 1);
    if k % N > 0: tmp.append(k - 1);
    return tmp

def obenlinks(k):
    # returns Liste mit den Indizes der Zellen oben links
    return [i for i in range(N*N) if i<= k and i%N <= k%N ]
     

def randomStart():
    for i in range(N*N):
        on[i] = True if random.random() < 0.5 else False

GELB  = (255,255, 0)
GRAU = (200,200,200)
SCHWARZ = (0,0,0)

N = 6           # N x N Zellen
modus = 0       # 0 - Nachbarn, 1 - obenlinks
abstand = 20    # Abstand der Quadrate untereinander
abstandZumRand = 40;
size = 50       # Seitenlänge der Quadrate
screenBreite = 2 * abstandZumRand + N * size + (N - 1) * abstand

on = [False] * (N*N)     # on = True => GELB

screen = pygame.display.set_mode((screenBreite, screenBreite))
pygame.display.set_caption("LAMA")
clock = pygame.time.Clock()
randomStart()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            for i in range(N * N):
                if innerhalb(mouseX, mouseY, i):
                    if modus == 0:        # Nachbarn
                        on[i] = not on[i]
                        for k in nb(i):
                            on[k] = not on[k]
                    elif modus == 1:      # obenlinks
                        for k in obenlinks(i):
                            on[k] = not on[k]
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                randomStart()
    # display
    screen.fill(GRAU)
    
    for i in range(N * N):
        farbe = GELB if on[i] else SCHWARZ
        pygame.draw.rect(screen, farbe, [getX(i), getY(i), size, size], 0)

    pygame.display.flip()
    clock.tick(60)



 