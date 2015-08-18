PORT_NUMBER = 2134
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class handler(BaseHTTPRequestHandler):
    path = '/index.html'

    def do_GET(self):
        curdir = "/home/jmeireles/Anime-Tv-shows-Scrapper/server/public/"
        try:
            # Check the file extension required and
            # set the right mime type

            sendReply = False
            if self.path.endswith(".html"):
                mimetype = 'text/html'
                sendReply = True
            if self.path.endswith(".jpg"):
                mimetype = 'image/jpg'
                sendReply = True
            if self.path.endswith(".gif"):
                mimetype = 'image/gif'
                sendReply = True
            if self.path.endswith(".js"):
                mimetype = 'application/javascript'
                sendReply = True
            if self.path.endswith(".css"):
                mimetype = 'text/css'
                sendReply = True

            if sendReply == True:
                # Open the static file requested and send it
                f = open(curdir + self.path)
                self.send_response(200)
                self.send_header('Content-type', mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()

        except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)

        return


try:
    server = HTTPServer(('', PORT_NUMBER), handler)
    server.serve_forever()

except KeyboardInterrupt:
    server.socket.close()