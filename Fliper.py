from pygame import mixer
from random import randint
from time import sleep

# Inicio

print("SEJA BEM-VINDO AO FLIPERAMA DONATO X3000")
nome = str(input("Digite o seu lindo nome: "))
print(f"Ola {nome}! Fico feliz que veio testar meu fliperama!")
sleep(1.0)
print("Vamos jogar!!!")
print("""
[ 1 ] JOKENPO
[ 2 ] JOGO DA ADIVINHAÇÃO
[ 3 ] Par ou Impar
""")



jogar = int(input("Digite o numero do jogo que você deseja jogar :) "))


# Tocador de musica

musica = str(input("Quer escutar uma musica enquanto joga :) [S/N] ")).strip().upper()[0]
if musica == "S":  
    mixer.init()
    mixer.music.load("TopGearSong.mp3")
    mixer.music.play() 


# JOKENPO

if jogar == 1:
    jogar_novamente = "S"
    while jogar_novamente == "S":
        itens = ("\033[1;34mPedra\033[m", "\033[1;32mPapel\033[m", "\033[1;35mTesoura\033[m")
        computador = randint(0, 2)
        print("""\033[1;33mSuas opções:\033[m                     
        [\033[1;34m0\033[m] \033[1;34mPEDRA\033[m
        [\033[1;32m1\033[m] \033[1;32mPAPEL\033[m
        [\033[1;35m2\033[m] \033[1;35mTESOURA\033[m""") # Cores em python
        print("-=" * 15)
        jogador = int(input("Faça sua jogada: "))
        print("\033[1;32mJO\033[m")
        sleep(1.0)
        print("\033[1;35mKEN\033[m")
        sleep(1.0)
        print("\033[1;34mPO\033[m")
        sleep(1.0)
        print("-=" * 15)
        print(f"Computador jogou {itens[computador]}")
        print(f"Jogador jogou {itens[jogador]}")
        if computador == 0: # Computador jogou PEDRA
            if jogador == 0:
                print("EMPATE!")
            elif jogador == 1:
                print("JOGADOR VENCE")
            elif jogador == 2:
                print("COMPUTADOR VENCE")        
            else:
                print("JOGADA INVÁLIDA")
        elif computador == 1: # Computador jogou PAPEL
            if jogador == 0:
                print("COMPUTADOR VENCE")
            elif jogador == 1:
                print("EMPATE")
            elif jogador == 2:
                print("JOGADOR VENCE")
            else:
                print("JOGADA INVÁLIDA")
        elif computador == 2: # Computador jogou TESOURA
            if jogador == 0:
                print("JOGADOR VENCE")
            elif jogador == 1:
                print("COMPUTADOR VENCE")            
            elif jogador == 2:
                print("EMPATE!")    
            else:
                print("JOGADA INVÁLIDA")
        jogar_novamente = str(input("Deseja jogar este jogo novamente? Tecle: S para Sim - N para Não: "))        

    

# Jogo da adivinhação

if jogar == 2:
    jogar_novamente = "S"
    while jogar_novamente == "S":
        computador = randint(0, 10)
        print("Ola, sou seu computador... Acabei de pensar em um numero de 0 a 10")
        print("Sera que você consegue adivinhar qual foi?")
        acertou = False
        palpites = 0
        while not acertou:
            jogador = int(input("Qual seu palpite: "))
            palpites += 1
            if jogador == computador:
                acertou = True
            else:
                if jogador < computador:
                    print("Mais...")
                elif jogador > computador:
                    print("Menos...")
        print(f"\033[1;34mAcertou com {palpites} tentativas\033[m")
        jogar_novamente = str(input("Deseja jogar este jogo novamente? Tecle: S para Sim - N para Não: ")) 
        
        
# Par ou Impar

v = 0
if jogar == 3:
    jogar_novamente = "S"
    while jogar_novamente == "S":
        while True:
            computador = randint(0, 10)
            jogador = int(input("Digite um numero: "))
            total = computador + jogador
            opcao = " "
            while opcao not in "PpIi":
                opcao = str(input("Par ou Impar? [P/I]")).strip().upper()[0]
                print(f"Voce jogou {jogador} e o computador {computador}. Total de {total}")
                print(f"DEU PAR" if total % 2 == 0 else "DEU IMPAR")
            if opcao == "P":
                if total % 2 == 0:
                    print("Voce venceu")
                    v += 1
                else:
                    print("Voce perdeu")
                    break
            elif opcao == "I":
                if total % 2 == 1:
                    print("Voce venceu")
                    v += 1
                else:
                    print("Voce perdeu")
                    break
            print("Vamos jogar novamente")
        print(f"Gamer Over! Voce venceu {v} vezes")
        jogar_novamente = str(input("Deseja jogar este jogo novamente? Tecle: S para Sim - N para Não: ")) 
        
