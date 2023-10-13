import random
import string

def generate_secure_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)):
            break

    return password

def print_dashed_line(length):
    print('-' * (length + 28))  # Adicionei 28 caracteres para compensar o texto adicional

if __name__ == "__main__":
    while True:
        user_input = input("Digite o comprimento desejado da senha ou 'SAIR' para sair: ")
        
        if user_input.upper() == 'SAIR':
            break

        try:
            length = int(user_input)
            if length < 8:
                print("A senha deve ter pelo menos 8 caracteres.")
            else:
                password = generate_secure_password(length)
                print_dashed_line(length)
                print(f"Senha segura gerada: {password}")
                print_dashed_line(length)
        except ValueError:
            print("Digite um valor numérico válido para o comprimento da senha.")