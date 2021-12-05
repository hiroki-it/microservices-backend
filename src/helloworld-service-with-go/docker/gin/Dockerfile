#===================
# Global ARG
#===================
ARG GO_VERSION=1.16.5
ARG LABEL="Hiroki <hasegawafeedshop@gmail.com>"

#===================
# Build Stage
#===================
FROM golang:${GO_VERSION} as build

WORKDIR /go/src

# インストールのキャッシュを活用するためにコピーしておく．
COPY go.mod go.sum /go/src/

# ライブラリをインストールする．
RUN go get github.com/cosmtrek/air@v1.27.3

COPY . /go/src/

# ビルドのアーティファクトを/go/binに配置する．
# NOTE: netパッケージは標準で動的リンクのため，静的リンクを明示的に指定する必要がある．
RUN go build -x -a -tags netgo -installsuffix netgo -o /go/bin ./cmd

#===================
# Production Stage
#===================
FROM golang:${GO_VERSION}-alpine

LABEL maintainer=${LABEL}

# /go/binにパスを通す．
ENV PATH $PATH:/go/bin

COPY --from=build /go /go/

WORKDIR /go/src

CMD ["/go/bin/cmd"]
