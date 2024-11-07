package models

import (
	"encoding/json"
	"fmt"
	"os"
	"strconv"

	"github.com/gin-gonic/gin"
)

type Pizza struct {
	ID    int     `json:"id"`
	Nome  string  `json:"nome"`
	Preco float64 `json:"preco"`
}

var pizzas = []Pizza{}

func GetPizzas(c *gin.Context) {
	c.JSON(200, gin.H{
		"pizzas": pizzas,
	})
}

func PostPizzas(c *gin.Context) {
	var newPizza Pizza

	if err := c.ShouldBindJSON(&newPizza); err != nil {
		c.JSON(400, gin.H{
			"erro": err.Error(),
		})
		return
	}

	newPizza.ID = len(pizzas) + 1
	pizzas = append(pizzas, newPizza)
	SavePizza()
	c.JSON(201, newPizza)
}

func GetPizzasByID(c *gin.Context) {
	idParam := c.Param("id")
	id, err := strconv.Atoi(idParam)

	if err != nil {
		c.JSON(400, gin.H{
			"erro": err.Error(),
		})
		return
	}

	for _, p := range pizzas {
		if p.ID == id {
			c.JSON(200, p)
			return
		}
	}
	c.JSON(404, gin.H{"message": "Pizza not found"})
}

func LoadPizzas() {
	file, err := os.Open("dados.json")

	if err != nil {
		fmt.Println("Error file:", err)
		return
	}

	defer file.Close()
	decoder := json.NewDecoder(file)

	if err := decoder.Decode(&pizzas); err != nil {
		fmt.Println("Error decoding JSON: ", err)
	}
}

func SavePizza() {
	file, err := os.Create("dados.json")

	if err != nil {
		fmt.Println("Error file:", err)
		return
	}

	defer file.Close()
	encoder := json.NewEncoder(file)

	if err := encoder.Encode(&pizzas); err != nil {
		fmt.Println("Error encoding JSON: ", err)
	}
}
