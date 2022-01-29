package routers

import (
	"github.com/gin-gonic/gin"
	"github.com/hiroki-it/account/cmd/interface/controllers"
)

func Run() {

	r := gin.Default()

	c := controllers.NewAccountController()

	r.Group("/account")
	{
		r.GET("/:id", c.ShowAccount)
		r.POST("/", c.CreateAccount)
		r.PUT("/", c.UpdateAccount)
		r.DELETE("/", c.DeleteAccount)
	}

	r.Run()
}
