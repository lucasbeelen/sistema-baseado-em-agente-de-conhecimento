from typing import List
from sistema_conhecimento import BaseConhecimento, MotorInferencia, InterfaceLinguagemNatural

def criar_sistema_medico():
    bc = BaseConhecimento()
    
    bc.adicionar_regra(["febre", "tosse", "fadiga"], "possivel_covid")
    bc.adicionar_regra(["febre", "garganta_inflamada"], "possivel_gripe")
    bc.adicionar_regra(["nariz_escorrendo", "espirros", "tosse"], "resfriado_comum")
    bc.adicionar_regra(["possivel_covid", "teste_positivo"], "covid_confirmado")
    
    mi = MotorInferencia(bc)
    interface = InterfaceLinguagemNatural(bc, mi)
    
    return bc, mi, interface

def fazer_pergunta(pergunta: str) -> bool:
    resposta = input(f"{pergunta} (sim/nao): ").lower()
    return resposta == "sim"

def diagnosticar():
    bc, mi, _ = criar_sistema_medico()
    sintomas = []
    
    # Perguntas sobre sintomas
    if fazer_pergunta("Você está com febre?"):
        sintomas.append("febre")
    
    if fazer_pergunta("Você está com tosse?"):
        sintomas.append("tosse")
    
    if fazer_pergunta("Você está sentindo fadiga?"):
        sintomas.append("fadiga")
    
    if fazer_pergunta("Sua garganta está inflamada?"):
        sintomas.append("garganta_inflamada")
    
    if fazer_pergunta("Seu nariz está escorrendo?"):
        sintomas.append("nariz_escorrendo")
    
    if fazer_pergunta("Você está espirrando muito?"):
        sintomas.append("espirros")
    
    # Se houver suspeita de COVID, perguntar sobre teste
    if "febre" in sintomas and "tosse" in sintomas:
        if fazer_pergunta("Você fez teste de COVID e deu positivo?"):
            sintomas.append("teste_positivo")
    
    # Adicionar sintomas como fatos
    for sintoma in sintomas:
        bc.adicionar_fato(sintoma)
    
    # Verificar possíveis condições
    possiveis_condicoes = ["covid_confirmado", "possivel_covid", "possivel_gripe", "resfriado_comum"]
    diagnosticos = []
    
    for condicao in possiveis_condicoes:
        if mi.encadeamento_tras(condicao):
            diagnosticos.append(condicao)
            
    return diagnosticos if diagnosticos else ["Nenhum diagnóstico claro"]