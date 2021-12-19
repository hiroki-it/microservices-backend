package controllers

import (
	"github.com/gin-gonic/gin"
)

type PaymentController struct {
}

func NewPaymentController() *PaymentController {
	return &PaymentController{}
}

func (pc *PaymentController) ShowPayment(context *gin.Context) {
}

func (pc *PaymentController) CreatePayment(context *gin.Context) {
}

func (pc *PaymentController) UpdatePayment(context *gin.Context) {
}

func (pc *PaymentController) DeletePayment(context *gin.Context) {
}
