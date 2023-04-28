import pygame, funcoes

# --------cores----------------
branco = (255, 255, 255)
preto = (0, 0, 0)
laranja = (230, 115, 0)
laranja_escuro = (200, 100, 0)
laranja_claro = (255, 140, 0)
roxo = (147,112,219)
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
                    fase_2(tela)
                    break
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
        
def fase_2(tela):
    fonte_pergunta = pygame.font.Font('Chendolle.otf',45)
    pergunta =  fonte_pergunta.render('A 1 turma de C.Comp se forma em?.', True, preto)
    fonte_alternativa = pygame.font.Font('Chendolle.otf',70)
    A = fonte_alternativa.render('2023', True, preto)
    B = fonte_alternativa.render('2024', True, preto)
    C = fonte_alternativa.render('2025', True, preto)
    D = fonte_alternativa.render('2026', True, preto)
    fonte_nivel = pygame.font.Font('Chendolle.otf',85)
    nivel = fonte_nivel.render('2.', True, preto)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if  alternativa_C.collidepoint(mouse_pos):
                    fase_3(tela)
                    break
                if alternativa_A.collidepoint(mouse_pos) or alternativa_B.collidepoint(mouse_pos) or alternativa_D.collidepoint(mouse_pos):
                    print('agua') # e aqui exibir a tela derrota



        tela.fill(branco)
        funcoes.desenha_interface_fases(tela)
        funcoes.desenha_quantidade_moedas(tela)
        tela.blit(nivel, (35, 5))
        tela.blit(A, (150, 250))
        tela.blit(B, (515, 255))
        tela.blit(C, (155, 400))
        tela.blit(D, (515, 390))
        tela.blit(pergunta, (400 - pergunta.get_width() // 2, 100))
        pygame.display.update()
        

def fase_3(tela):
    fonte_pergunta = pygame.font.Font('Chendolle.otf',45)
    pergunta =  fonte_pergunta.render('Qual faculdade a grazi nao estudou?.', True, preto)
    fonte_alternativa = pygame.font.Font('Chendolle.otf',70)
    A = fonte_alternativa.render('UNICAMP', True, preto)
    B = fonte_alternativa.render('USP', True, preto)
    C = fonte_alternativa.render('U.OXFORD', True, preto)
    D = fonte_alternativa.render('Federal PE', True, preto)
    fonte_nivel = pygame.font.Font('Chendolle.otf',85)
    nivel = fonte_nivel.render('3.', True, preto)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if  alternativa_A.collidepoint(mouse_pos):
                    fase_4(tela)
                    break
                if alternativa_C.collidepoint(mouse_pos) or alternativa_B.collidepoint(mouse_pos) or alternativa_D.collidepoint(mouse_pos):
                    print('agua') # e aqui exibir a tela derrota



        tela.fill(branco)
        funcoes.desenha_interface_fases(tela)
        funcoes.desenha_quantidade_moedas(tela)
        tela.blit(nivel, (35, 5))
        tela.blit(nivel, (35, 5))
        tela.blit(A, (120, 250))
        tela.blit(B, (535, 255))
        tela.blit(C, (95, 400))
        tela.blit(D, (460, 390))
        tela.blit(pergunta, (400 - pergunta.get_width() // 2, 100))
        pygame.display.update()
        
def fase_4(tela):
    fonte_pergunta = pygame.font.Font('Chendolle.otf',45)
    pergunta =  fonte_pergunta.render('Ano de fundacao do insper?.', True, preto)
    fonte_alternativa = pygame.font.Font('Chendolle.otf',70)
    A = fonte_alternativa.render('2002', True, preto)
    B = fonte_alternativa.render('1987', True, preto)
    C = fonte_alternativa.render('1980', True, preto)
    D = fonte_alternativa.render('1992', True, preto)
    fonte_nivel = pygame.font.Font('Chendolle.otf',85)
    nivel = fonte_nivel.render('4.', True, preto)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if  alternativa_B.collidepoint(mouse_pos):
                    fase_5(tela)
                    break
                if alternativa_A.collidepoint(mouse_pos) or alternativa_C.collidepoint(mouse_pos) or alternativa_D.collidepoint(mouse_pos):
                    print('agua') # e aqui exibir a tela derrota

        tela.fill(branco)
        funcoes.desenha_interface_fases(tela)
        funcoes.desenha_quantidade_moedas(tela)
        tela.blit(nivel, (35, 5))
        tela.blit(nivel, (35, 5))
        tela.blit(A, (120, 250))
        tela.blit(B, (515, 255))
        tela.blit(C, (155, 400))
        tela.blit(D, (515, 390))
        tela.blit(pergunta, (400 - pergunta.get_width() // 2, 100))
        pygame.display.update()
        
def fase_5(tela):
    fonte_pergunta = pygame.font.Font('Chendolle.otf',45)
    pergunta =  fonte_pergunta.render('Atual presidente do insper?.', True, preto)
    fonte_alternativa = pygame.font.Font('Chendolle.otf',70)
    A = fonte_alternativa.render('M.Lisboa', True, preto)
    B = fonte_alternativa.render('A.Toshi', True, preto)
    C = fonte_alternativa.render('M.Knobel', True, preto)
    D = fonte_alternativa.render('Neymar', True, preto)
    fonte_nivel = pygame.font.Font('Chendolle.otf',85)
    nivel = fonte_nivel.render('5.', True, preto)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if  alternativa_C.collidepoint(mouse_pos):
                    fase_6(tela)
                    break
                if alternativa_A.collidepoint(mouse_pos) or alternativa_B.collidepoint(mouse_pos) or alternativa_D.collidepoint(mouse_pos):
                    print('agua') # e aqui exibir a tela derrota



        tela.fill(branco)
        funcoes.desenha_interface_fases(tela)
        funcoes.desenha_quantidade_moedas(tela)
        tela.blit(nivel, (35, 5))
        tela.blit(nivel, (35, 5))
        tela.blit(A, (120, 250))
        tela.blit(B, (515, 255))
        tela.blit(C, (155, 400))
        tela.blit(D, (515, 390))
        tela.blit(pergunta, (400 - pergunta.get_width() // 2, 100))
        pygame.display.update()
        
def fase_6(tela):
    fonte_pergunta = pygame.font.Font('Chendolle.otf',45)
    pergunta =  fonte_pergunta.render('Na pergunta 2, onde era a certa?.', True, preto)
    fonte_alternativa = pygame.font.Font('Chendolle.otf',70)
    A = fonte_alternativa.render('AQUI', True, preto)
    B = fonte_alternativa.render('NESSE', True, preto)
    C = fonte_alternativa.render('HERE', True, preto)
    D = fonte_alternativa.render('NESTE', True, preto)
    fonte_nivel = pygame.font.Font('Chendolle.otf',85)
    nivel = fonte_nivel.render('6.', True, preto)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if  alternativa_D.collidepoint(mouse_pos):
                    fase_7(tela)
                    break
                if alternativa_A.collidepoint(mouse_pos) or alternativa_B.collidepoint(mouse_pos) or alternativa_C.collidepoint(mouse_pos):
                    print('agua') # e aqui exibir a tela derrota
        tela.fill(branco)
        funcoes.desenha_interface_fases(tela)
        funcoes.desenha_quantidade_moedas(tela)
        tela.blit(nivel, (35, 5))
        tela.blit(nivel, (35, 5))
        tela.blit(A, (120, 250))
        tela.blit(B, (515, 255))
        tela.blit(C, (155, 400))
        tela.blit(D, (515, 390))
        tela.blit(pergunta, (400 - pergunta.get_width() // 2, 100))
        pygame.display.update()
        
def fase_7(tela):
    fonte_pergunta = pygame.font.Font('Chendolle.otf',45)
    pergunta =  fonte_pergunta.render('Quantos cursos tem no insper?.', True, preto)
    fonte_alternativa = pygame.font.Font('Chendolle.otf',70)
    A = fonte_alternativa.render('6', True, preto)
    B = fonte_alternativa.render('5', True, preto)
    C = fonte_alternativa.render('8', True, preto)
    D = fonte_alternativa.render('9', True, preto)
    fonte_nivel = pygame.font.Font('Chendolle.otf',85)
    nivel = fonte_nivel.render('7.', True, preto)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if circulo_laranja.collidepoint(mouse_pos) or circulo_roxo.collidepoint(mouse_pos):
                    fase_8(tela)
                    break
                if alternativa_A.collidepoint(mouse_pos) or alternativa_B.collidepoint(mouse_pos) or alternativa_C.collidepoint(mouse_pos) or alternativa_D.collidepoint(mouse_pos):
                    print('agua') # e aqui exibir a tela derrota

        tela.fill(branco)
        funcoes.desenha_interface_fases(tela)
        funcoes.desenha_quantidade_moedas(tela)
        tela.blit(nivel, (35, 5))
        tela.blit(nivel, (35, 5))
        tela.blit(A, (120, 250))
        tela.blit(B, (515, 255))
        tela.blit(C, (155, 400))
        tela.blit(D, (515, 390))
        tela.blit(pergunta, (400 - pergunta.get_width() // 2, 100))
        pygame.display.update()
        
def fase_8(tela):
    fonte_pergunta = pygame.font.Font('Chendolle.otf',45)
    pergunta =  fonte_pergunta.render('Quantas Org Estudantis o Insper tem?.', True, preto)
    fonte_alternativa = pygame.font.Font('Chendolle.otf',70)
    A = fonte_alternativa.render('39', True, preto)
    B = fonte_alternativa.render('40', True, preto)
    C = fonte_alternativa.render('38', True, preto)
    D = fonte_alternativa.render('41', True, preto)
    fonte_nivel = pygame.font.Font('Chendolle.otf',85)
    nivel = fonte_nivel.render('8.', True, preto)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if  alternativa_A.collidepoint(mouse_pos):
                    fase_9(tela)
                    break
                if alternativa_C.collidepoint(mouse_pos) or alternativa_B.collidepoint(mouse_pos) or alternativa_D.collidepoint(mouse_pos):
                    print('agua') # e aqui exibir a tela derrota
        tela.fill(branco)
        funcoes.desenha_interface_fases(tela)
        funcoes.desenha_quantidade_moedas(tela)
        tela.blit(nivel, (35, 5))
        tela.blit(nivel, (35, 5))
        tela.blit(A, (120, 250))
        tela.blit(B, (515, 255))
        tela.blit(C, (155, 400))
        tela.blit(D, (515, 390))
        tela.blit(pergunta, (400 - pergunta.get_width() // 2, 100))
        pygame.display.update()
        
def fase_9(tela):
    fonte_pergunta = pygame.font.Font('Chendolle.otf',45)
    pergunta =  fonte_pergunta.render('ONDE A PRO DANI FEZ MESTRADO?.', True, preto)
    fonte_alternativa = pygame.font.Font('Chendolle.otf',70)
    A = fonte_alternativa.render('UNICAMP', True, preto)
    B = fonte_alternativa.render('USP', True, preto)
    C = fonte_alternativa.render('FESPSP', True, preto)
    D = fonte_alternativa.render('PUC', True, preto)
    fonte_nivel = pygame.font.Font('Chendolle.otf',85)
    nivel = fonte_nivel.render('9.', True, preto)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if  alternativa_B.collidepoint(mouse_pos):
                    fase_10(tela)
                    break
                if alternativa_A.collidepoint(mouse_pos) or alternativa_C.collidepoint(mouse_pos) or alternativa_D.collidepoint(mouse_pos):
                    print('agua') # e aqui exibir a tela derrota
        tela.fill(branco)
        funcoes.desenha_interface_fases(tela)
        funcoes.desenha_quantidade_moedas(tela)
        tela.blit(nivel, (35, 5))
        tela.blit(nivel, (35, 5))
        tela.blit(A, (120, 250))
        tela.blit(B, (515, 255))
        tela.blit(C, (155, 400))
        tela.blit(D, (515, 390))
        tela.blit(pergunta, (400 - pergunta.get_width() // 2, 100))
        pygame.display.update()
        
def fase_10(tela):
    fonte_pergunta = pygame.font.Font('Chendolle.otf',45)
    pergunta =  fonte_pergunta.render('ONDE ERA A CERTA DA QUESTAO 4?.', True, preto)
    fonte_alternativa = pygame.font.Font('Chendolle.otf',70)
    A = fonte_alternativa.render('Direita', True, preto)
    B = fonte_alternativa.render('Baixo', True, preto)
    C = fonte_alternativa.render('Esquerda', True, preto)
    D = fonte_alternativa.render('Cima', True, preto)
    fonte_nivel = pygame.font.Font('Chendolle.otf',85)
    nivel = fonte_nivel.render('10.', True, preto)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if  alternativa_D.collidepoint(mouse_pos):
                    fase_11(tela)
                    break
                if alternativa_A.collidepoint(mouse_pos) or alternativa_B.collidepoint(mouse_pos) or alternativa_C.collidepoint(mouse_pos):
                    print('agua') # e aqui exibir a tela derrota
        tela.fill(branco)
        funcoes.desenha_interface_fases(tela)
        funcoes.desenha_quantidade_moedas(tela)
        tela.blit(nivel, (35, 5))
        tela.blit(nivel, (35, 5))
        tela.blit(A, (120, 250))
        tela.blit(B, (515, 255))
        tela.blit(C, (155, 400))
        tela.blit(D, (515, 390))
        tela.blit(pergunta, (400 - pergunta.get_width() // 2, 100))
        pygame.display.update()
        
def fase_11(tela):
    fonte_pergunta = pygame.font.Font('Chendolle.otf',45)
    pergunta =  fonte_pergunta.render('Qual nao tem no 4* semestre?.', True, preto)
    fonte_alternativa = pygame.font.Font('Chendolle.otf',70)
    A = fonte_alternativa.render('MACHINE L.', True, preto)
    B = fonte_alternativa.render('HARDWARE', True, preto)
    C = fonte_alternativa.render('ALGORITIMO', True, preto)
    D = fonte_alternativa.render('DEVLIFE', True, preto)
    fonte_nivel = pygame.font.Font('Chendolle.otf',85)
    nivel = fonte_nivel.render('11.', True, preto)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if  alternativa_D.collidepoint(mouse_pos):
                    fase_12(tela)
                    break
                if alternativa_A.collidepoint(mouse_pos) or alternativa_B.collidepoint(mouse_pos) or alternativa_C.collidepoint(mouse_pos):
                    print('agua') # e aqui exibir a tela derrota
        tela.fill(branco)
        funcoes.desenha_interface_fases(tela)
        funcoes.desenha_quantidade_moedas(tela)
        tela.blit(nivel, (35, 5))
        tela.blit(nivel, (35, 5))
        tela.blit(A, (120, 250))
        tela.blit(B, (515, 255))
        tela.blit(C, (155, 400))
        tela.blit(D, (515, 390))
        tela.blit(pergunta, (400 - pergunta.get_width() // 2, 100))
        pygame.display.update()
        
def fase_12(tela):
    fonte_pergunta = pygame.font.Font('Chendolle.otf',45)
    pergunta =  fonte_pergunta.render('PRINCIPAL LINGUAGEM DE IA?.', True, preto)
    fonte_alternativa = pygame.font.Font('Chendolle.otf',70)
    A = fonte_alternativa.render('C', True, preto)
    B = fonte_alternativa.render('JAVA', True, preto)
    C = fonte_alternativa.render('PYTHON', True, preto)
    D = fonte_alternativa.render('PHP', True, preto)
    fonte_nivel = pygame.font.Font('Chendolle.otf',85)
    nivel = fonte_nivel.render('12.', True, preto)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if  alternativa_C.collidepoint(mouse_pos):
                    fase_13(tela)
                    break
                if alternativa_A.collidepoint(mouse_pos) or alternativa_B.collidepoint(mouse_pos) or alternativa_D.collidepoint(mouse_pos):
                    print('agua') # e aqui exibir a tela derrota
        tela.fill(branco)
        funcoes.desenha_interface_fases(tela)
        funcoes.desenha_quantidade_moedas(tela)
        tela.blit(nivel, (35, 5))
        tela.blit(nivel, (35, 5))
        tela.blit(A, (120, 250))
        tela.blit(B, (515, 255))
        tela.blit(C, (155, 400))
        tela.blit(D, (515, 390))
        tela.blit(pergunta, (400 - pergunta.get_width() // 2, 100))
        pygame.display.update()
        
def fase_13(tela):
    fonte_pergunta = pygame.font.Font('Chendolle.otf',45)
    pergunta =  fonte_pergunta.render('SISTEMA OPERACIONAL DO PC DA SALA 312?.', True, preto)
    fonte_alternativa = pygame.font.Font('Chendolle.otf',70)
    A = fonte_alternativa.render('LINUX', True, preto)
    B = fonte_alternativa.render('MACOS', True, preto)
    C = fonte_alternativa.render('WINDOWS', True, preto)
    D = fonte_alternativa.render('NAO TEM', True, preto)
    fonte_nivel = pygame.font.Font('Chendolle.otf',85)
    nivel = fonte_nivel.render('13.', True, preto)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if  alternativa_A.collidepoint(mouse_pos):
                    fase_14(tela)
                    break
                if alternativa_C.collidepoint(mouse_pos) or alternativa_B.collidepoint(mouse_pos) or alternativa_D.collidepoint(mouse_pos):
                    print('agua') # e aqui exibir a tela derrota

        tela.fill(branco)
        funcoes.desenha_interface_fases(tela)
        funcoes.desenha_quantidade_moedas(tela)
        tela.blit(nivel, (35, 5))
        tela.blit(nivel, (35, 5))
        tela.blit(A, (120, 250))
        tela.blit(B, (515, 255))
        tela.blit(C, (155, 400))
        tela.blit(D, (515, 390))
        tela.blit(pergunta, (400 - pergunta.get_width() // 2, 100))
        pygame.display.update()
        
def fase_14(tela):
    fonte_pergunta = pygame.font.Font('Chendolle.otf',45)
    pergunta =  fonte_pergunta.render('QUANTAS MESAS TEM NA SALA DE 312?.', True, preto)
    fonte_alternativa = pygame.font.Font('Chendolle.otf',70)
    A = fonte_alternativa.render('25', True, preto)
    B = fonte_alternativa.render('26', True, preto)
    C = fonte_alternativa.render('27', True, preto)
    D = fonte_alternativa.render('28', True, preto)
    fonte_nivel = pygame.font.Font('Chendolle.otf',85)
    nivel = fonte_nivel.render('14.', True, preto)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if  alternativa_D.collidepoint(mouse_pos):
                    fase_3(tela)
                    break
                if alternativa_A.collidepoint(mouse_pos) or alternativa_B.collidepoint(mouse_pos) or alternativa_C.collidepoint(mouse_pos):
                    print('agua') # e aqui exibir a tela derrota



        tela.fill(branco)
        funcoes.desenha_interface_fases(tela)
        funcoes.desenha_quantidade_moedas(tela)
        tela.blit(nivel, (35, 5))
        tela.blit(nivel, (35, 5))
        tela.blit(A, (120, 250))
        tela.blit(B, (515, 255))
        tela.blit(C, (155, 400))
        tela.blit(D, (515, 390))
        tela.blit(pergunta, (400 - pergunta.get_width() // 2, 100))
        pygame.display.update()
        
# def fase_3(tela):
#     fonte_pergunta = pygame.font.Font('Chendolle.otf',45)
#     pergunta =  fonte_pergunta.render('Qual faculdade a grazi nao estudou?.', True, preto)
#     fonte_alternativa = pygame.font.Font('Chendolle.otf',70)
#     A = fonte_alternativa.render('UNICAMP', True, preto)
#     B = fonte_alternativa.render('USP', True, preto)
#     C = fonte_alternativa.render('U.OXFORD', True, preto)
#     D = fonte_alternativa.render('Federal PE', True, preto)
#     fonte_nivel = pygame.font.Font('Chendolle.otf',85)
#     nivel = fonte_nivel.render('3.', True, preto)
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_pos = event.pos
#                 if  alternativa_C.collidepoint(mouse_pos):
#                     fase_3(tela)
#                     break
#                 if alternativa_A.collidepoint(mouse_pos) or alternativa_B.collidepoint(mouse_pos) or alternativa_D.collidepoint(mouse_pos):
#                     print('agua') # e aqui exibir a tela derrota



#         tela.fill(branco)
#         funcoes.desenha_interface_fases(tela)
#         funcoes.desenha_quantidade_moedas(tela)
#         tela.blit(nivel, (35, 5))
#         tela.blit(nivel, (35, 5))
#         tela.blit(A, (120, 250))
#         tela.blit(B, (515, 255))
#         tela.blit(C, (155, 400))
#         tela.blit(D, (515, 390))
#         tela.blit(pergunta, (400 - pergunta.get_width() // 2, 100))
#         pygame.display.update()
        
