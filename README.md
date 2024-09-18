# POO---TADS
Respositório para o trabalho de POO - python
Sistema de Transporte Público - ViaBus
Descrição
O Sistema de Transporte Público - ViaBus é uma aplicação de transporte implementada em Python, que permite aos usuários pesquisarem por linhas de ônibus, paradas, localizações, horários e consultar tarifas. Ele utiliza conceitos de Programação Orientada a Objetos, como herança e exceções, para garantir uma estrutura organizada e robusta.

O sistema é voltado para facilitar a busca por informações de transporte, mostrando detalhes de linhas, paradas e horários, além de personalizar a experiência do usuário com base em seu status de estudante, aplicando desconto na tarifa quando aplicável.

Funcionalidades
O sistema oferece as seguintes funcionalidades:

Identificação do Usuário:

Ao iniciar o sistema, o usuário é solicitado a fornecer seu nome e se ele é estudante. Se for, ele recebe uma tarifa reduzida de R$2,25 (metade da tarifa normal).
Pesquisa de Linhas de Ônibus:

O usuário pode pesquisar por número de linha, recebendo como resultado as paradas que essa linha faz e a tarifa associada.
Pesquisa de Paradas:

O sistema permite ao usuário buscar uma parada pelo nome e mostrar quais linhas passam por essa parada.
Pesquisa de Localização:

A localização de uma parada também pode ser pesquisada, exibindo todas as paradas próximas e as linhas que passam por elas.
Pesquisa de Horários:

O usuário pode pesquisar por horários e visualizar quais linhas passam nas paradas nesse horário específico.
Tratamento de Exceções:

Caso o usuário insira dados incorretos ou inválidos, o sistema exibe uma mensagem adequada e permite novas tentativas.
Herança:

O sistema utiliza herança para organizar a estrutura de classes, facilitando a extensão de funcionalidades.
Linhas de Transporte
As linhas cadastradas no sistema são:

Linha 26:

Paradas: Midway (Tirol), Shopping (Capim Macio), Praia (Ponta Negra), IFRN (Tirol)
Horários:
Midway: 8:00
Shopping: 9:00
Praia: 9:30
IFRN: 13:00
Linha 54:

Paradas: Midway, Shopping, Praia, Academia (Capim Macio)
Horários:
Midway: 10:00
Shopping: 7:00
Praia: 6:30
Academia: 8:00
Linha 46:

Paradas: IFRN, Shopping, Praia, Academia, Conjunto (Ponta Negra)
Horários:
IFRN: 7:00
Shopping: 16:00
Praia: 8:30
Academia: 14:00
Conjunto: 18:00
Linha 73:

Paradas: Praia, Midway, Conjunto, Academia
Horários:
Praia: 6:30
Midway: 12:00
Academia: 17:00
Conjunto: 18:00
Tarifa
Tarifa Normal: R$ 4,50
Tarifa Reduzida (Estudantes): R$ 2,25
Requisitos Técnicos
Linguagem de Programação: Python 3.x
Bibliotecas utilizadas: datetime para manipulação de horários.

Exemplo de uso
Início:

O sistema pedirá seu nome e se você é estudante.
Pesquisa por Linha:

O usuário pode digitar 'linha' e inserir o número da linha para obter as paradas e a tarifa associada.
Pesquisa por Parada:

O usuário pode digitar 'parada' e inserir o nome da parada para ver quais linhas passam por ela.
Pesquisa por Localização:

O usuário pode digitar 'localizacao' e inserir a localização para encontrar as paradas nessa área.
Pesquisa por Horário:

O usuário pode digitar 'horario' e inserir um horário para ver quais ônibus passam nesse horário.
Tratamento de Exceções
Se um dado incorreto for inserido (como uma linha inexistente ou nome de parada errado), o sistema informará ao usuário e solicitará uma nova entrada.
Estrutura do Código
O código está organizado em classes:

Parada: Representa uma parada de ônibus.
LinhaDeTransporte: Representa uma linha de transporte, contendo uma lista de paradas e horários.
Horario: Representa os horários dos ônibus em cada parada.
SistemaDeTransporte: Gerencia todas as linhas e pesquisas realizadas pelo usuário.
