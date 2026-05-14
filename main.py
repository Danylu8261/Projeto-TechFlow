# Script de validação de prioridades

def validar_prioridade(prioridade):
    prioridades_validas = ['Baixa', 'Média', 'Alta']
    return prioridade in prioridades_validas

if __name__ == "__main__":
    p = input("Digite a prioridade (Baixa, Média, Alta): ")
    if validar_prioridade(p):
        print(f"LOG: Prioridade '{p}' aceita com sucesso.")
    else:
        print(f"ERRO: '{p}' não é uma prioridade válida para o TechFlow.")
        # Versão final do desafio - TechFlow v1.0
    ```