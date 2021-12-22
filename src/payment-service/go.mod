module github.com/hiroki-it/payment-service

go 1.16

require (
	github.com/gin-gonic/gin v1.7.2
	github.com/joho/godotenv v1.4.0
	go.uber.org/zap v1.19.1
	gorm.io/driver/mysql v1.2.1
	gorm.io/gorm v1.22.4
)

replace github.com/hiroki-it/payment-service => /
