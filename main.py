# Made by: Felipe Cradoso;
# GitHub: the-felipe;

import os
import time
from random import randint

emojis = {1:"1️⃣", 2:"2️⃣", 3:"3️⃣", 4:"4️⃣", 5:"5️⃣", 6:"6️⃣", 7:"7️⃣", 8:"8️⃣", 9:"9️⃣", 10:"🔟"}

def main():
    os.system("clear")
    menu()
    verComandos()
    
    listaComandos = ["i", "s", "p", "e", "c"]   
    tentativas = 1
    testeJogador = 0
    numJogador = 0
    listaPlacar = []
    testando = 1

    while testando == 1:
        print("")
        comando = input("📄 | COMANDO >> ").lower()
        os.system("clear")
        
        if comando == "i":
            testeJogador += 1
            tentativas = jogoRodando()

        elif comando == "e":
            print("🤖 | OBRIGADO POR JOGAR!\n")
            time.sleep(1.5)
            os.system("clear")
            testando = 0

        elif comando == "s":
            if testeJogador == 0:
                print("💤 | VOCÊ DEVE JOGAR 1 VEZ PARA CONSEGUIR SALVAR SUA PONTUAÇÃO.")
            else:
                listaPlacar.append(tentativas)
                numJogador += 1
                print(f"📝 | SUA PONTUAÇÃO FOI SALVA NO PLACAR >> (JOGADOR {numJogador})")

        elif comando == "p":
            if listaPlacar == []:
                print(f"❕ | VOCÊ NÃO SALVOU NENHUMA PONTUAÇÃO")

            else:
                print("🥇 | PLACAR DE PONTOS\n")
                for i in range(len(listaPlacar)):
                    print(f"JOGADOR {i+1} >> {emojis[listaPlacar[i]]}  TENTATIVA(S)")

        elif comando == "c":
            comandos()

        elif comando not in listaComandos:
            print("❌ | COMANDO NÃO ENCONTRADO!")
            print('💡 | DIGITE "C" PARA VER OS COMANDOS DISPONÍVEIS.')
    
def jogoRodando():

    run = 1
    tentativas = 1
    num = randint(1, 10)

    while run == 1:
        chute = int(input("🏁 | TENTE UM NÚMERO >> "))
        if chute == num:
            if tentativas == 1:
                print("👑 | UAU! ACERTOU DE 1ª")
            else:
                print("🟢 | PARABÉNS!")
                print(f"{emojis[tentativas]}  | TENTATIVAS NESCESSÁRIAS.")
                print("🔵 | PARA SALVAR SUA PONTUAÇÃO DIGITE 'S'!")
            run = 0

        elif chute != num:
            tentativas += 1
            if chute > 10:
                print("💡 | LEMBRE-SE QUE O NÚMERO MÁXIMO É 10!")
            if chute > num:
                print("🔴 | TENTE UM NÚMERO MENOR.\n")
                
            if chute < 1:
                print("💡 | LEMBRE-SE QUE O NÚMERO MÍNIMO É 1!")  
            if chute < num:
                print("🔴 | TENTE UM NÚMERO MAIOR.\n")   

    return tentativas

def comandos():
    print("""📚 | LISTA DE COMANDOS DISPONÍVEIS:
                  
'I' >> INICIAR
'S' >> SALVAR PONTUAÇÃO
'P' >> MOSTRAR PLACAR
'E' >> ENCERRAR
""")
    
def verComandos():
    op = input("❓ | Deseja ver os comandos? (S/N) >> ").lower()
    if op == "s":
        os.system("clear")
        comandos()

def menu():
    print("🎮 | JOGO EM PYTHON\n__________________\n")

main()