#Menu de Opções: Mostrar um menu: 1. Registrar Estudo, 2. Ver Total Acumulado, 3. Sair.
#Repetição (while): O programa não pode fechar sozinho! Ele só fecha se você escolher a opção 3.
#Soma Acumulada: Toda vez que você registrar horas de Python, ele deve somar com o que já existia antes.
#Emoji de Progresso: Use emojis para indicar o status (ex: 📚 para estudo, ✅ para salvo).
import emoji
print('='*62)
print(emoji.emojize(':books: Bem-Vindo Ao Tracker de Carreira! :books:'.center(65)))
print('='*62)
with open('usuarios.txt', 'w') as arquivo:
    arquivo.write('Julyanna,julyanna1234')
with open('usuarios.txt', 'r') as arquivo:
    conteudo = arquivo.read().strip()
    dados = conteudo.split(',')
    dono_salvo = dados[0].strip()
    senha_salva = dados[1].strip()
print('Sistema de Acesso'.center(60))
print('='*62)
usuario_digitado = input('Usuário: ')
senha_digitada = input('Senha: ')
if usuario_digitado == dono_salvo and senha_digitada == senha_salva:
    print(f'Bem-vinda, {dono_salvo}! O que deseja fazer hoje?')
else:
    print('Acesso negado.')
total_horas = 0
while True:
    print('=' * 62)
    print(emoji.emojize(':books:  MENU DE PROGRESSO  :books:').center(62))
    print('=' * 62)
    print('1 - Registrar Horas de Estudo')
    print('2 - Ver Total Acumulado')
    print('3 - Sair do Sistema')
    print('=' * 62)
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        horas = float(input('Quantas horas você estudou hoje? '))
        total_horas += horas
        print(emoji.emojize(':check_mark_button: Horas registradas!'))
    elif opcao == '2':
        print(f'\nVocê já acumulou {total_horas} horas!')
        if total_horas < 10:
            print('Continue firme! 💪')
        else:
            print('Uau! Você está evoluindo! 🚀')
    elif opcao == '3':
        print('Encerrando o Tracker... Até logo!')
        break  # Comando sem aspas para fechar o programa de verdade

    else:
        print('Opção inválida! Tente 1, 2 ou 3.')