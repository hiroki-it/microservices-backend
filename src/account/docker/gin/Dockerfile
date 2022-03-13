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

# 参考：https://hiroki-it.github.io/tech-notebook-gitbook/public/software/software_application_procedural_language_go.html
RUN go mod tidy \
  && go mod download -x \
  && go build -x -a -tags netgo -installsuffix netgo -o /go/bin ./cmd

#===================
# Prd Stage
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
