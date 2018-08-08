from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

 #This class will handle any incoming request from
 #the browser 

class myHandler(BaseHTTPRequestHandler):
	#This will handle GET requests
	def do_GET(self):
		self.send_response(200)
		
		# You will need to change this if you are sending something
  		# other than plain text, like JSON or HTML.
		self.send_header('Content-type','text/html')
		self.end_headers()
		print '^C jjjjjjjjjjjj'
		self.wfile.write("Hello World !")

		# Send the "Hello World" message here 
		
		return
