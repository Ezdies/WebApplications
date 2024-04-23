import telnetlib

# Dane serwera SMTP
smtp_server = 'smtp.freesmtpservers.com'
smtp_port = 25  # Port dla TLS (STARTTLS)

# Dane maila
sender_email = 'siema@siema.pl'
receiver_email = 'siema@siema.pl'
subject = 'Testowy e-mail'
body = 'To jest treść testowego e-maila.'


def send_email():
    with telnetlib.Telnet(smtp_server, smtp_port) as tn:
        print(tn.read_until(b'220').decode())
        tn.write(b'EHLO max\r\n')
        print(tn.read_until(b'250').decode())
        tn.write(f'MAIL FROM:{sender_email}\r\n'.encode())
        print(tn.read_until(b'250').decode())
        tn.write(f'RCPT TO:{receiver_email}\r\n'.encode())
        print(tn.read_until(b'250').decode())
        tn.write(b'DATA\r\n')
        print(tn.read_until(b'354').decode())

        # Wysyłanie treści wiadomości linia po linii
        tn.write(f'From: {sender_email}\r\n'.encode())
        tn.write(f'To: {receiver_email}\r\n'.encode())
        tn.write(f'Subject: {subject}\r\n'.encode())
        tn.write(b'\r\n')  # Pusta linia oddzielająca nagłówki od treści
        tn.write(f'{body}\r\n'.encode())  # Treść wiadomości
        tn.write(b'.\r\n')  # Zakończenie wiadomości kropką
        print(tn.read_until(b'250').decode())  # Odpowiedź serwera

        tn.write(b'QUIT\r\n')
        print(tn.read_until(b'Connection closed').decode())

if __name__ == "__main__":
    send_email()

# to jest to co w cmd jest napisane
# ➜  Lab6 git:(main) ✗ telnet smtp.freesmtpservers.com 25
# Trying 104.237.130.88...
# Connected to smtp.freesmtpservers.com.
# Escape character is '^]'.
# 220 tools.wpoven.com Python SMTP 1.4.2
# MAIL FROM:siema@siema.pl
# 503 Error: send HELO first
# EHLO max
# 250-tools.wpoven.com
# 250-SIZE 33554432
# 250-8BITMIME
# 250-SMTPUTF8
# 250 HELP
# MAIL FROM:siema@siema.pl
# 250 OK
# RCPT TO:siema@siema.pl
# 250 OK
# DATA
# 354 End data with <CR><LF>.<CR><LF>
# From: siema@siema.pl
# To: siema@siema.pl
# Subject: Testowy e-mail

# To jest treść testowego e-maila.
# .
# 250 OK
# QUIT
# Connection closed by foreign host.