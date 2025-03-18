from typing import Dict, List, Tuple, Set
import re

class BaseConhecimento:
    def __init__(self):
        self.regras = []
        self.fatos = set()
        
    def adicionar_regra(self, condicoes_se: List[str], conclusao_entao: str):
        self.regras.append({"se": condicoes_se, "entao": conclusao_entao})
        
    def adicionar_fato(self, fato: str):
        self.fatos.add(fato)
        
    def obter_regras(self):
        return self.regras
        
    def obter_fatos(self):
        return self.fatos

class MotorInferencia:
    def __init__(self, base_conhecimento: BaseConhecimento):
        self.bc = base_conhecimento
        self.explicacao = []
        
    def encadeamento_frente(self, objetivo: str = None) -> bool:
        novos_fatos = set()
        while True:
            acionado = False
            for regra in self.bc.obter_regras():
                if all(cond in self.bc.obter_fatos() for cond in regra["se"]):
                    conclusao = regra["entao"]
                    if conclusao not in self.bc.obter_fatos():
                        novos_fatos.add(conclusao)
                        self.explicacao.append(f"Regra aplicada: SE {' E '.join(regra['se'])} ENTÃO {conclusao}")
                        acionado = True
            
            if not acionado:
                break
                
            self.bc.fatos.update(novos_fatos)
            if objetivo in novos_fatos:
                return True
        return objetivo in self.bc.obter_fatos() if objetivo else True

    def encadeamento_tras(self, objetivo: str) -> bool:
        if objetivo in self.bc.obter_fatos():
            return True
            
        for regra in self.bc.obter_regras():
            if regra["entao"] == objetivo:
                if all(self.encadeamento_tras(condicao) for condicao in regra["se"]):
                    self.explicacao.append(f"Provado {objetivo} usando regra: SE {' E '.join(regra['se'])} ENTÃO {regra['entao']}")
                    return True
        return False

    def obter_explicacao(self) -> List[str]:
        return self.explicacao

class InterfaceLinguagemNatural:
    def __init__(self, base_conhecimento: BaseConhecimento, motor_inferencia: MotorInferencia):
        self.bc = base_conhecimento
        self.mi = motor_inferencia
        
    def processar_entrada(self, entrada_usuario: str) -> str:
        if "por que" in entrada_usuario.lower():
            return "\n".join(self.mi.obter_explicacao())
        return "Não entendi essa pergunta."