package main

import (
	"gorm.io/gorm"

	"github.com/hiroki-it/payment-service/cmd/infrastructure/database"
	"github.com/hiroki-it/payment-service/cmd/infrastructure/routers"
)

func main() {
	// データベースに接続します．
	db, err := database.NewDB()

	if err != nil {
		panic(err)
	}

	// 最後にデータベースとの接続を切断します．
	defer func(db *gorm.DB) {
		database.Close(db)
	}(db)

	// コントローラにルーティングします．
	routers.Run()
}
