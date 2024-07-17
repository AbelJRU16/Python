import socket

# Crear un socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el socket a la dirección y puerto del servidor
client_socket.connect(('localhost', 12345))

# Enviar datos al servidor
client_socket.sendall(b"Hola desde el cliente")

# Recibir la respuesta del servidor
data = client_socket.recv(1024)
print(f"Datos recibidos: {data.decode()}")

# Cerrar el socket
client_socket.close()
