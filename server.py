from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. Send HTTP 200 OK status and headers
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # 2. Send the HTML response back to the browser
        message = "<h1>Adaptive Study System - Week 1 Server Running!</h1>"
        mess2 = "<h5>Hello!<h5>"
        self.wfile.write(message.encode("utf-8"))
        self.wfile.write(mess2.encode("utf-8"))

if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), MyHandler)
    print("Server running! Open http://localhost:8000 in your browser.")
    server.serve_forever()