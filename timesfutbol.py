N, t = map(int, input().split())

jogadores = []

for i in range(N):
    nome, habilidade = input().split()
    habilidade = int(habilidade)
    jogadores.append((habilidade, nome))
 
# Ordena pela habilidade (maior para menor)
jogadores.sort(reverse=True)

# Cria os times
times = []

for i in range(t):
    times.append([])

# Distribui em rodízio
for i in range(N):
    habilidade, nome = jogadores[i]
    times[i % t].append(nome)

# Ordena os nomes de cada time
for time in times:
    time.sort()

# Imprime
for i in range(t):
    print(f" Time {i+1}")

    for nome in times[i]:
        print(nome)

    print()