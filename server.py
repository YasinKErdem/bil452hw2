
from http.server import   HTTPServer, BaseHTTPRequestHandler
from this import s
HOST = "10.2.41.116"
PORT = 8080
class NeuralHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content Type","text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>Hello World!<h1><body><html>"),"utf-8")
    def GET(number):
        if(number.isnumeric()):
            print("Is numeric")
            if(number.isPrime(number)):
                print("400 Bad Request..")
        else:
            print("400 Bad Request..")

    def isPrime(n):
        for i in range(2,n):
            if (n%i) == 0:
                return False
        return True        

server = HTTPServer((HOST,PORT) , NeuralHTTP)
print("server is running ...")
server.serve_forever()
server.server_close()
print("Server is closed...")
