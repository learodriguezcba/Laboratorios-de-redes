import socket
import threading
 
def conexiones(socket_cliente):
    peticion = socket_cliente.recv(1024)
    print "[*] El mensaje ha sido recibido: %s" % peticion
    socket_cliente.send("Este mensaje ha sido enviado por el servidor")
    socket_cliente.close()


ip = "0.0.0.0" 
puerto = 5555 
max_conexiones = 5 
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


servidor.bind((ip, puerto))
servidor.listen(max_conexiones)


print "[*] Esperando conexiones en %s:%d" % (ip, puerto)


while True:
    cliente, direccion = servidor.accept()
    print "[*] La conexion se ha establecido con %s:%d" % (direccion[0] , direccion[1])
    conexiones = threading.Thread(target=conexiones, args=(cliente,))
    conexiones.start()