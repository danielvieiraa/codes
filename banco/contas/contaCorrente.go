package contas

import "banco/clientes"

type ContaCorrente struct {
	Titular              clientes.Titular
	Agencia, NumeroConta int
	saldo                float64
}

func (c *ContaCorrente) Sacar(valorSaque float64) string {
	podeSacar := valorSaque > 0 && valorSaque <= c.saldo

	if podeSacar {
		c.saldo -= valorSaque
		return "Saque realizado com sucesso"
	} else {
		return "saldo indisponivel"
	}
}

func (c *ContaCorrente) Depositar(valorDeposito float64) (string, float64) {
	if valorDeposito > 0 {
		c.saldo += valorDeposito
		return "Depósito realizado com sucesso", c.saldo
	} else {
		return "Valor do depósito é inválido", c.saldo
	}
}

func (c *ContaCorrente) Transferir(valorTransferencia float64, contaDestino *ContaCorrente) bool {
	if valorTransferencia < c.saldo+1 && valorTransferencia > 0 {
		c.saldo -= valorTransferencia
		contaDestino.saldo += valorTransferencia
		return true
	} else {
		return false
	}
}

func (c *ContaCorrente) GetSaldo() float64 {
	return c.saldo
}
