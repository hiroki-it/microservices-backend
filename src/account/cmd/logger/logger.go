package logger

import (
	"go.uber.org/zap"
)

type Logger struct {
	log *zap.Logger
}

// NewLogger コンストラクタ
func NewLogger() (*Logger, error) {
	log, err := zap.NewDevelopment()

	if err != nil {
		return nil, err
	}

	return &Logger{
		log: log,
	}, nil
}

// Log logを返却します．
func (l *Logger) Log() *zap.Logger {
	return l.log
}
