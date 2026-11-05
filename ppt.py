import random

pedra = 1
papel = 2
tesoura = 3
nomes = {pedra: "Pedra", papel: "Papel", tesoura: "Tesoura"}

p_player = 0
p_pc = 0

print("Bem vindo ao Pedra, Papel e Tesoura!")

while True:
    print(f"\nPlacar:\nVocê: {p_player}\nComputador: {p_pc}")

    esc = 0
    while esc not in (pedra, papel, tesoura):
        try:
            esc = int(input("\nEscolha uma opção:\n1 - Pedra\n2 - Papel\n3 - Tesoura\nDigite o número correspondente à sua escolha: "))
        except ValueError:
            esc = 0
        if esc not in (pedra, papel, tesoura):
            print("Opção inválida. Por favor, escolha um número entre 1 e 3.")

    esc_pc = random.randint(1, 3)
    print(f"Você escolheu {nomes[esc]} e o computador escolheu {nomes[esc_pc]}.")

    if esc == esc_pc:
        print("Empate!")
    elif (esc == pedra and esc_pc == tesoura) or \
         (esc == papel and esc_pc == pedra) or \
         (esc == tesoura and esc_pc == papel):
        print("Você ganhou!")
        p_player += 1
    else:
        print("Você perdeu!")
        p_pc += 1

    print(f"\nPlacar:\nVocê: {p_player}\nComputador: {p_pc}")

    jogar_novamente = ""
    while jogar_novamente not in ("s", "n"):
        jogar_novamente = input("\nJogar novamente? (s/n): ").strip().lower()
        if jogar_novamente not in ("s", "n"):
            print("Opção inválida. Digite 's' para sim ou 'n' para não.")

    if jogar_novamente == "n":
        print("Obrigado por jogar! Até a próxima.")
        break