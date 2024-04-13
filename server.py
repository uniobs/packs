import http.server
import socketserver

# Define a porta em que o servidor irá escutar
PORT = 8000

# Define o manipulador de requisições
Handler = http.server.SimpleHTTPRequestHandler

# Cria um servidor
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Servidor rodando na porta:", PORT)
    # Mantém o servidor em execução
    httpd.serve_forever()
