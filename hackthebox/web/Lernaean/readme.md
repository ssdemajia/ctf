最后使用wireshark查看请求过程
wireshark的过滤为`http.file_data == "password=leonardo"`
```html
POST / HTTP/1.0
Host: docker.hackthebox.eu
User-Agent: Mozilla/5.0 (Hydra)
Content-Length: 17
Content-Type: application/x-www-form-urlencoded
Cookie: 

password=leonardoHTTP/1.1 200 OK
Date: Thu, 12 Mar 2020 06:45:31 GMT
Server: Apache/2.4.18 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 618
Connection: close
Content-Type: text/html; charset=UTF-8

<h1 style='color: #fff;'>HTB{l1k3_4_b0s5_s0n}</h1><script type="text/javascript">
                   window.location = "noooooooope.html"
              </script>
<html>
<head>
    <title>Login - Lernaean</title>
</head>
<body style="background-color: #cd4e7b;">
    <center>
        <br><br><br>
        <h1><u>Administrator Login</u></h1>
        <h2>--- CONFIDENTIAL ---</h2>
        <h2>Please do not try to guess my password!</h2>
        <form method="POST">
            <input type="password" name="password"><br><br>
            <input type="submit" value="Submit">
        </form>
    </center>
</body>
```