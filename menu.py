import sys
import pygame

# Inicializa o Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Menu")

# CORES
WHITE = (255, 255, 255)
GRAY = (120, 120, 120)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# FONTES
font = pygame.font.Font(None, 50)

# MENU DE OPÇÕES
menu_options = ["Iniciar Simulação", "Sair"]
selected_option = 0

# Botões de controle de tick rate
button_images = {
    "increase": pygame.image.load("fastforward.jpg"),
}
button_rects = {
    "increase": pygame.Rect(WIDTH // 4, HEIGHT // 4, 10, 5),  # Posição do botão "avançar"
}

# Tick rate inicial
tick_rate = 60

def draw_menu():
    """Renderiza o menu na tela."""
    screen.fill(BLACK)  # Limpa a tela

    # Desenha os botões de controle de tick rate
    screen.blit(button_images["increase"], button_rects["increase"].center)

    # Desenha o menu de opções
    for index, option in enumerate(menu_options):
        text_surface = font.render(option, True, WHITE)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + index * 50))
        
        # Verifica se o mouse está sobre o botão
        if text_rect.collidepoint(pygame.mouse.get_pos()):
            text_color = GRAY  # Muda a cor do texto para cinza
            circle_color = GRAY  # Muda a cor do círculo para cinza
            # Desenha um círculo à esquerda do texto
            circle_radius = 10
            circle_x = text_rect.left - 30  # Posição do círculo à esquerda do texto
            circle_y = text_rect.centery  # Centraliza verticalmente com o texto
            pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)
        else:
            text_color = WHITE
        
        # Renderiza o texto com a cor apropriada
        text_surface = font.render(option, True, text_color)
        screen.blit(text_surface, text_rect)  # Adiciona a opção na tela
        screen.blit(button_images["increase"], button_rects["increase"].topleft)
    pygame.display.flip()  # Atualiza a tela

def main_menu():
    """Loop do menu principal."""
    global selected_option, tick_rate
    running = True

    while running:
        draw_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # Verifica se o clique foi em um dos botões de controle de tick rate
                if button_rects["increase"].collidepoint(x, y):
                    tick_rate += 10  # Aumenta o tick rate em 10
                    print(f"Tick rate aumentado para: {tick_rate}")
                
                # Verifica se o clique foi em uma das opções do menu
                for index, option in enumerate(menu_options):
                    text_surface = font.render(option, True, WHITE)
                    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + index * 50))
                    if text_rect.collidepoint(x, y):
                        if index == 0:
                            print("Starting Game...")  # Aqui pode chamar a função do jogo
                            running = False  # Sai do menu
                        elif index == 1:
                            pygame.quit()
                            sys.exit()
           
            # Detecta teclas do teclado
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:
                        print("Starting Game...")  # Aqui pode chamar a função do jogo
                        running = False  # Sai do menu
                    elif selected_option == 1:
                        pygame.quit()
                        sys.exit()

    return tick_rate  # Retorna o tick rate

main_menu()