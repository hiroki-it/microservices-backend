package routers

import (
	"github.com/gin-gonic/gin"
	"github.com/hiroki-it/payment-service/cmd/interface/controllers"
)

func Run() {

	r := gin.Default()

	c := controllers.NewPaymentController()

	r.Group("/payment")
	{
		r.GET("/:id", c.ShowPayment)
		r.POST("/", c.CreatePayment)
		r.PUT("/", c.UpdatePayment)
		r.DELETE("/", c.DeletePayment)
	}

	r.Run()
}
