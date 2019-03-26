import pygame, random, sys
pygame.init()

def draw_spich(screen, x, y):
    screen.blit(spichka, [x, y])

def draw_krest(screen, x, y):
    screen.blit(sgorspichka, [x, y])

def draw_text(N, k, n):
    pygame.draw.rect(screen, white, [0, 0, 700, 55], 0)
    pygame.draw.rect(screen, black, [0, 0, 700, 55], 1)
    font = pygame.font.Font(None, 20)
    text1 = font.render('Начальное количество спичек: ' + str(N), True, black)
    text2 = font.render('Максимальное количество спичек, которые можно сжечь за ход: ' + str(k), True, black)
    text3 = font.render('Текущее количество спичек: ' + str(n), True, black)
    screen.blit(text1, [5, 3])
    screen.blit(text2, [5, 20])
    screen.blit(text3, [5, 38])

def PlayerWin():
    screen.fill(green)
    font = pygame.font.Font(None, 70)
    win = font.render('ВЫ ВЫИГРАЛИ!!!', True, black)
    screen.blit(win, [145, 200])
    font2 = pygame.font.Font(None, 25)
    regames = font2.render('Чтобы начать заново, нажмите ПРОБЕЛ.', True, black)
    screen.blit(regames, [180, 400])

def PlayerLoss():
    screen.fill(red)
    font = pygame.font.Font(None, 70)
    win = font.render('ВЫ ПРОИГРАЛИ!!!', True, black)
    screen.blit(win, [135, 200])
    font2 = pygame.font.Font(None, 25)
    regames = font2.render('Чтобы начать заново, нажмите ПРОБЕЛ.', True, black)
    screen.blit(regames, [180, 400])


black = (0, 0, 0)
white = (250, 250, 250)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 250)
yellow = (255, 255, 0)
cyan = (0, 200, 200)
grey = (190, 190, 190)
orange = (255, 165, 0)
brown = (100, 30, 20)
purple = (160, 32, 240)
DarkGreen = (0, 100, 0)
DarkBrown = (139, 69, 19)
colorit = (150,255,255)


done2 = True

key = [pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6,pygame.K_7]

trip = sys.path[0]

mus = pygame.mixer.Sound(trip + '/4FREE.wav')

size = [700,500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption(trip + '/It is Game')
spichka = pygame.image.load(trip + '/020.png').convert()
sgorspichka = pygame.image.load(trip + '/021.png').convert()

while done2 :
    replay = 0

    n = N = random.randrange(10,65)
    k = random.randrange(3,8)

    xx = 50
    yy = 70
    r = 5
    a = 6
    b = 70

    loss = 0
    win = 0

    player = 0
    comp = 0

    x = []
    y = []

    for i in range(0, N):
        x.append(xx)
        xx += 40
        y.append(yy)
        if xx == 690:
            xx = 50
            yy += 100

    done = True

    mus.play()
    screen.fill(colorit)
    pygame.display.flip()

    for i in range(0,N):
        draw_spich(screen,x[i],y[i])
        pygame.display.flip()


    while done :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
                done2 = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE  and (win == 1 or loss == 1) :
                    replay = 1

            for i in range(0,k):
                if event.type == pygame.KEYUP:
                    if event.key == key[i] :
                        player = i+1

        if win == 0 and loss == 0 :
            draw_text(N, k, n)
            pygame.display.flip()

        if n - player < 0: player = n

        if player != 0 :
            for i in range(n-1,n-1-player,-1):
                draw_krest(screen,x[i],y[i])
                pygame.time.wait(150)
                pygame.display.flip()
        n -= player

        if n <= 0 :
            loss = 1

        if n <= 0:
            loss = 1
        if player != 0 and n != 0:
            if n > k + 1:
                if n % (k + 1) == 1:
                    comp = random.randrange(1, k + 1)
                else:
                    comp = n - ((k + 1) * (n // (k + 1))) - 1
                if n % (k + 1) == 0: comp = k
            else:
                comp = n - 1
            if n == 1: comp = 1

        if player != 0:
            pygame.time.wait(500)

        if comp != 0 :
            for i in range(n-1,n-1-comp,-1):
                draw_krest(screen,x[i],y[i])
                pygame.time.wait(150)
                pygame.display.flip()

        n -= comp

        if n <= 0 and loss == 0:
            win = 1

        comp = 0
        player = 0

        if n <= 0 :
            if win == 1 : PlayerWin()
            else : PlayerLoss()

        if replay == 1:
            done = False
            mus.stop()

        pygame.display.flip()

pygame.quit()