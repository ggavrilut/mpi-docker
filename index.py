import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()


# docker build . -t python-docker-2
# docker run -it -p 8080:8080 python-docker-2

# identic

#docker-compose up -d