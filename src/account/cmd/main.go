package main

import (
	"github.com/hiroki-it/account/cmd/infrastructure/database"
	"github.com/hiroki-it/account/cmd/infrastructure/logger"
	"github.com/hiroki-it/account/cmd/infrastructure/routers"
	"github.com/joho/godotenv"
	"gorm.io/gorm"
)

func main() {

	log, err := logger.NewLogger()

	if err != nil {
		panic(err)
	}

	err = godotenv.Load()

	if err != nil {
		log.Log().Error(err.Error())
	}

	// データベースに接続します．
	db, err := database.NewDB()

	if err != nil {
		log.Log().Error(err.Error())
	}

	// 最後にデータベースとの接続を切断します．
	defer func(db *gorm.DB) {
		database.Close(db)
	}(db)

	// コントローラにルーティングします．
	routers.Run()
}
