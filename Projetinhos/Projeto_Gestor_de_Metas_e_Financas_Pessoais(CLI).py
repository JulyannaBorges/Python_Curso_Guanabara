import emoji
import sys
print('='*62)
print(emoji.emojize(':money_bag: Bem-Vindo Ao seu Planejador de Finanças Pessoais!! :money_bag:'))
print('='*62)
with open('usuarios.txt', 'w') as arquivo:
    arquivo.write('Julyanna,senha1234')
with open('usuarios.txt', 'r') as arquivo:
    conteudo = arquivo.read().strip()
    dados = conteudo.split(',')
    dono_salvo = dados[0].strip()
    senha_salva = dados[1].strip()
print('SISTEMA DE ACESSO'.center(60))
print('='*62)
usuario_digitado = input('Usuário: ')
senha_digitada = input('Senha: ')
if usuario_digitado == dono_salvo and senha_digitada == senha_salva:
    print(f'Bem-vinda, {dono_salvo}!')
else:
    print('Acesso negado. Encerrando o sistema...')
    sys.exit()
meta_valor = 50000.00
idade_atual = int(input('Qual é a sua idade atual? '))
print(f"Sua meta atual é acumular: R$ {meta_valor:,.2f}")
saldo_atual = float(input('Quanto você já tem guardado hoje? R$ '))
aporte_mensal = float(input('Quanto você consegue guardar por mês? '))
falta = meta_valor - saldo_atual
meses_restantes = falta / aporte_mensal
anos_restantes = meses_restantes / 12
idade_final = idade_atual + anos_restantes
print('-' * 30)
print(emoji.emojize(f":rocket: Analisando seu futuro financeiro... :chart_increasing:"))
if saldo_atual >= meta_valor:
    print("INCRÍVEL! Você já atingiu sua meta financeira!")
else:
    print(f"Ainda faltam R$ {falta:,.2f} para sua meta.")
    print(f"Nesse ritmo, você levará aproximadamente {anos_restantes:.1f} anos para atingir o objetivo.")
    if idade_final <= 25:
        print(emoji.emojize(
            f":star-struck: Ótima notícia! Você terá R$ {meta_valor:,.2f} aos {idade_final:.0f} anos (antes dos 25)!"))
    else:
        print(emoji.emojize(
            f":warning: Com esse aporte, você chegaria lá aos {idade_final:.0f} anos. \nPara chegar aos 25, precisamos aumentar o aporte mensal ou buscar uma renda maior em Tech!"))