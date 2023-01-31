import pygame
from config import FPS, WIDTH, HEIGHT, BLACK
from assets import carrega_arquivos
from sprites import Input
def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    dicionario_de_arquivos = carrega_arquivos()
    lista_imagem = pygame.sprite.Group()
    input = Input(dicionario_de_arquivos)
    lista_imagem.add(input)
    MEMORIZE = True
    DONE = 0
    PLAYING = 1
    state = PLAYING
    last_update = pygame.time.get_ticks()
    ultima_vez = pygame.time.get_ticks()
    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)
        segundos = int((pygame.time.get_ticks() - last_update)/1000)
        cont = 40 - segundos


        # ----- Trata eventos
        for event in pygame.event.get(): 
            if event.type == pygame.KEYUP:
                print(event.unicode)   
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
        if cont <0:
            state = DONE
        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor branca
        lista_imagem.draw(window)
        num = dicionario_de_arquivos['font2'].render(input.palavra, True, (0, 0, 0))
        timer = dicionario_de_arquivos['font'].render(str(cont), True, (255, 255, 255))
        texto = dicionario_de_arquivos['font_media'].render(input.memorize, True, (255, 255, 255))
        dig = dicionario_de_arquivos['font_media'].render(input.digite, True, (255, 255, 255))
        window.blit(timer, (860, 10))
        if MEMORIZE == True:
            window.blit(num, (410, 260))
            window.blit(texto, (280, 180))
        if MEMORIZE == False:
            window.blit(dig, (280, 180))
        agora = pygame.time.get_ticks()
        if MEMORIZE == True and agora - ultima_vez > 3000:
            MEMORIZE = False
            ultima_vez = agora
        if MEMORIZE == False and agora - ultima_vez > 5000:
            MEMORIZE = True
            ultima_vez = agora
        pygame.display.update()  # Mostra o novo frame para o jogador
        
    return state
