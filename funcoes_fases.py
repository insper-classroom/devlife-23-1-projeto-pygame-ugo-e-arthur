import pygame, funcoes
# ugao, a ideia eh que na condicao certa de cada funcao de fase esteja a proxima funcao
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
circulo_roxo = pygame.Rect(50 - 40, 50 - 40, 40 * 2, 40 * 2)
circulo_laranja = pygame.Rect(50 - 42, 50 - 42, 42 * 2, 42 * 2)

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
                if circulo_laranja.collidepoint(mouse_pos) or circulo_roxo.collidepoint(mouse_pos):
                    print('agua') # so um exemplo, neste caso a funcao deve pressionar a funcao fase_2
                if alternativa_A.collidepoint(mouse_pos) or alternativa_B.collidepoint(mouse_pos) or alternativa_C.collidepoint(mouse_pos) or alternativa_D.collidepoint(mouse_pos):
                    print('agua') # e aqui exibir a tela derrota



        tela.fill(branco)
        funcoes.desenha_interface_fases(tela)
        funcoes.desenha_quantidade_moedas(tela)
        tela.blit(nivel, (35, 5))
        tela.blit(A, (185, 250))
        tela.blit(B, (560, 255))
        tela.blit(C, (185, 400))
        tela.blit(D, (560, 390))
        tela.blit(pergunta, (130, 100))
        pygame.display.update()
        



