def print_board(board):
    """Imprime o tabuleiro do jogo da velha sem a última linha de separação."""
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:  # Adiciona uma linha de separação apenas entre as linhas, não após a última linha
            print("-" * 9)



def is_winner(board, player):
    """Verifica se o jogador venceu."""
    # Verifica linhas, colunas e diagonais
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Verifica linhas
            return True
        if all([board[j][i] == player for j in range(3)]):  # Verifica colunas
            return True
    # Verifica diagonais
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False


def get_empty_cells(board):
    """Retorna uma lista de células vazias no tabuleiro."""
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return empty_cells


def greedy_move(board, player):
    """Algoritmo de busca gulosa para escolher a melhor jogada no momento."""
    opponent = 'O' if player == 'X' else 'X'

    # 1. Verifica se o jogador pode vencer no próximo movimento
    for (i, j) in get_empty_cells(board):
        board[i][j] = player
        if is_winner(board, player):
            return (i, j)  # Joga para vencer
        board[i][j] = ' '  # Desfaz o movimento

    # 2. Bloqueia o oponente se ele puder vencer no próximo movimento
    for (i, j) in get_empty_cells(board):
        board[i][j] = opponent
        if is_winner(board, opponent):
            return (i, j)  # Bloqueia o oponente
        board[i][j] = ' '  # Desfaz o movimento

    # 3. Ocupar o centro
    if board[1][1] == ' ':
        return (1, 1)

    # 4. Ocupar um dos cantos
    for (i, j) in [(0, 0), (0, 2), (2, 0), (2, 2)]:
        if board[i][j] == ' ':
            return (i, j)

    # 5. Escolher qualquer posição vazia
    empty_cells = get_empty_cells(board)
    if empty_cells:
        return empty_cells[0]

    return None  # Não há movimentos disponíveis


def player_move(board):
    """Função para o jogador (usuário) fazer uma jogada."""
    while True:
        try:
            row = int(input("Escolha a linha (0, 1, 2): "))
            col = int(input("Escolha a coluna (0, 1, 2): "))
            if (row, col) in get_empty_cells(board):
                return (row, col)
            else:
                print("Essa posição já está ocupada ou é inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite números de 0 a 2.")


def is_draw(board):
    """Verifica se o jogo terminou em empate."""
    return len(get_empty_cells(board)) == 0


def play_game():
    """Função principal para jogar o jogo da velha."""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'  # O jogador 'X' começa

    print("Bem-vindo ao Jogo da Velha!")
    print("Você é 'X' e o computador é 'O'.")
    print_board(board)

    while True:
        if current_player == 'X':
            print("\nSua vez!")
            move = player_move(board)
        else:
            print("\nTurno do computador...")
            move = greedy_move(board, current_player)

        # Faz a jogada
        board[move[0]][move[1]] = current_player
        print_board(board)

        # Verifica vitória ou empate
        if is_winner(board, current_player):
            print(f"\nJogador {current_player} venceu!")
            break
        elif is_draw(board):
            print("\nO jogo terminou em empate!")
            break

        # Troca de jogador
        current_player = 'O' if current_player == 'X' else 'X'


def main():
    """Função principal para gerenciar o loop do jogo."""
    while True:
        play_game()
        # Pergunta ao usuário se deseja jogar novamente
        play_again = input("Deseja jogar novamente? (s/n): ").strip().lower()
        if play_again != 's':
            print("Obrigado por jogar! Até a próxima!")
            break


# Executa o jogo
if __name__ == "__main__":
    main()
