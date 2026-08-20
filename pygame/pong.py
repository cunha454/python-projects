import pygame

pygame.init()
pygame.font.init()

tela = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
FPS = 60

LARGURA = tela.get_width()
ALTURA = tela.get_height()

CENTRO_X = LARGURA // 2
CENTRO_Y = ALTURA // 2

jogador_1 = pygame.Rect(0, 0, 30, 150)
jogador_1_velocidade = 0
jogador_1_pontos = 0

jogador_2 = pygame.Rect(1250, 0, 30, 150)
jogador_2_pontos = 0

bola = pygame.Rect(0, 0, 15, 15)
bola.center = (CENTRO_X, CENTRO_Y)

bola_direcao_x = 5
bola_direcao_y = 5

fonte = pygame.font.Font(None, 50)

placar_jogador_1 = fonte.render(str(jogador_1_pontos), True, "white")
placar_jogador_2 = fonte.render(str(jogador_2_pontos), True, "white")

derrota_som = pygame.mixer.Sound("pygame/assets/efeitos_sonoros/fah.mp3")

cena = "menu"
tempo_game_over = 0

loop = True
while loop:
    if cena == "jogando":
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                loop = False

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_w:
                    jogador_1_velocidade = -5

                if evento.key == pygame.K_s:
                    jogador_1_velocidade = 5

                if evento.key == pygame.K_ESCAPE:
                    cena = "menu"

        jogador_1.y += jogador_1_velocidade

        if jogador_1.y <= 0:
            jogador_1.y = 0

        elif jogador_1.y >= ALTURA - jogador_1.height:
            jogador_1.y = ALTURA - jogador_1.height

        if bola.colliderect(jogador_1) or bola.colliderect(jogador_2):
            bola_direcao_x *= -1

        bola.x += bola_direcao_x
        bola.y += bola_direcao_y

        if bola.x <= 0:
            jogador_2_pontos += 1
            derrota_som.play()

            placar_jogador_2 = fonte.render(str(jogador_2_pontos), True, "white")

            bola.center = (CENTRO_X, CENTRO_Y)
            bola_direcao_x *= -1

        elif bola.x >= LARGURA:
            jogador_1_pontos += 1
            derrota_som.play()

            placar_jogador_1 = fonte.render(str(jogador_1_pontos), True, "white")

            bola.center = (CENTRO_X, CENTRO_Y)
            bola_direcao_x *= -1

        if bola.y <= 0 or bola.y >= ALTURA - bola.height:
            bola_direcao_y *= -1

        jogador_2.y = bola.y

        if jogador_2.y <= 0:
            jogador_2.y = 0

        elif jogador_2.y >= ALTURA - jogador_2.height:
            jogador_2.y = ALTURA - jogador_2.height

        if jogador_1_pontos >= 3 or jogador_2_pontos >= 3:
            tempo_game_over = pygame.time.get_ticks()
            cena = "game_over"

        tela.fill((0, 0, 0))

        pygame.draw.rect(tela, "white", jogador_1)
        pygame.draw.rect(tela, "white", jogador_2)

        pygame.draw.circle(tela, "white", bola.center, 8)

        rect_jogador_1 = placar_jogador_1.get_rect(
            center=(CENTRO_X - 50, 50)
        )

        rect_jogador_2 = placar_jogador_2.get_rect(
            center=(CENTRO_X + 50, 50)
        )

        tela.blit(placar_jogador_1, rect_jogador_1)
        tela.blit(placar_jogador_2, rect_jogador_2)

    elif cena == "game_over":
        tela.fill((0, 0, 0))

        texto_game_over = fonte.render("GAME OVER", True, "white")

        rect_game_over = texto_game_over.get_rect(
            center=(CENTRO_X, CENTRO_Y)
        )

        tela.blit(texto_game_over, rect_game_over)

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                loop = False

        if pygame.time.get_ticks() - tempo_game_over >= 5000:

            jogador_1_pontos = 0
            jogador_2_pontos = 0

            placar_jogador_1 = fonte.render(str(jogador_1_pontos), True, "white")
            placar_jogador_2 = fonte.render(str(jogador_2_pontos), True, "white")

            cena = "menu"

    elif cena == "menu":

        tela.fill((0, 0, 0))

        texto_menu = fonte.render("PONG", True, "white")

        rect_menu = texto_menu.get_rect(
            center=(CENTRO_X, CENTRO_Y)
        )

        tela.blit(texto_menu, rect_menu)

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                loop = False

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_SPACE:

                    jogador_1_pontos = 0
                    jogador_2_pontos = 0

                    placar_jogador_1 = fonte.render(str(jogador_1_pontos), True, "white")
                    placar_jogador_2 = fonte.render(str(jogador_2_pontos), True, "white")

                    jogador_1.y = 0
                    jogador_2.y = 0

                    bola.center = (CENTRO_X, CENTRO_Y)

                    bola_direcao_x = 5
                    bola_direcao_y = 5

                    jogador_1_velocidade = 0

                    cena = "jogando"

    pygame.display.flip()
    clock.tick(FPS)
    
pygame.quit()