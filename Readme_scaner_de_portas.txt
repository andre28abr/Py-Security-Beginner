# SCANER DE PORTAS EM PYTHON

Este é um código Python simples para escanear portas em um host alvo. O programa permite que você especifique o host alvo e as portas a serem verificadas. Ele detecta as portas abertas no host e exibe as informações relevantes.

## Como usar o scanner

1. O programa solicitará algumas informações:

   - Digite o host alvo (pode ser um endereço IP ou nome de domínio).
   - Digite as portas a serem verificadas, separadas por vírgulas (por exemplo, `80, 443, 22`) ou digite 'TODAS' para escanear todas as portas disponíveis.

2. O scanner verificará as portas especificadas no host alvo. Ele exibirá uma lista de portas abertas ou uma mensagem indicando que nenhuma porta aberta foi encontrada.

## Como funciona o código

O código utiliza a biblioteca `socket` do Python para criar soquetes e verificar a conectividade em cada porta especificada. Aqui está uma visão geral do funcionamento do código:

- Importa a biblioteca `socket`.
- Define uma função `scan_ports(target, ports)` para verificar as portas em um host alvo.
- Itera sobre a lista de portas especificadas.
- Tenta criar um soquete e conectar-se à porta especificada.
- Se a conexão for bem-sucedida (código de resultado igual a 0), a porta é considerada aberta e adicionada à lista de portas abertas.
- Exibe uma lista das portas abertas encontradas ou uma mensagem se nenhuma porta aberta for encontrada.

Lembre-se de que este é um scanner de portas simples, e sua utilização deve estar em conformidade com as leis e regulamentos locais. Certifique-se de ter permissão para escanear portas em um host antes de usá-lo em qualquer contexto.

Espero que esta explicação ajude a entender o código do scanner de portas Python. Se você tiver alguma dúvida adicional ou precisar de mais informações, sinta-se à vontade para perguntar.