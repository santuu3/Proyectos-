
import socket

def escanear_puertos(ip):
    """Escanea los puertos de una dirección IP dada."""
    for puerto in range(1, 65536):  # El rango debe ser hasta 65536
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Corrección de constantes
        sock.settimeout(1)  # Tiempo de espera más corto para mejorar la velocidad

        # Intentar conectar al puerto
        resultado = sock.connect_ex((ip, puerto))  # Usar connect_ex para obtener el código de error

        if resultado == 0:
            print(f"Puerto Abierto: {puerto}")
        else:
            print(f"Puerto Cerrado: {puerto}")

        sock.close()  # Cerrar el socket después de cada intento

if __name__ == "__main__":
    ip = input("Ingrese la dirección IP a escanear: ")
    escanear_puertos(ip)
    