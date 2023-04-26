import pygame, funcoes
# --------cores----------------
branco = (255, 255, 255)
preto = (0, 0, 0)
laranja = (230, 115, 0)
laranja_escuro = (200, 100, 0)
laranja_claro = (255, 140, 0)
roxo = (147,112,219)
# --------cores----------------
# --------alternativas------------------------
alternativa_A = pygame.Rect(60, 250, 310, 80)
alternativa_B = pygame.Rect(430, 250, 310, 80)
alternativa_C = pygame.Rect(60, 390, 310, 80)
alternativa_D = pygame.Rect(430, 390, 310, 80)
# --------alternativas------------------------
def fase_1(tela):
    fonte_pergunta = pygame.font.Font('Chendolle.otf',45)
    pergunta =  fonte_pergunta.render('Qual dia do mes o Toshi nasceu?.', True, preto)
    fonte_alternativa = pygame.font.Font('Chendolle.otf',70)
    A = fonte_alternativa.render('02', True, preto)
    B = fonte_alternativa.render('20', True, preto)
    C = fonte_alternativa.render('19', True, preto)
    D = fonte_alternativa.render('08', True, preto)
    fonte_nivel = pygame.font.Font('Chendolle.otf',85)
    nivel = fonte_nivel.render('1.', True, preto)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if nivel.collidepoint(mouse_pos):
                    funcoes.desenha_interface_fases
                    pygame.display.update(tela)

        tela.fill(branco)
        funcoes.desenha_interface_fases(tela)
        tela.blit(nivel, (35, 5))
        tela.blit(A, (185, 250))
        tela.blit(B, (560, 255))
        tela.blit(C, (185, 400))
        tela.blit(D, (560, 390))
        tela.blit(pergunta, (130, 100))
        pygame.display.update()
        




