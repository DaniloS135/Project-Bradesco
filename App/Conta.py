class Conta:
    def __init__(self, saldo, numero, titular):
        self.saldo= 0
        self.numero= numero
        self.titular= titular
        
    def saque(self, valor):
        if (self.saldo>= valor):
            self.saldo-= valor
            print("Saque realizado com sucesso.")
        else:
            print("Saldo Insuficiente")
    
    def deposita(self, valor):
        self.saldo+=valor
    
    def extrato(self):
        print("Cliente: ", self.titular, "Saldo atual: ", self._saldo)
        
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo):
        if (saldo < 0):
            print("saldo não pode ser negativo")
        else:
            self._saldo = saldo   
            
     
        """def get_saldo(self):
            return self._saldo
        
        def set_saldo(self, saldo):
            if (saldo<0):
                print("0 saldo não pode ser negativo")
            else:
                self._saldo = saldo"""
        