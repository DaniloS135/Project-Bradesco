class Main:
    pass

from Cliente import Cliente

from Conta import Conta

c1 = Cliente("Danilo", "114444-2222" )
conta = Conta(0, 7200, c1._nome)

conta.deposita(100)
conta.saque(50)
conta.extrato()
