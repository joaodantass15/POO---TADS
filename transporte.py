from datetime import timedelta

# Classe base para todas as entidades do sistema de transporte
class EntidadeTransporte:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def __repr__(self):
        return f"{self.nome} (ID: {self.id})"

# Classe Parada, herdando de EntidadeTransporte
class Parada(EntidadeTransporte):
    def __init__(self, id, nome, localizacao):
        super().__init__(id, nome)  # Herança
        self.localizacao = localizacao

    def __repr__(self):
        return f"{self.nome} - Localização: {self.localizacao}"

# Classe LinhaDeTransporte, herdando de EntidadeTransporte
class LinhaDeTransporte(EntidadeTransporte):
    def __init__(self, id, numero, nome, tarifa):
        super().__init__(id, nome)  # Herança
        self.numero = numero
        self.tarifa = tarifa
        self.paradas = []
        self.horarios = {}

    def adicionar_parada(self, parada, horario=None):
        self.paradas.append(parada)
        if horario:
            self.horarios[parada.nome] = horario

    def buscar_parada_por_nome(self, nome):
        for parada in self.paradas:
            if parada.nome.lower() == nome.lower():
                return parada
        return None

    def buscar_parada_por_localizacao(self, localizacao):
        for parada in self.paradas:
            if parada.localizacao.lower() == localizacao.lower():
                return parada
        return None

    def __repr__(self):
        return f"Linha {self.numero} - {self.nome} (Tarifa: R${self.tarifa:.2f})"

# Classe SistemaDeTransporte com exceções e herança
class SistemaDeTransporte:
    def __init__(self, usuario_nome, tarifa_estudante):
        self.linhas = []
        self.usuario_nome = usuario_nome
        self.tarifa_estudante = tarifa_estudante

    def adicionar_linha(self, linha):
        self.linhas.append(linha)

    def buscar_linha_por_numero(self, numero):
        for linha in self.linhas:
            if linha.numero == numero:
                return linha
        return None

    def buscar_parada_por_nome(self, nome):
        for linha in self.linhas:
            parada = linha.buscar_parada_por_nome(nome)
            if parada:
                return parada
        return None

    def buscar_parada_por_localizacao(self, localizacao):
        for linha in self.linhas:
            parada = linha.buscar_parada_por_localizacao(localizacao)
            if parada:
                return parada
        return None

    def buscar_linhas_por_horario(self, horario):
        linhas_com_horario = []
        for linha in self.linhas:
            for parada, h in linha.horarios.items():
                if h == horario:
                    linhas_com_horario.append((linha.numero, parada))
        return linhas_com_horario

    def pesquisar(self):
        print(f"\nBem-vindo(a), {self.usuario_nome}!")
        while True:
            print("\nDigite 'linha' para pesquisar por número da linha, 'parada' para pesquisar por nome da parada, 'localizacao' para pesquisar por localização da parada, ou 'horario' para pesquisar por horário do ônibus.")
            tipo_pesquisa = input("Sua escolha: ").strip().lower()

            if tipo_pesquisa == 'linha':
                try:
                    numero_linha = int(input("Digite o número da linha: "))
                    linha = self.buscar_linha_por_numero(numero_linha)
                    if linha:
                        print(f"Linha encontrada: {linha}")
                        print("Paradas:")
                        for parada in linha.paradas:
                            print(f"- {parada}")
                    else:
                        print("Linha não encontrada.")
                except ValueError:
                    print("Número de linha inválido. Por favor, tente novamente.")

            elif tipo_pesquisa == 'parada':
                nome_parada = input("Digite o nome da parada: ").strip()
                parada = self.buscar_parada_por_nome(nome_parada)
                if parada:
                    print(f"Parada encontrada: {parada}")
                    linhas_passando = [linha.numero for linha in self.linhas if linha.buscar_parada_por_nome(parada.nome)]
                    print(f"Linhas que passam por essa parada: {', '.join(map(str, linhas_passando))}")
                else:
                    print("Parada não encontrada.")

            elif tipo_pesquisa == 'localizacao':
                localizacao = input("Digite a localização: ").strip()
                parada = self.buscar_parada_por_localizacao(localizacao)
                if parada:
                    print(f"Parada encontrada na localização {localizacao}: {parada}")
                    linhas_passando = [linha.numero for linha in self.linhas if linha.buscar_parada_por_localizacao(parada.localizacao)]
                    print(f"Linhas que passam por essa localização: {', '.join(map(str, linhas_passando))}")
                else:
                    print("Nenhuma parada encontrada nesta localização.")

            elif tipo_pesquisa == 'horario':
                horario = input("Digite o horário (HH:MM): ").strip()
                linhas_com_horario = self.buscar_linhas_por_horario(horario)
                if linhas_com_horario:
                    print(f"Ônibus com horário {horario}:")
                    for linha_numero, parada in linhas_com_horario:
                        print(f"Linha {linha_numero} - Parada: {parada}")
                else:
                    print("Nenhum ônibus encontrado nesse horário.")

            else:
                print("Entrada inválida. Tente novamente.")

            continuar = input("Deseja fazer outra pesquisa? (s/n): ").strip().lower()
            if continuar != 's':
                break

# Capturar informações do usuário
usuario_nome = input("Digite seu nome: ").strip()
estudante = input("Você é estudante? (s/n): ").strip().lower()

# Tarifa reduzida para estudantes
tarifa_estudante = 2.25 if estudante == 's' else 4.50

# Inicializando o sistema de transporte
sistema = SistemaDeTransporte(usuario_nome, tarifa_estudante)

# Exemplo de criação de linhas e paradas com horários
linha_26 = LinhaDeTransporte(1, 26, "Linha 26", tarifa_estudante)
parada_midway = Parada(1, "Midway", "Tirol")
parada_shopping = Parada(2, "Shopping", "Capim Macio")
parada_praia = Parada(3, "Praia", "Ponta Negra")
parada_ifrn = Parada(4, "IFRN", "Tirol")
linha_26.adicionar_parada(parada_midway, "08:00")
linha_26.adicionar_parada(parada_shopping, "09:00")
linha_26.adicionar_parada(parada_praia, "09:30")
linha_26.adicionar_parada(parada_ifrn, "13:00")

linha_54 = LinhaDeTransporte(2, 54, "Linha 54", tarifa_estudante)
parada_academia = Parada(5, "Academia", "Capim Macio")
linha_54.adicionar_parada(parada_midway, "10:00")
linha_54.adicionar_parada(parada_shopping, "07:00")
linha_54.adicionar_parada(parada_praia, "06:30")
linha_54.adicionar_parada(parada_academia, "08:00")

linha_46 = LinhaDeTransporte(3, 46, "Linha 46", tarifa_estudante)
parada_conjunto = Parada(6, "Conjunto", "Ponta Negra")
linha_46.adicionar_parada(parada_ifrn, "07:00")
linha_46.adicionar_parada(parada_shopping, "16:00")
linha_46.adicionar_parada(parada_praia, "08:30")
linha_46.adicionar_parada(parada_academia, "14:00")
linha_46.adicionar_parada(parada_conjunto, "18:00")

linha_73 = LinhaDeTransporte(4, 73, "Linha 73", tarifa_estudante)
linha_73.adicionar_parada(parada_praia, "06:30")
linha_73.adicionar_parada(parada_midway, "12:00")
linha_73.adicionar_parada(parada_conjunto, "18:00")
linha_73.adicionar_parada(parada_academia, "17:00")

# Adicionando linhas ao sistema
sistema.adicionar_linha(linha_26)
sistema.adicionar_linha(linha_54)
sistema.adicionar_linha(linha_46)
sistema.adicionar_linha(linha_73)

# Iniciar a pesquisa no sistema
sistema.pesquisar()
