package main

import (
	"banco/contas"
	"fmt"
)

func PagarBoleto(conta verificarConta, valorDoBoleto float64) {
	conta.Sacar(valorDoBoleto)
}

type verificarConta interface {
	Sacar(valor float64) string
}

func main() {
	contaDaniel := contas.ContaPoupanca{}
	contaDaniel.Depositar(100)
	PagarBoleto(&contaDaniel, 50)

	fmt.Println(contaDaniel)
}
