from gerenciador_credito import avaliar_risco_credito
from diagnostico_medico import diagnosticar
from mini_akinator import MiniAkinator

def main():
    while True:
        print("\nDemo do Sistema Baseado em Conhecimento")
        print("1. Avaliação de Risco de Crédito")
        print("2. Diagnóstico Médico")
        print("3. Mini Akinator")
        print("4. Sair")
        
        escolha = input("Selecione uma opção: ")
        
        if escolha == "1":
            resultado, explicacao = avaliar_risco_credito()
            print(f"\nAvaliação de Risco de Crédito: {resultado}")
            print("\nJustificativa da decisão:")
            print(explicacao)
            
        elif escolha == "2":
            print("\nVou fazer algumas perguntas sobre seus sintomas.")
            resultado = diagnosticar()
            print(f"Possíveis Diagnósticos: {resultado}")
            
        elif escolha == "3":
            akinator = MiniAkinator()
            resultado = akinator.jogar()
            print(resultado)
            
        elif escolha == "4":
            break

if __name__ == "__main__":
    main()