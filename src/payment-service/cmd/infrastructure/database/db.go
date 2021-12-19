package database

import (
	"fmt"
	"os"

	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)

// NewDB コンストラクタ
func NewDB() (*gorm.DB, error) {
	dsn := fmt.Sprintf(
		"%s:%s@tcp(%s:%s)/%s?charset=utf8&parseTime=True&loc=Local",
		os.Getenv("DB_PASSWORD"),
		os.Getenv("DB_USER"),
		os.Getenv("DB_HOST"),
		os.Getenv("DB_PORT"),
		os.Getenv("DB_DATABASE"),
	)

	db, err := gorm.Open(mysql.Open(dsn), &gorm.Config{})

	if err != nil {
		return nil, err
	}

	return db, nil
}

func Close(db *gorm.DB) error {

	sqlDb, err := db.DB()

	if err != nil {
		return err
	}

	err = sqlDb.Close()

	if err != nil {
		return err
	}

	return nil
}
