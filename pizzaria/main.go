package main

import (
	"pizzaria/models"

	"github.com/gin-gonic/gin"
)

func main() {
	models.LoadPizzas()
	router := gin.Default()
	router.GET("/pizzas", models.GetPizzas)
	router.POST("/pizzas", models.PostPizzas)
	router.GET("/pizzas/:id", models.GetPizzasByID)
	router.Run()
}
