// Deve-se criar um txt com as urls que irão ser monitoradas

package main

import (
	"bufio"
	"fmt"
	"io"
	"net/http"
	"os"
	"strconv"
	"strings"
	"time"
)

const monitoramentos = 3
const delay = 5

func main() {
	nome := "Daniel"
	versao := 1.1

	fmt.Println("Olá,", nome)
	fmt.Println("Versão ", versao)

	for {
		fmt.Println("1- Iniciar Monitoramento")
		fmt.Println("2- Exibir Logs")
		fmt.Println("0- Sair")

		var option int
		fmt.Scan(&option)

		switch option {
		case 1:
			iniciarMonitoramento()
		case 2:
			exibeLogs()
		case 0:
			os.Exit(0)
		default:
			fmt.Println("Opção inválida")
		}
	}
}

func iniciarMonitoramento() {
	sites := leSiteArquivo()

	for i := 0; i < monitoramentos; i++ {
		for i, site := range sites {
			fmt.Println(i, site)
			testaSite(site)
		}
		time.Sleep(delay * time.Second)
		fmt.Println("")
	}
	fmt.Println("")
}

func testaSite(site string) {
	response, erro := http.Get(site)

	if erro != nil {
		fmt.Println("Erro:", erro)
	}

	if response.StatusCode == 200 {
		fmt.Println("O site:", site, "foi carregado com sucesso!")
		registraLog(site, true)
	} else {
		fmt.Println("Erro ao carregar site. Status code:", response.StatusCode)
		registraLog(site, false)
	}
}

func leSiteArquivo() []string {

	var sites []string

	arquivo, erro := os.Open("sites.txt")

	if erro != nil {
		fmt.Println("Ocorreu um erro:", erro)
	}

	leitor := bufio.NewReader(arquivo)
	for {
		linha, erro := leitor.ReadString('\n')
		linha = strings.TrimSpace(linha)

		sites = append(sites, linha)

		if erro == io.EOF {
			break
		}

	}

	arquivo.Close()
	return sites
}

func registraLog(site string, status bool) {
	arquivo, erro := os.OpenFile("log.txt", os.O_RDWR|os.O_CREATE|os.O_APPEND, 0666)

	if erro != nil {
		fmt.Println(erro)
	}

	arquivo.WriteString(time.Now().Format("02/01/2006 15:04:05") + " - " + site + " - online: " + strconv.FormatBool(status) + "\n")

	arquivo.Close()
}

func exibeLogs() {
	arquivo, erro := os.ReadFile("log.txt")

	if erro != nil {
		fmt.Println(erro)
	}

	fmt.Println(string(arquivo))
}
