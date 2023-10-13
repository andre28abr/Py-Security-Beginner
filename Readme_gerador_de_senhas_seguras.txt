# GERADOR DE SENHAS SEGURAS

Este é um pequeno programa em Python que gera senhas seguras aleatórias com base no comprimento especificado pelo usuário. As senhas geradas atendem a critérios de segurança, como a inclusão de letras maiúsculas, letras minúsculas, dígitos e caracteres especiais.

## Passo a passo do código

### 1. Importação de bibliotecas

```python
import random
import string
```

Neste passo, importamos as bibliotecas `random` e `string`, que são usadas para gerar senhas aleatórias e trabalhar com caracteres.

### 2. Definição da função `generate_secure_password`

```python
def generate_secure_password(length):
    # ...
```

A função `generate_secure_password` é responsável por gerar senhas seguras com base no comprimento especificado. Ela gera senhas aleatórias até que todos os critérios de segurança sejam atendidos (letras maiúsculas, minúsculas, dígitos e caracteres especiais).

### 3. Definição da função `print_dashed_line`

```python
def print_dashed_line(length):
    # ...
```

A função `print_dashed_line` é usada para imprimir uma linha tracejada na tela, cujo tamanho é baseado no comprimento da senha gerada.

### 4. Bloco principal

```python
if __name__ == "__main__":
    # ...
```

O código principal é executado quando o arquivo é executado diretamente (não importado como um módulo).

### 5. Loop principal

```python
while True:
    user_input = input("Digite o comprimento desejado da senha ou 'SAIR' para sair: ")
    
    if user_input.upper() == 'SAIR':
        break
```

O programa entra em um loop onde o usuário é solicitado a fornecer o comprimento desejado da senha. Se o usuário digitar "SAIR," o loop é interrompido e o programa termina.

### 6. Validação do comprimento

```python
try:
    length = int(user_input)
    if length < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
    else:
        # Geração da senha e impressão
        password = generate_secure_password(length)
        print_dashed_line(length)
        print(f"Senha segura gerada: {password}")
        print_dashed_line(length)
except ValueError:
    print("Digite um valor numérico válido para o comprimento da senha.")
```

Dentro do loop, o programa tenta converter a entrada do usuário em um número inteiro e verifica se é maior ou igual a 8. Se a validação for bem-sucedida, uma senha segura é gerada e exibida na tela, cercada por linhas tracejadas cujo tamanho é baseado no comprimento da senha. Se o usuário fornecer uma entrada inválida, o programa informará que um valor numérico válido é necessário.