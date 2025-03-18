from sistema_conhecimento import BaseConhecimento, MotorInferencia, InterfaceLinguagemNatural

class MiniAkinator:
    def __init__(self):
        self.bc = BaseConhecimento()
        self.mi = MotorInferencia(self.bc)
        self.inicializar_base_conhecimento()
        
    def inicializar_base_conhecimento(self):
        self.bc.adicionar_regra(["eh_bruxo", "tem_cicatriz", "usa_oculos"], "harry_potter")
        self.bc.adicionar_regra(["eh_princesa", "tem_cabelo_longo", "mora_em_torre"], "rapunzel")
        self.bc.adicionar_regra(["eh_rato", "usa_shorts_vermelho", "tem_orelhas_grandes"], "mickey_mouse")
        
    def fazer_pergunta(self, pergunta: str) -> bool:
        resposta = input(f"{pergunta} (sim/nao): ").lower()
        return resposta == "sim"
        
    def jogar(self):
        self.bc.fatos = set()
        
        # First question to determine character type
        if self.fazer_pergunta("O personagem é um bruxo?"):
            self.bc.adicionar_fato("eh_bruxo")
            if self.fazer_pergunta("O personagem tem uma cicatriz?"):
                self.bc.adicionar_fato("tem_cicatriz")
                if self.fazer_pergunta("O personagem usa óculos?"):
                    self.bc.adicionar_fato("usa_oculos")
        
        elif self.fazer_pergunta("O personagem é uma princesa?"):
            self.bc.adicionar_fato("eh_princesa")
            if self.fazer_pergunta("O personagem tem cabelo muito longo?"):
                self.bc.adicionar_fato("tem_cabelo_longo")
                if self.fazer_pergunta("O personagem mora em uma torre?"):
                    self.bc.adicionar_fato("mora_em_torre")
        
        elif self.fazer_pergunta("O personagem é um rato?"):
            self.bc.adicionar_fato("eh_rato")
            if self.fazer_pergunta("O personagem usa shorts vermelho?"):
                self.bc.adicionar_fato("usa_shorts_vermelho")
                if self.fazer_pergunta("O personagem tem orelhas grandes?"):
                    self.bc.adicionar_fato("tem_orelhas_grandes")
        
        for regra in self.bc.obter_regras():
            if self.mi.encadeamento_tras(regra["entao"]):
                return f"Acho que é {regra['entao'].replace('_', ' ').title()}!"
                
        return "Desculpe, não consegui adivinhar o personagem!"