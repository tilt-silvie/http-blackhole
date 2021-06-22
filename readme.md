# http-blackhole

あらゆるパス、あらゆるメソッドのHTTPリクエストを受け、ヘッダーとボディのデータをダンプするツールです。

## Usage

起動します。
```
docker build -t http-blackhole .
docker run -it -p 8080:80 http-blackhole 
```

以下のようにアクセスすると、http-blackholeを起動している端末にヘッダーとボディの情報がダンプされます。

```
curl http://localhost:8080/<任意のパス>
```


