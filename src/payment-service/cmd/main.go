package main

import (
	"github.com/hiroki-it/payment-service/cmd/infrastructure/database"
	"github.com/hiroki-it/payment-service/cmd/infrastructure/logger"
	"github.com/hiroki-it/payment-service/cmd/infrastructure/routers"
)

func main() {

	log, err := logger.NewLogger()

	if err != nil {
		panic(err)
	}

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
