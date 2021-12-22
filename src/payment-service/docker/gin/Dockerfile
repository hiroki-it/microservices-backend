#===================
# Global ARG
#===================
ARG GO_VERSION=1.16.11
ARG LABEL="Hiroki <hasegawafeedshop@gmail.com>"

#===================
# Build Stage
#===================
FROM golang:${GO_VERSION} as build

WORKDIR /go/src

# インストールのキャッシュを活用するためにコピーしておく．
COPY go.mod go.sum /go/src/

# ライブラリをインストールする．
RUN go get github.com/cosmtrek/air@v1.27.8

COPY . /go/src/

# go mod tidyの実行を忘れると，次回のイメージのビルド時に，goのビルドに失敗するようになってしまう．
# そのため，保険としてgo mod tidyを実行しておく．
RUN go mod tidy \
  # コンテナが起動後にすぐ終了しないように，起動前にフレームワークをインストールしておく．
  && go mod download -x \
# ビルドのアーティファクトを/go/binに配置する．
# NOTE: netパッケージは標準で動的リンクのため，静的リンクを明示的に指定する必要がある．
  && go build -x -a -tags netgo -installsuffix netgo -o /go/bin ./cmd

#===================
# Production Stage
#===================
FROM golang:${GO_VERSION}-alpine

LABEL maintainer=${LABEL}

# /go/binにパスを通す．
ENV PATH $PATH:/go/bin

ENV LANG ja_JP.UTF-8
ENV TZ Asia/Tokyo
# ビルドするバイナリファイルを静的リンク化する．
ENV CGO_ENABLED 0 
ENV GOARCH amd64
ENV GOOS linux

COPY --from=build /go /go/

WORKDIR /go/src

CMD ["/go/bin/cmd"]
