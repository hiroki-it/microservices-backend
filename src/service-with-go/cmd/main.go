package main

import (
	"github.com/gin-gonic/gin"
)

type Input struct {
	Number int `json:"number"`
}

func main() {
	r := gin.Default()

	r.Group("/swg")
	{
		r.GET("/", func(c *gin.Context) {
			c.String(200, "Hello world!")
		})

		r.POST("/", func(c *gin.Context) {
			input := &Input{}
			_ = c.Bind(input)
			result := input.Number * 2
			c.JSON(200, result)
		})
	}

	r.Run()
}
