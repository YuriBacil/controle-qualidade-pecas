# Sistema de Controle de Qualidade e Caixas - UniFECAF

Projeto desenvolvido para a disciplina de Algoritmos e Logica de Programacao (Modulo 6).

A ideia do projeto e simular uma esteira de fabrica que avalia pecas automaticamente em vez de depender de inspecao manual. O script confere peso, tamanho e cor da peca, guarda as aprovadas em caixas de ate 10 unidades e registra o que deu errado com as reprovadas.

### Como funciona

O script roda no terminal e tem 5 opcoes:
1. Cadastrar peca: recebe id, peso (deve ter 95g a 105g), cor (azul ou verde) e comprimento (10cm a 20cm). Se passar em tudo vai pra caixa atual. Quando junta 10 pecas na caixa, ela fecha e abre outra.
2. Listar pecas: mostra as pecas aprovadas e as reprovadas com o motivo da falha.
3. Remover peca: exclui pelo ID e recalcula as caixas.
4. Listar caixas fechadas: mostra os lotes de 10 pecas que ja foram concluidos.
5. Relatorio final: resumo geral da linha de producao.

### Como rodar

Tendo o Python 3 instalado, e so abrir o terminal nesta pasta e executar:

python main.py

### Exemplos rapidos

Exemplo de peca aprovada:
- Digitando: ID 1, peso 100, cor azul, comprimento 15
- Resultado: "Peca 1 APROVADA! Adicionada na caixa (1/10)."

Exemplo de peca reprovada:
- Digitando: ID 2, peso 85, cor vermelho, comprimento 25
- Resultado: o sistema avisa que foi reprovada e lista os motivos (peso abaixo de 95g, cor invalida e tamanho acima de 20cm).

Quando a caixa enche com 10 pecas aprovadas, o sistema avisa na hora que a caixa foi fechada e comeca a contar a proxima.


