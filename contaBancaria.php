<?php
    class ContaBancaria {
        public $titular;
        private $saldo;
        public $numeroConta;

        public function __construct($titular, $saldoInicial, $numeroConta) {
            $this->titular = $titular;
            $this->saldo = $saldoInicial;
            $this->numeroConta = $numeroConta;
        }

        public function depositar($valor) {
            if ($valor > 0) {
                $this->saldo += $valor;
                echo "Depósito realizado com sucesso.<br>";
            } else {
                echo "Valor de depósito inválido.<br>";
            }
        }

        public function sacar($valor) {
            if ($valor > 0 && $valor <= $this->saldo) {
                $this->saldo -= $valor;
                echo "Saque realizado com sucesso <br>";
            } else {
                echo "Saldo indisponivel <br>";
            }
        }

        public function verSaldo() {
            echo "Saldo: R$ $this->saldo <br>";
        }
    }

    $conta1 = new ContaBancaria("João", 1000, "12345");

    $conta1->verSaldo();
    $conta1->depositar(500);
    $conta1->verSaldo();
    $conta1->sacar(300);
    $conta1->verSaldo();
?>