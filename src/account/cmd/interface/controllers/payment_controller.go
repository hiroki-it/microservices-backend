package controllers

import (
	"github.com/gin-gonic/gin"
)

type AccountController struct {
}

func NewAccountController() *AccountController {
	return &AccountController{}
}

func (ac *AccountController) ShowAccount(context *gin.Context) {
}

func (ac *AccountController) CreateAccount(context *gin.Context) {
}

func (ac *AccountController) UpdateAccount(context *gin.Context) {
}

func (ac *AccountController) DeleteAccount(context *gin.Context) {
}
