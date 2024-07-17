import socket

# Crear un socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Asignar el socket a una dirección y un puerto
server_socket.bind(('localhost', 12345))

# Poner el socket en modo de escucha
server_socket.listen(5)
print("Servidor a la escucha en puerto 12345...")

while True:
    # Aceptar nuevas conexiones
    client_socket, client_address = server_socket.accept()
    print(f"Conexión establecida con {client_address}")

    # Recibir datos del cliente
    data = client_socket.recv(1024)
    print(f"Datos recibidos: {data.decode()}")

    # Enviar una respuesta al cliente
    client_socket.sendall(b"Hola desde el servidor")

    # Cerrar la conexión con el cliente
    client_socket.close()
