package routers

import (
	"github.com/gin-gonic/gin"
	"github.com/hiroki-it/account/cmd/controllers"
)

func Run() {

	r := gin.Default()

	ac := controllers.NewAccountController()

	r.Group("/account")
	{
		r.GET("/:id", ac.ShowAccount)
		r.POST("/", ac.CreateAccount)
		r.PUT("/", ac.UpdateAccount)
		r.DELETE("/", ac.DeleteAccount)
	}

	r.Run()
}
