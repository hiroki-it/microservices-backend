package controllers

import (
	"github.com/gin-gonic/gin"
)

type AccountController struct {
}

func NewAccountController() *AccountController {
	return &AccountController{}
}

func (pc *AccountController) ShowAccount(context *gin.Context) {
}

func (pc *AccountController) CreateAccount(context *gin.Context) {
}

func (pc *AccountController) UpdateAccount(context *gin.Context) {
}

func (pc *AccountController) DeleteAccount(context *gin.Context) {
}
