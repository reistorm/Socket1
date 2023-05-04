from time import sleep
import socket
import threading

ya_sock = socket.socket()
addr = ("77.88.55.242", 443)
ya_sock.connect(addr)


#http-запрос
data_out = b"GET / HTTP/1.1\r\nHost:ya.ru\r\n\r\n" #в таком виде на L7 уровне улетает запрос на яндекс-хост
#пошлем эти данные на сокет
ya_sock.send(data_out) 
#перехватим ответ по сколько данных будет перехватывать
# data_in = ya_sock.recv(1024) 
# print(data_in)
# # в терминале 200 - значит успешное соединение
# data_in = ya_sock.recv(1024) 
# print(data_in)
# data_in = ya_sock.recv(1024) 
# print(data_in)
# data_in = ya_sock.recv(1024) 
# print(data_in)
# data_in = ya_sock.recv(1024) 
# print(data_in) #чем больше запросов data_in, тем больше текст страницы

# Но лучше все это завернуть в цикл
data_in = b""
def recieving():
    global data_in
    while True:
    
        data_chunk = ya_sock.recv(1024)
        data_in = data_in + data_chunk
rec_thread = threading.Thread(target=recieving) #функция threading.Thread возвращает поток rec_thread, 
#которая запускает функцию recieving в себе
rec_thread.start()

sleep(4)
print(data_in) #data_in - ответ от веб-сервера
ya_sock.close()

