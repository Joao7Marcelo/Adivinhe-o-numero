from distutils.command.clean import clean
import os
from pickletools import read_int4
import random
import time
from turtle import color
import turtle

def titulo():
    print('###########################')
    print('#                         #')
    print('#  Olá, Vamos jogar?      #')
    print('#                         #')
    print('###########################')
    
    input('\n\nDigite Enter para iniciar o gamer!!!...')
    os.system('cls')
    print('Um momento...')
    time.sleep(2)
    os.system('cls')
    print('m momento...')
    time.sleep(0.1)
    os.system('cls')
    print(' momento...')
    time.sleep(0.1)
    os.system('cls')
    print('momento...')
    time.sleep(0.1)
    os.system('cls')
    print('omento...')
    time.sleep(0.1)
    os.system('cls')
    print('mento...')
    time.sleep(0.1)
    os.system('cls')
    print('ento...')
    time.sleep(0.1)
    os.system('cls')
    print('nto...')
    time.sleep(0.1)
    os.system('cls')
    print('to...')
    time.sleep(0.1)
    os.system('cls')
    print('o...')
    time.sleep(0.1)
    os.system('cls')
    print('...')
    time.sleep(0.1)
    os.system('cls')
    print('..')
    time.sleep(0.1)
    os.system('cls')
    print('.')
    time.sleep(0.1)
    os.system('cls')
    print('Pensei em um numero entre 1 e 100')
    
def gerador_de_numero():
    numero_gerado = random.randrange(1, 101)
    return numero_gerado

def jogo(numero, erros):
    while True:
        try:
            resposta = int(input('\nEm qual número pensei: '))
            if resposta > 100 or resposta < 1:
                print('O valor tem digitado tem que ser maior que 1 e menor que 100')
                time.sleep(1)
            elif resposta > numero:
                print(f'!!! O número que pensei é menor que: {resposta} !!!')
                erros += 1
            elif resposta < numero:
                
                print(f'!!!  O número que pensei é maior que: {resposta} !!!')
                erros += 1
            elif resposta == numero:
                print('\n\n#######################################')
                print('#                                     #')
                print(f'# Parabéns... O número correto é: {resposta}  #')
                print(f'# Seu número de erros foi: {erros}')
                print('#                                     #')
                print('#######################################')
                
                fim = input('\nDeseja reinicar o jogo S ou N?: ')
                if fim == 's':
                    os.system('cls')
                    time.sleep(2)
                    print('Pensei em outro número entre 1 e 100...')
                    titulo()
                    continue
                else:
                    os.system('cls')
                    time.sleep(1)
                    print('Obrigado por jogar nosso jogo!!!')
                    time.sleep(3)
                    os.system('cls')
                    print('por jogar nosso jogo!!!')
                    time.sleep(0.3)
                    os.system('cls')
                    print('jogar nosso jogo!!!')
                    time.sleep(0.3)
                    os.system('cls')
                    print('nosso jogo!!!')
                    time.sleep(0.3)
                    os.system('cls')
                    print('jogo!!!')
                    time.sleep(0.3)
                    os.system('cls')
                    break
                                    
        except ValueError:
            print('Digite apenas números inteiros!!!')
            time.sleep(1)
                
titulo()

numero = gerador_de_numero()
erros = 0
jogo(numero, erros, gerador_de_numero)