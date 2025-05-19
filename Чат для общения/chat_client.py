# chat_client.py

import socket
import threading
import sys

def receive_messages(sock):
    """
    Поток для чтения данных от сервера и вывода в консоль.
    """
    try:
        while True:
            data = sock.recv(1024)
            if not data:
                print("[i] Соединение закрыто сервером.")
                break
            sys.stdout.write(data.decode())
            sys.stdout.flush()
    except Exception as e:
        print(f"[!] Ошибка при приёме данных: {e}")
    finally:
        sock.close()

def start_client(server_host, server_port, nickname):
    """
    Подключается к серверу и запускает поток приёма.
    Основной поток читает stdin и шлёт серверу.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((server_host, server_port))
    except Exception as e:
        print(f"[!] Не удалось подключиться к {server_host}:{server_port}: {e}")
        return

    print(f"[i] Подключено к {server_host}:{server_port}. Введите сообщения и ENTER.")

    # Опционально отправляем строку «никнейм подключился»
    try:
        sock.sendall(f"{nickname} подключился.\n".encode())
    except:
        pass

    # Запускаем поток, который слушает сервер и печатает входящие сообщения
    recv_thread = threading.Thread(
        target=receive_messages, args=(sock,), daemon=True
    )
    recv_thread.start()

    # Основной поток: читаем пользовательский ввод
    try:
        for line in sys.stdin:
            if not line:
                break
            message = f"[{nickname}] {line}"
            sock.sendall(message.encode())
    except KeyboardInterrupt:
        print("\n[i] Отключение по Ctrl+C.")
    finally:
        try:
            sock.close()
        except:
            pass

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Использование: python3 chat_client.py <хост> <порт> <никнейм>")
        sys.exit(1)
    host = sys.argv[1]
    port = int(sys.argv[2])
    nick = sys.argv[3]
    start_client(host, port, nick)