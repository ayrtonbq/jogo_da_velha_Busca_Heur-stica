def imprimir_tabuleiro(tabuleiro):
    """Imprime o tabuleiro do jogo da velha."""
    for i, linha in enumerate(tabuleiro):
        print(" | ".join(linha))
        if i < 2:  
            print("-" * 9)


def verificar_vencedor(tabuleiro, jogador):
    """Verifica se o jogador venceu."""
    # Verifica linhas, colunas e diagonais
    for i in range(3):
        if all([celula == jogador for celula in tabuleiro[i]]):  # Verifica linhas
            return True
        if all([tabuleiro[j][i] == jogador for j in range(3)]):  # Verifica colunas
            return True
    # Verifica diagonais
    if all([tabuleiro[i][i] == jogador for i in range(3)]) or all([tabuleiro[i][2 - i] == jogador for i in range(3)]):
        return True
    return False


def obter_celulas_vazias(tabuleiro):
    """Retorna uma lista de células vazias no tabuleiro."""
    celulas_vazias = [(i, j) for i in range(3) for j in range(3) if tabuleiro[i][j] == ' ']
    return celulas_vazias


def jogada_gulosa(tabuleiro, jogador):
    """Algoritmo de busca gulosa para escolher a melhor jogada no momento."""
    oponente = 'O' if jogador == 'X' else 'X'

    # 1. Verifica se o jogador pode vencer no próximo movimento
    for (i, j) in obter_celulas_vazias(tabuleiro):
        tabuleiro[i][j] = jogador
        if verificar_vencedor(tabuleiro, jogador):
            return (i, j)  # Joga para vencer
        tabuleiro[i][j] = ' '  # Desfaz o movimento

    # 2. Bloqueia o oponente se ele puder vencer no próximo movimento
    for (i, j) in obter_celulas_vazias(tabuleiro):
        tabuleiro[i][j] = oponente
        if verificar_vencedor(tabuleiro, oponente):
            return (i, j)  # Bloqueia o oponente
        tabuleiro[i][j] = ' '  # Desfaz o movimento

    # 3. Ocupar o centro
    if tabuleiro[1][1] == ' ':
        return (1, 1)

    # 4. Ocupar um dos cantos
    for (i, j) in [(0, 0), (0, 2), (2, 0), (2, 2)]:
        if tabuleiro[i][j] == ' ':
            return (i, j)

    # 5. Escolher qualquer posição vazia
    celulas_vazias = obter_celulas_vazias(tabuleiro)
    if celulas_vazias:
        return celulas_vazias[0]

    return None  # Não há movimentos disponíveis


def jogada_jogador(tabuleiro):
    """Função para o jogador (usuário) fazer uma jogada."""
    while True:
        try:
            linha = int(input("Escolha a linha (0, 1, 2): "))
            coluna = int(input("Escolha a coluna (0, 1, 2): "))
            if (linha, coluna) in obter_celulas_vazias(tabuleiro):
                return (linha, coluna)
            else:
                print("Essa posição já está ocupada ou é inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite números de 0 a 2.")


def verificar_empate(tabuleiro):
    """Verifica se o jogo terminou em empate."""
    return len(obter_celulas_vazias(tabuleiro)) == 0


def jogar():
    """Função principal para jogar o jogo da velha."""
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    jogador_atual = 'X'  # O jogador 'X' começa

    print("Bem-vindo ao Jogo da Velha!")
    print("Você é 'X' e o computador é 'O'.")
    imprimir_tabuleiro(tabuleiro)

    while True:
        if jogador_atual == 'X':
            print("\nSua vez!")
            jogada = jogada_jogador(tabuleiro)
        else:
            print("\nTurno do computador...")
            jogada = jogada_gulosa(tabuleiro, jogador_atual)

        # Faz a jogada
        tabuleiro[jogada[0]][jogada[1]] = jogador_atual
        imprimir_tabuleiro(tabuleiro)

        # Verifica vitória ou empate
        if verificar_vencedor(tabuleiro, jogador_atual):
            print(f"\nJogador {jogador_atual} venceu!")
            break
        elif verificar_empate(tabuleiro):
            print("\nO jogo terminou em empate!")
            break

        # Troca de jogador
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'


def main():
    """Função principal para gerenciar o loop do jogo."""
    while True:
        jogar()
        # Pergunta ao usuário se deseja jogar novamente
        jogar_novamente = input("Deseja jogar novamente? (s/n): ").strip().lower()
        if jogar_novamente != 's':
            print("Obrigado por jogar! Até a próxima!")
            break


# Executa o jogo
if __name__ == "__main__":
    main()
