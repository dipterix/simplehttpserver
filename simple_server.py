import http.server
import socket
import webbrowser

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind(('', 0))
host, port = tcp.getsockname()
tcp.close()

host = "127.0.0.1"

url = "http://%s:%d" % ( host, port )
print("Starting a simple web server at \n\t%s" % url)

Handler = http.server.SimpleHTTPRequestHandler
serv = http.server.HTTPServer(("", port), Handler)
webbrowser.open_new(url)
serv.serve_forever()

