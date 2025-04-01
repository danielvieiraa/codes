<?php
    class Veiculo {
        public $marca;
        public $modelo;
        public $ano;

        public function __construct($marca, $modelo, $ano) {
            $this->marca = $marca;
            $this->modelo = $modelo;
            $this->ano = $ano;
        }

        public function exibirFicha() {
            return "Carro: {$this->marca} {$this->modelo}, Ano: {$this->ano}";
        }
    }

    $meuCarro = new Veiculo("Honda", "Civic", 2017);

    echo $meuCarro->exibirFicha();
?>