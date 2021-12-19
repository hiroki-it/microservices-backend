package main

import (
	"github.com/gin-gonic/gin"
)

type Order struct {
	Id      int `json:"number"`
	FoodId  int `json:"number"`
	DrinkId int `json:"number"`
}

func main() {
	r := gin.Default()

	r.Group("/payment")
	{
		r.GET("/", func(c *gin.Context) {
			c.String(200, "Hello world!")
		})

		// 簡単な計算を実行します．
		r.POST("/", func(c *gin.Context) {
			input := &Input{}
			_ = c.Bind(input)
			result := input.Number * 2
			c.JSON(200, result)
		})
	}

	r.Run()
}
