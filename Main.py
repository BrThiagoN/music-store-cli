import os
import array

import data

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('==========MENU==========')
    print('Bem-vindo a loja de instrumentos musicais!')
    print('1. Cadastrar instrumento')
    print('2. Listar instrumentos')
    print('3. Sair')
    print('========================')
    value = int(input('Digite a opção desejada: '))

    if value == 1:
        cadastrarInstrumento()
    if value == 2:
        listarInstrumentos()
    if value == 3:
        sair()
    else:
        respostaInvalida()

def cadastrarInstrumento() -> array:
     name = input('qual o nome do instrumento?')
     price = float(input('qual o preço do instrumento?'))
     instrument = {'name': name, 'price': price}

     data.instruments.append(instrument)
     print('instrumento adicionado com sucesso!')
     retornarMenu()
     return data.instruments

def listarInstrumentos() -> None:
    print(data.instruments)
    retornarMenu()

def sair() -> None:
    print('Obrigado por usar nosso sistema!')
    exit()

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