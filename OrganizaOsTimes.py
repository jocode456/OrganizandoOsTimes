class Aluno:
    def __init__(self, nome, habilidade):
        self.nome = nome
        self.habilidade = habilidade

    def __repr__(self):
        return f"{self.nome} ({self.habilidade})"


class Time:
    def __init__(self, numero):
        self.numero = numero
        self.jogadores = []

    def adicionar_jogador(self, aluno):
        self.jogadores.append(aluno)

    def listar_jogadores(self):
        # ordena de forma alfabetica pelo nome
        return sorted([aluno.nome for aluno in self.jogadores])


class GerenciadorTimes:
    def __init__(self, alunos, qtd_times):
        self.alunos = alunos
        self.qtd_times = qtd_times
        self.times = [Time(i + 1) for i in range(qtd_times)]

    def distribuir(self):
        # Ordena os alunos pela habilidade de forma decrescente
        self.alunos.sort(key=lambda a: a.habilidade, reverse=True)

        # for para Distribuir alternadamente entre os times
        i = 0
        for aluno in self.alunos:
            self.times[i].adicionar_jogador(aluno)
            i = (i + 1) % self.qtd_times

    def mostrar_resultado(self):
        for time in self.times:
            print(f"Time {time.numero}")
            for jogador in time.listar_jogadores():
                print(jogador)
            print()  


def main():
    N, T = map(int, input().split())
    alunos = []

    for _ in range(N):
        nome, habilidade = input().split()
        alunos.append(Aluno(nome, int(habilidade)))

    gerenciador = GerenciadorTimes(alunos, T)
    gerenciador.distribuir()
    gerenciador.mostrar_resultado()


if __name__ == "__main__":
    main()
