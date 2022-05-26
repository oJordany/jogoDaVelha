from time import sleep
model = [
    ['    ', '    ', '    '],
    ['    ', '    ', '    '],
    ['    ', '    ', '    '],
]


def printTable(row=None, column=None, symbol=None, model=model):
    print("+----+----+----+", end='')
    print()

    if row != None and column != None:
        model[row][column] = f"{symbol:^4}"

    for index, row in enumerate(model):
        if index <= 2:
            print(f"|{row[0]}|{row[1]}|{row[2]}|")
            print(f"+----+----+----+")


def machineChoice(symbol, model=model):
    from random import randint
    while True:
        row = randint(0, 2)
        column = randint(0, 2)
        if model[row][column] == '    ':
            printTable(row, column, symbol)
            break


def playerChoice(row, column, symbol, model=model):
    if model[row][column] == '    ':
        printTable(row, column, symbol)
        return True
    else:
        print('\033[1;31mErro: posicao ja preenchida\033[m')
        return False


def checkWin(machineSymbol, playerSymbol, model=model):
    checker = False
    for i in range(0, len(model)):
        if model[i][0] == model[i][1] == model[i][2] and model[i][0] != '    ' and model[i][1] != '    ' and model[i][2] != '    ':
            if model[i][0].strip() == machineSymbol:
                print('\033[1;31mQue Pena, vc perdeu :(\033[m')
            else:
                print('\033[1;32mParabens, vc me venceu! :)\033[m')
            return False
        elif model[0][i] == model[1][i] == model[2][i] and model[0][i] != '    ' and model[1][i] != '    ' and model[2][i] != '    ':
            if model[0][i].strip() == machineSymbol:
                print('\033[1;31mQue Pena, vc perdeu :(\033[m')
            else:
                print('\033[1;32mParabens, vc me venceu! :)\033[m')
            return False

    if model[0][0] == model[1][1] == model[2][2] and model[0][0] != '    ' and model[1][1] != '    ' and model[2][2] != '    ' or model[0][2] == model[1][1] == model[2][0] and model[0][2] != '    ' and model[1][1] != '    ' and model[2][0] != '    ':
        if model[1][1].strip() == machineSymbol:
            print('\033[1;31mQue Pena, vc perdeu :(\033[m')
        else:
            print('\033[1;32mParabens, vc me venceu! :)\033[m')

        return False

    for row in model:
        if row[0] == '    ' or row[1] == '    ' or row[2] == '    ':
            checker = True
    if checker == False:
        print('\033[1;33mO jogo Empatou :|\033[m')
    
    return checker


# Programa principal
print(f"{' JOGO DA VELHA ':#^41}")
playerSymbol = input(
    'Escolha o seu simbolo [C -> 〇 / X -> ⨉]: ').upper().strip()[0]
machineSymbol = '⨉' if playerSymbol == 'C' else '○'
playerSymbol = '○' if playerSymbol == 'C' else '⨉'

varTeste = checkWin(machineSymbol, playerSymbol)
checker = True
while True:
    print('> Minha Vez ...')
    sleep(2)
    machineChoice(machineSymbol)
    if not checkWin(machineSymbol, playerSymbol):
        break
    print('> Sua Vez ...')
    sleep(2)
    checkPosition = False
    while True:
        if not checkPosition:
            playerRow = int(input('Insira a linha da posicao q vc deseja jogar: ')) - 1
            playerColumn = int(input('Insira a coluna da posicao que vc deseja jogar: ')) - 1
            checkPosition = playerChoice(playerRow, playerColumn, playerSymbol)
        else:
            break
    if not checkWin(machineSymbol, playerSymbol):
        break