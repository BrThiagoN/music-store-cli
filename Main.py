import os
import array

import data

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('==========MENU==========')
    print('Bem-vindo a loja de instrumentos musicais!')
    print('1. Cadastrar instrumento')
    print('2. Listar instrumentos')
    print('3. Excluir item')
    print('4. Sair')
    print('========================')
    value = int(input('Digite a opção desejada: '))

    if value == 1:
        cadastrarInstrumento()
    elif value == 2:
        listarInstrumentos()
    elif value == 3:
        excluirInstrumento()
    elif value == 4:
        sair()
    else:
        respostaInvalida()

def cadastrarInstrumento() -> list[dict]:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('==========MENU==========')
    try:
        name = str(input('qual o nome do instrumento? '))
        price = float(input('qual o preço do instrumento? '))
        instrument = {'Name': name, 'Price': price}
        data.instruments.append(instrument)
        print('instrumento adicionado com sucesso!')
        retornarMenu()

    except ValueError:
        print('Valor inválido, tente novamente!')
        return cadastrarInstrumento()
    return data.instruments

def listarInstrumentos() -> None:
    exibirInstrumento()
    retornarMenu()

def sair() -> None:
    print('Obrigado por usar nosso sistema!')
    exit()

def excluirInstrumento() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    exibirInstrumento()
    delete:str = input('Qual o nome do item você deseja excluir? ')
    for instrument in data.instruments:
        if instrument['Name'].lower() == delete.lower():
            data.instruments.remove(instrument)
            print('Instrumento removido com sucesso')
        else:
            print('instrumento não encontrado')
        retornarMenu()

#FORA DO FLUXO DE MENU
def exibirInstrumento() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('==========MENU==========')
    i = 1
    for instrument in data.instruments:
        print(f'{i}. Nome: {instrument["Name"]}, Preço: R${instrument["Price"]:.2f}')
        i = i+1
    print('========================')

def retornarMenu() -> int:
    option = input('aperte enter para voltar ao menu')
    if option == '':
        menu()
        return 0
    else:
        retornarMenu()
        return 0

def respostaInvalida() -> int:
    print('Opção inválida, tente novamente!')
    return retornarMenu()

menu()