import pygame, funcoes, Main_Menu

#--------sons-----------
pygame.mixer.init()
som_errou = pygame.mixer.Sound('./docs/buzzer-or-wrong-answer-20582.mp3')
som_errou.set_volume(0.5)
som_acertou = pygame.mixer.Sound('./docs/correct-6033.wav')
som_acertou.set_volume(0.5)


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
    pergunta =  fonte_pergunta.render('Qual dia do mes o Toshi nasceu?', True, preto)
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
                    som_acertou.play()
                    fase_2(tela)
                    break
                if alternativa_A.collidepoint(mouse_pos) or alternativa_B.collidepoint(mouse_pos) or alternativa_C.collidepoint(mouse_pos) or alternativa_D.collidepoint(mouse_pos):
                    som_errou.play()
                    funcoes.derrota_0(tela)

  
        tela.fill(branco)
        funcoes.desenha_interface_fases(tela)
        funcoes.desenha_quantidade_moedas_0(tela)
        tela.blit(nivel, (35, 5))
        tela.blit(A, (185, 250))
        tela.blit(B, (560, 255))
        tela.blit(C, (185, 400))
        tela.blit(D, (560, 390))
        tela.blit(pergunta, (130, 100))
        pygame.display.update()
        
def fase_2(tela):
    fonte_pergunta = pygame.font.Font('Chendolle.otf',45)
    pergunta =  fonte_pergunta.render('A primeira turma de C.Comp se forma em?', True, preto)
    fonte_alternativa = pygame.font.Font('Chendolle.otf',70)
    A = fonte_alternativa.render('2023', True, preto)
    B = fonte_alternativa.render('2024', True, preto)
    C = fonte_alternativa.render('2026', True, preto)
    D = fonte_alternativa.render('2025', True, preto)
    fonte_nivel = pygame.font.Font('Chendolle.otf',85)
    nivel = fonte_nivel.render('2.', True, preto)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if  alternativa_D.collidepoint(mouse_pos):
                    som_acertou.play()
                    fase_3(tela)
                    break
                if alternativa_A.collidepoint(mouse_pos) or alternativa_B.collidepoint(mouse_pos) or alternativa_C.collidepoint(mouse_pos):
                    som_errou.play()
                    funcoes.derrota_0(tela)



        tela.fill(branco)
        funcoes.desenha_interface_fases(tela)
        funcoes.desenha_quantidade_moedas_0(tela)
        tela.blit(nivel, (22, 1))
        tela.blit(A, (150, 250))
        tela.blit(B, (515, 255))
        tela.blit(C, (150, 390))
        tela.blit(D, (515, 390))
        tela.blit(pergunta, (400 - pergunta.get_width() // 2, 100))
        pygame.display.update()
        

def fase_3(tela):
    fonte_pergunta = pygame.font.Font('Chendolle.otf',45)
    pergunta =  fonte_pergunta.render('Qual faculdade a grazi nao estudou?', True, preto)
    fonte_alternativa = pygame.font.Font('Chendolle.otf',70)
    A = fonte_alternativa.render('UNICAMP', True, preto)
    B = fonte_alternativa.render('USP', True, preto)
    C = fonte_alternativa.render('U.OXFORD', True, preto)
    D = fonte_alternativa.render('Federal PE', True, preto)
    fonte_nivel = pygame.font.Font('Chendolle.otf',80)
    nivel = fonte_nivel.render('3.', True, preto)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if  alternativa_A.collidepoint(mouse_pos):
                    som_acertou.play()
                    fase_4(tela)
                    break
                if alternativa_C.collidepoint(mouse_pos) or alternativa_B.collidepoint(mouse_pos) or alternativa_D.collidepoint(mouse_pos):
                    som_errou.play()
                    funcoes.derrota_0(tela)



        tela.fill(branco)
        funcoes.desenha_interface_fases(tela)
        funcoes.desenha_quantidade_moedas_0(tela)
        tela.blit(nivel, (25, 5))
        tela.blit(A, (95, 255))
        tela.blit(B, (535, 255))
        tela.blit(C, (85, 395))
        tela.blit(D, (445, 398))
        tela.blit(pergunta, (400 - pergunta.get_width() // 2, 100))
        pygame.display.update()
        
def fase_4(tela):
    fonte_pergunta = pygame.font.Font('Chendolle.otf',45)
    pergunta =  fonte_pergunta.render('Qual foi o ano de fundacao do ibmec?', True, preto)
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
                    som_acertou.play()
                    fase_5(tela)
                    break
                if alternativa_A.collidepoint(mouse_pos) or alternativa_C.collidepoint(mouse_pos) or alternativa_D.collidepoint(mouse_pos):
                    som_errou.play()
                    funcoes.derrota_0(tela)

        tela.fill(branco)
        funcoes.desenha_interface_fases(tela)
        funcoes.desenha_quantidade_moedas_0(tela)
        tela.blit(nivel, (20, 5))
        tela.blit(A, (146, 250))
        tela.blit(B, (535, 255))
        tela.blit(C, (155, 395))
        tela.blit(D, (535, 395))
        tela.blit(pergunta, (400 - pergunta.get_width() // 2, 100))
        pygame.display.update()
        
def fase_5(tela):
    fonte_pergunta = pygame.font.Font('Chendolle.otf',45)
    pergunta =  fonte_pergunta.render('Qual o atual presidente do insper?', True, preto)
    fonte_alternativa = pygame.font.Font('Chendolle.otf',70)
    A = fonte_alternativa.render('M.Lisboa', True, preto)
    B = fonte_alternativa.render('A.Toshi', True, preto)
    C = fonte_alternativa.render('M.Knobel', True, preto)
    D = fonte_alternativa.render('Neymar', True, preto)
    fonte_nivel = pygame.font.Font('Chendolle.otf',79)
    nivel = fonte_nivel.render('5.', True, preto)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if  alternativa_C.collidepoint(mouse_pos):
                    som_acertou.play()
                    fase_6(tela)
                    break
                if alternativa_A.collidepoint(mouse_pos) or alternativa_B.collidepoint(mouse_pos) or alternativa_D.collidepoint(mouse_pos):
                    som_errou.play()
                    funcoes.derrota_0(tela)



        tela.fill(branco)
        funcoes.desenha_interface_fases(tela)
        funcoes.desenha_quantidade_moedas_0(tela)
        tela.blit(nivel, (26, 8))
        tela.blit(A, (112, 252))
        tela.blit(B, (487, 255))
        tela.blit(C, (112, 395))
        tela.blit(D, (500, 390))
        tela.blit(pergunta, (400 - pergunta.get_width() // 2, 100))
        pygame.display.update()
        
def fase_6(tela):
    fonte_pergunta = pygame.font.Font('Chendolle.otf',45)
    pergunta =  fonte_pergunta.render('Na pergunta 2, onde era a certa?', True, preto)
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
                    som_acertou.play()
                    fase_7(tela)
                    break
                if alternativa_A.collidepoint(mouse_pos) or alternativa_B.collidepoint(mouse_pos) or alternativa_C.collidepoint(mouse_pos):
                    som_errou.play()
                    funcoes.derrota_1(tela)

        tela.fill(branco)
        funcoes.desenha_interface_fases(tela)
        funcoes.desenha_quantidade_moedas_1(tela)
        tela.blit(nivel, (25, 2))
        tela.blit(A, (148, 260))
        tela.blit(B, (505, 255))
        tela.blit(C, (143, 395))
        tela.blit(D, (505, 395))
        tela.blit(pergunta, (400 - pergunta.get_width() // 2, 100))
        pygame.display.update()
        
def fase_7(tela):
    fonte_pergunta = pygame.font.Font('Chendolle.otf',45)
    pergunta =  fonte_pergunta.render('Quantos cursos tem no insper?', True, preto)
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
                    som_acertou.play()
                    fase_8(tela)
                    break
                if alternativa_A.collidepoint(mouse_pos) or alternativa_B.collidepoint(mouse_pos) or alternativa_C.collidepoint(mouse_pos) or alternativa_D.collidepoint(mouse_pos):
                    som_errou.play()
                    funcoes.derrota_1(tela)

        tela.fill(branco)
        funcoes.desenha_interface_fases(tela)
        funcoes.desenha_quantidade_moedas_1(tela)
        tela.blit(nivel, (23, 4))
        tela.blit(A, (195, 256))
        tela.blit(B, (562, 255))
        tela.blit(C, (195, 390))
        tela.blit(D, (562, 400))
        tela.blit(pergunta, (400 - pergunta.get_width() // 2, 100))
        pygame.display.update()
        
def fase_8(tela):
    fonte_pergunta = pygame.font.Font('Chendolle.otf',45)
    pergunta =  fonte_pergunta.render('Quantas Orgs. Estudantis o Insper tem?', True, preto)
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
                    som_acertou.play()
                    fase_9(tela)
                    break
                if alternativa_C.collidepoint(mouse_pos) or alternativa_B.collidepoint(mouse_pos) or alternativa_D.collidepoint(mouse_pos):
                    som_errou.play()
                    funcoes.derrota_1(tela)

        tela.fill(branco)
        funcoes.desenha_interface_fases(tela)
        funcoes.desenha_quantidade_moedas_1(tela)
        tela.blit(nivel, (29, 1))
        tela.blit(A, (175, 255))
        tela.blit(B, (550, 255))
        tela.blit(C, (175, 395))
        tela.blit(D, (550, 394))
        tela.blit(pergunta, (400 - pergunta.get_width() // 2, 100))
        pygame.display.update()
        
def fase_9(tela):
    fonte_pergunta = pygame.font.Font('Chendolle.otf',45)
    pergunta =  fonte_pergunta.render('ONDE A PRO DANI FEZ MESTRADO?', True, preto)
    fonte_alternativa = pygame.font.Font('Chendolle.otf',70)
    A = fonte_alternativa.render('UNICAMP', True, preto)
    B = fonte_alternativa.render('USP', True, preto)
    C = fonte_alternativa.render('FESPSP', True, preto)
    D = fonte_alternativa.render('PUC', True, preto)
    fonte_nivel = pygame.font.Font('Chendolle.otf',75)
    nivel = fonte_nivel.render('9.', True, preto)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if  alternativa_B.collidepoint(mouse_pos):
                    som_acertou.play()
                    fase_10(tela)
                    break
                if alternativa_A.collidepoint(mouse_pos) or alternativa_C.collidepoint(mouse_pos) or alternativa_D.collidepoint(mouse_pos):
                    som_errou.play()
                    funcoes.derrota_1(tela)

        tela.fill(branco)
        funcoes.desenha_interface_fases(tela)
        funcoes.desenha_quantidade_moedas_1(tela)
        tela.blit(nivel, (25, 8))
        tela.blit(A, (95, 255))
        tela.blit(B, (535, 255))
        tela.blit(C, (115, 395))
        tela.blit(D, (535, 397))
        tela.blit(pergunta, (400 - pergunta.get_width() // 2, 100))
        pygame.display.update()
        
def fase_10(tela):
    fonte_pergunta = pygame.font.Font('Chendolle.otf',45)
    pergunta =  fonte_pergunta.render("O que a letra 'R' significa no CRAP?", True, preto)
    fonte_alternativa = pygame.font.Font('Chendolle.otf',65)
    A = fonte_alternativa.render('Recorrencia', True, preto)
    B = fonte_alternativa.render('Ritmo', True, preto)
    C = fonte_alternativa.render('Repeticao', True, preto)
    D = fonte_alternativa.render('Rotacao', True, preto)
    fonte_nivel = pygame.font.Font('Chendolle.otf',70)
    nivel = fonte_nivel.render('10.', True, preto)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                    
                if  alternativa_C.collidepoint(mouse_pos):
                    som_acertou.play()
                    fase_11(tela)
                    break
                if alternativa_A.collidepoint(mouse_pos) or alternativa_B.collidepoint(mouse_pos) or alternativa_D.collidepoint(mouse_pos):
                    som_errou.play()
                    funcoes.derrota_1(tela)

        tela.fill(branco)
        funcoes.desenha_interface_fases(tela)
        funcoes.desenha_quantidade_moedas_1(tela)
        tela.blit(nivel, (16, 6))
        tela.blit(A, (83, 259))
        tela.blit(B, (515, 255))
        tela.blit(C, (100, 396))
        tela.blit(D, (488, 395))
        tela.blit(pergunta, (400 - pergunta.get_width() // 2, 100))
        pygame.display.update()
        
def fase_11(tela):
    fonte_pergunta = pygame.font.Font('Chendolle.otf',45)
    pergunta =  fonte_pergunta.render('Qual das materias nao esta no curso de Ccomp?', True, preto)
    fonte_alternativa = pygame.font.Font('Chendolle.otf',60)
    A = fonte_alternativa.render('ALGORITIMO', True, preto)
    B = fonte_alternativa.render('HARDWARE', True, preto)
    C = fonte_alternativa.render('Cyberlearning', True, preto)
    D = fonte_alternativa.render('MACHINE L', True, preto)
    fonte_nivel = pygame.font.Font('Chendolle.otf',85)
    nivel = fonte_nivel.render('11.', True, preto)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if  alternativa_C.collidepoint(mouse_pos):
                    som_acertou.play()
                    fase_12(tela)
                    break
                if alternativa_A.collidepoint(mouse_pos) or alternativa_B.collidepoint(mouse_pos) or alternativa_D.collidepoint(mouse_pos):
                    som_errou.play()
                    funcoes.derrota_2(tela)

        tela.fill(branco)
        funcoes.desenha_interface_fases(tela)
        funcoes.desenha_quantidade_moedas_2(tela)
        tela.blit(nivel, (20, 3))
        tela.blit(A, (83, 260))
        tela.blit(B, (465, 260))
        tela.blit(C, (70, 402))
        tela.blit(D, (460, 400))
        tela.blit(pergunta, (400 - pergunta.get_width() // 2, 100))
        pygame.display.update()
        
def fase_12(tela):
    fonte_pergunta = pygame.font.Font('Chendolle.otf',45)
    pergunta =  fonte_pergunta.render('Qual desses nao fundou o insper?', True, preto)
    fonte_alternativa = pygame.font.Font('Chendolle.otf',40)
    A = fonte_alternativa.render('Claudio Haddad', True, preto)
    B = fonte_alternativa.render('Jorge Paulo Lemann', True, preto)
    C = fonte_alternativa.render('Carlos Sicupira', True, preto)
    D = fonte_alternativa.render('Marcelo Zanutim', True, preto)
    fonte_nivel = pygame.font.Font('Chendolle.otf',75)
    nivel = fonte_nivel.render('12.', True, preto)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if  alternativa_D.collidepoint(mouse_pos):
                    som_acertou.play()
                    fase_13(tela)
                    break
                if alternativa_A.collidepoint(mouse_pos) or alternativa_B.collidepoint(mouse_pos) or alternativa_C.collidepoint(mouse_pos):
                    som_errou.play()
                    funcoes.derrota_2(tela)

        tela.fill(branco)
        funcoes.desenha_interface_fases(tela)
        funcoes.desenha_quantidade_moedas_2(tela)
        tela.blit(nivel, (20, 2))
        tela.blit(A, (99, 270))
        tela.blit(B, (442, 268))
        tela.blit(C, (97, 407))
        tela.blit(D, (465, 405))
        tela.blit(pergunta, (400 - pergunta.get_width() // 2, 100))
        pygame.display.update()
        
def fase_13(tela):
    fonte_pergunta = pygame.font.Font('Chendolle.otf',45)
    pergunta =  fonte_pergunta.render('SISTEMA OPERACIONAL DO PC DA SALA 312?', True, preto)
    fonte_alternativa = pygame.font.Font('Chendolle.otf',70)
    A = fonte_alternativa.render('LINUX', True, preto)
    B = fonte_alternativa.render('MACOS', True, preto)
    C = fonte_alternativa.render('WINDOWS', True, preto)
    D = fonte_alternativa.render('NAO TEM', True, preto)
    fonte_nivel = pygame.font.Font('Chendolle.otf',70)
    nivel = fonte_nivel.render('13.', True, preto)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                    
                if  alternativa_A.collidepoint(mouse_pos):
                    som_acertou.play()
                    fase_14(tela)
                    
                    break
                if alternativa_C.collidepoint(mouse_pos) or alternativa_B.collidepoint(mouse_pos) or alternativa_D.collidepoint(mouse_pos):
                    som_errou.play()
                    funcoes.derrota_2(tela)

        tela.fill(branco)
        funcoes.desenha_interface_fases(tela)
        funcoes.desenha_quantidade_moedas_2(tela)
        tela.blit(nivel, (21, 4))
        tela.blit(A, (130, 255))
        tela.blit(B, (495, 255))
        tela.blit(C, (92, 400))
        tela.blit(D, (470, 395))
        tela.blit(pergunta, (400 - pergunta.get_width() // 2, 100))
        pygame.display.update()
        
def fase_14(tela):
    fonte_pergunta = pygame.font.Font('Chendolle.otf',45)
    pergunta =  fonte_pergunta.render('QUANTAS MESAS TEM NA SALA DE 312?', True, preto)
    fonte_alternativa = pygame.font.Font('Chendolle.otf',70)
    A = fonte_alternativa.render('25', True, preto)
    B = fonte_alternativa.render('26', True, preto)
    C = fonte_alternativa.render('27', True, preto)
    D = fonte_alternativa.render('28', True, preto)
    fonte_nivel = pygame.font.Font('Chendolle.otf',70)
    nivel = fonte_nivel.render('14.', True, preto)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if  alternativa_D.collidepoint(mouse_pos):
                    som_acertou.play()
                    fase_15(tela)
                    break
                if alternativa_A.collidepoint(mouse_pos) or alternativa_B.collidepoint(mouse_pos) or alternativa_C.collidepoint(mouse_pos):
                    som_errou.play()
                    funcoes.derrota_2(tela)



        tela.fill(branco)
        funcoes.desenha_interface_fases(tela)
        funcoes.desenha_quantidade_moedas_2(tela)
        tela.blit(nivel, (25, 5))
        tela.blit(A, (175, 255))
        tela.blit(B, (550, 255))
        tela.blit(C, (175, 395))
        tela.blit(D, (550, 394))
        tela.blit(pergunta, (400 - pergunta.get_width() // 2, 100))
        pygame.display.update()

def fase_15(tela):
    fonte_pergunta = pygame.font.Font('Chendolle.otf',40)
    pergunta =  fonte_pergunta.render('Por fim, qual a ultima palavra da 3* pergunta?', True, preto)
    fonte_alternativa = pygame.font.Font('Chendolle.otf',70)
    A = fonte_alternativa.render('Em', True, preto)
    B = fonte_alternativa.render('Miranda', True, preto)
    C = fonte_alternativa.render('Estudou', True, preto)
    D = fonte_alternativa.render('Insper', True, preto)
    fonte_nivel = pygame.font.Font('Chendolle.otf',75)
    nivel = fonte_nivel.render('15.', True, preto)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if  alternativa_C.collidepoint(mouse_pos):
                    som_acertou.play()
                    desenha_tela_vitoria(tela)
                    break
                if alternativa_D.collidepoint(mouse_pos) or alternativa_B.collidepoint(mouse_pos) or alternativa_A.collidepoint(mouse_pos):
                    som_errou.play()
                    funcoes.derrota_2(tela)



        tela.fill(branco)
        funcoes.desenha_interface_fases(tela)
        funcoes.desenha_quantidade_moedas_2(tela)
        tela.blit(nivel, (20, 3))
        tela.blit(A, (170, 254))
        tela.blit(B, (505, 250))
        tela.blit(C, (103, 395))
        tela.blit(D, (505, 390))
        tela.blit(pergunta, (400 - pergunta.get_width() // 2, 100))
        pygame.display.update()
        
def desenha_tela_vitoria(tela):
    branco = (255, 255, 255)
    preto = (0, 0, 0)
    laranja = (230, 115, 0)
    laranja_escuro = (200, 100, 0)
    laranja_claro = (255, 140, 0)
    fonte_titulo = pygame.font.Font('Chendolle.otf', 90)
    fonte_texto = pygame.font.Font('Chendolle.otf', 100)
    fonte_quantidade = pygame.font.Font('Chendolle.otf', 150)
    seta = pygame.image.load('seta-esquerda.png')
    seta = pygame.transform.scale(seta, (50, 50))
    coin = pygame.image.load('MCoin.png')
    coin = pygame.transform.scale(coin, (200, 200))
    voltar = pygame.Rect(20, 530, 150, 60)
    while True:
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            if voltar.collidepoint(mouse_pos):
                voltar = pygame.Rect(10, 520, 170, 80)
            else:
                voltar = pygame.Rect(20, 530, 150, 60)

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if voltar.collidepoint(mouse_pos):
                    Main_Menu.jogo()
        tela.fill(branco)
        titulo = fonte_titulo.render('Voce Ganhou!!!!', True, preto)
        premio = fonte_texto.render('Tome seu premio:', True, preto)
        quantidade = fonte_quantidade.render('3x', True, preto)
        tela.blit(titulo, (170, 20))
        tela.blit(premio, (100, 150))
        tela.blit(quantidade, (300, 280))
        tela.blit(coin, (395, 270))
        # interface Retangulo
        pygame.draw.rect(tela, laranja, voltar)
        pygame.draw.rect(tela, laranja_escuro, voltar, 5)
        pygame.draw.rect(tela, laranja_claro, voltar.inflate(-10, -10))
        tela.blit(seta, (65, 535))

        
        # Atualiza a tela
        pygame.display.update()