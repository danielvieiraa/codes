package contas

import "banco/clientes"

type ContaPoupanca struct {
	Titular                        clientes.Titular
	Agencia, NumeroConta, Operacao int
	saldo                          float64
}

func (c *ContaPoupanca) Sacar(valorSaque float64) string {
	podeSacar := valorSaque > 0 && valorSaque <= c.saldo

	if podeSacar {
		c.saldo -= valorSaque
		return "Saque realizado com sucesso"
	} else {
		return "saldo indisponivel"
	}
}

func (c *ContaPoupanca) Depositar(valorDeposito float64) (string, float64) {
	if valorDeposito > 0 {
		c.saldo += valorDeposito
		return "Depósito realizado com sucesso", c.saldo
	} else {
		return "Valor do depósito é inválido", c.saldo
	}
}

func (c *ContaPoupanca) Transferir(valorTransferencia float64, contaDestino *ContaPoupanca) bool {
	if valorTransferencia < c.saldo+1 && valorTransferencia > 0 {
		c.saldo -= valorTransferencia
		contaDestino.saldo += valorTransferencia
		return true
	} else {
		return false
	}
}

func (c *ContaPoupanca) GetSaldo() float64 {
	return c.saldo
}
