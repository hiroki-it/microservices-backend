package main

import (
	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()

	r.GET("/swg/", func(c *gin.Context) {
		c.String(200, "Hello world!")
	})

	r.Run()
}
