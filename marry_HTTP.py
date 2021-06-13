import sys
import time
import socketserver as socketserver
import http.server
from http.server import SimpleHTTPRequestHandler as RequestHandler
from urllib.parse import urlparse, unquote
import subprocess


class MyHandler(RequestHandler):

    #表頭處理
    def MyHeader(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()


    #收到HTTP GET 指令 要做的事(送出網址的時候)。
    def do_GET(self):

        #儲存資料的變數，命名自由、開心就好。
        html = '婚姻狀況'


        #接收HTTP GET 傳送的資料
        print(self.path)                    #/?year=1999
        #整理字串
        query = urlparse(self.path).query   #  year=1999

        #有收到資料的話。
        if query != "":

            #用dictionary的方式拆解
            dict2 = dict(qc.split("=") for qc in query.split("&"))


            try:
                year = dict2["year"] #取值
                print(year)

                html = subprocess.check_output(['python','marry.py',year])
                print(html)
                #執行表頭處理。
                self.MyHeader()
                # 回傳給網頁。
                self.wfile.write(html)
                return


            except:
                html = html + "沒有資料"

        super().do_GET()

#-------------------------------------------------------------------------------------
port = 8888
print('Server listening on port %s' % port)
socketserver.TCPServer.allow_reuse_address = True
httpd = socketserver.TCPServer(('0.0.0.0', port), MyHandler)
try:
    httpd.serve_forever()
except:
    print("Closing the server.")
    httpd.server_close()
    raise

