from sistema_conhecimento import BaseConhecimento, MotorInferencia, InterfaceLinguagemNatural

def criar_gerenciador_credito():
    bc = BaseConhecimento()
    
    # Regras para renda baixa ($0 a $15k)
    bc.adicionar_regra(["renda_0_15k", "divida_alta"], "risco_alto")
    bc.adicionar_regra(["renda_0_15k", "divida_baixa"], "risco_moderado")
    bc.adicionar_regra(["renda_0_15k", "historico_ruim"], "risco_alto")
    
    # Regras para renda média ($15k a $35k)
    bc.adicionar_regra(["renda_15_35k", "historico_ruim"], "risco_alto")
    bc.adicionar_regra(["renda_15_35k", "historico_bom"], "risco_baixo")
    bc.adicionar_regra(["renda_15_35k", "historico_desconhecido"], "risco_moderado")
    
    # Regras para renda alta (acima de $35k)
    bc.adicionar_regra(["renda_acima_35k", "historico_bom"], "risco_baixo")
    bc.adicionar_regra(["renda_acima_35k", "historico_desconhecido"], "risco_baixo")
    bc.adicionar_regra(["renda_acima_35k", "historico_ruim", "divida_baixa"], "risco_moderado")
    bc.adicionar_regra(["renda_acima_35k", "historico_ruim", "divida_alta"], "risco_alto")
    
    mi = MotorInferencia(bc)
    interface = InterfaceLinguagemNatural(bc, mi)
    
    return bc, mi, interface

def fazer_pergunta(pergunta: str) -> bool:
    resposta = input(f"{pergunta} (sim/nao): ").lower()
    return resposta == "sim"

def avaliar_risco_credito():
    bc, mi, _ = criar_gerenciador_credito()
    
    print("\nAvaliação de Renda:")
    print("1. $0 a $15.000")
    print("2. $15.001 a $35.000")
    print("3. Acima de $35.000")
    renda = input("Escolha a faixa de renda (1/2/3): ")
    
    if renda == "1":
        bc.adicionar_fato("renda_0_15k")
    elif renda == "2":
        bc.adicionar_fato("renda_15_35k")
    else:
        bc.adicionar_fato("renda_acima_35k")
    
    print("\nHistórico de Crédito:")
    print("1. Bom")
    print("2. Ruim")
    print("3. Desconhecido")
    historico = input("Escolha o tipo de histórico (1/2/3): ")
    
    if historico == "1":
        bc.adicionar_fato("historico_bom")
    elif historico == "2":
        bc.adicionar_fato("historico_ruim")
    else:
        bc.adicionar_fato("historico_desconhecido")
    
    print("\nNível de Dívida:")
    print("1. Alta")
    print("2. Baixa")
    divida = input("Escolha o nível de dívida (1/2): ")
    
    if divida == "1":
        bc.adicionar_fato("divida_alta")
    else:
        bc.adicionar_fato("divida_baixa")
    
    # Avaliar risco usando encadeamento para trás
    for nivel_risco in ["risco_baixo", "risco_moderado", "risco_alto"]:
        if mi.encadeamento_tras(nivel_risco):
            explicacao = "\n".join(mi.obter_explicacao())
            return nivel_risco, explicacao
            
    return "Não foi possível determinar o risco", ""