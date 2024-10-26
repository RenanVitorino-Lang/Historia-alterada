import random

# Função que gera a introdução da historia
def gerar_introduçao():
    introduçao = ["Era uma vez", "Há muito tempo atrás", "Num reino distante"]
    return random.choice(introduçao)

# Função que gera o desenvolvimento():
def gerar_desenvolvimento():
    desenvolvimento = ["Um ferroz Bárbaro", "um poderoso Bruxo", "Um sabio Monge", "Um grande guerreiro"]
    return random.choice(desenvolvimento)

# Função que gera o final da historia
def gerar_final():
    finais = ["estava em uma guerra sanguinaria contar Vampiros.", "procurando um tesouro escondido na floresta de druidas.", "caçando um Basilisco.", "salvando uma pequena vila de uma grande descontrolada hidra.", "salvando o povo largato de minotauros loucos por guerra.", "lutando contra um kraken em busca de salvar o povo do mar.", "Salvando goblins da escravidão.", "Tentando domesticar Hipogrifos.", "No lixão lutando contra um monstro da ferrugem."]
    return random.choice(finais)

# Função principal que gera toda a história
def gerar_historia():
    introducao = gerar_introduçao()
    desenvolvimento = gerar_desenvolvimento()
    final = gerar_final()

    historia = f"{introducao},{desenvolvimento}, {final}"
    return historia

# Exibe a história gerada 
if __name__ == "__main__":
    print(gerar_historia())