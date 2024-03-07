import socket
import struct
import time

NTP_SERVER = '153.19.250.123'
NTP_PORT = 123
TIME1970 = 2208988800  # liczba sekund między 1900 a 1970 rokiem

def get_time():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = '\x1b' + 47 * '\0'  # Wysyłamy zapytanie NTP
    client.sendto(data.encode(), (NTP_SERVER, NTP_PORT))
    data, _ = client.recvfrom(1024)
    if data:
        unpacked = struct.unpack("!12I", data)[10] - TIME1970
        return time.ctime(unpacked)  # Konwertujemy czas na format czytelny dla człowieka

if __name__ == "__main__":
    print("Current time is:", get_time())
