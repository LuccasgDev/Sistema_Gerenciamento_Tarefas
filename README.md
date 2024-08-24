# Gerenciador de Tarefas

Este é um simples gerenciador de tarefas baseado em terminal, escrito em Python. O aplicativo permite adicionar, listar e remover tarefas, armazenando-as em um arquivo de texto.

## Funcionalidades

- **Adicionar Tarefa**: Permite adicionar uma nova tarefa à lista.
- **Listar Tarefas**: Exibe todas as tarefas salvas.
- **Remover Tarefa**: Permite remover uma tarefa existente pelo índice.
- **Salvar e Sair**: Encerra o programa.

## Requisitos

- Python 3.x

## Como Usar

1. Clone o repositório ou baixe o arquivo Python.
2. Execute o script:

    ```bash
    python gerenciador_tarefas.py
    ```

3. Interaja com o aplicativo usando o menu que será exibido no terminal. As opções são:
    1. **Adicionar Tarefa**: Digite uma descrição e adicione uma nova tarefa.
    2. **Listar Tarefas**: Veja todas as tarefas atualmente armazenadas.
    3. **Remover Tarefa**: Escolha um número de tarefa para remover.
    4. **Salvar e Sair**: Salve as alterações e saia do programa.

## Arquivo de Dados

O programa utiliza um arquivo de texto chamado `tarefas.txt` para armazenar as tarefas. Se o arquivo não existir, ele será criado automaticamente.

## Observações

- O programa foi desenvolvido para sistemas Windows, utilizando o comando `cls` para limpar a tela. Se você estiver utilizando outro sistema operacional, como Linux ou macOS, substitua `cls` por `clear` no código para limpar a tela.
- Certifique-se de ter permissão para criar e modificar arquivos no diretório onde o script é executado.

## Exemplo de Execução

```plaintext
======================
====== SISTEMA =======
== GERENCIAR TAREFA ==
======================
1 - ADICIONAR TAREFA
2 - LISTAR TAREFAS
3 - REMOVER TAREFA
4 - SALVAR E SAIR
Escolha uma opção:
