import cv2
from onvif import ONVIFCamera
from rtsp_link_patterns import get_link


def get_links_by_producer(address, username, password, path_to_wsdl):
    if len(address) > 1:
        mycam = ONVIFCamera(address[0], 80, username, password, path_to_wsdl) # запрос к камере для определение производителя
        camera_name = mycam.devicemgmt.GetHostname().Name
        return get_link(camera_name, username, password, address[0], address[1])
    else:
        mycam = ONVIFCamera(IP, 80, username, password, path_to_wsdl)
        camera_name = mycam.devicemgmt.GetHostname().Name
        list_possible_addresses = []
        list_possible_addresses.append(get_link(camera_name, username, password, IP, 554)) # самые распространенные порты, дефолтные порты типа 7070 оставлены в файле ссылок
        list_possible_addresses.append(get_link(camera_name, username, password, IP, 558))
        return list_possible_addresses


def get_stream(link):
    cap = cv2.VideoCapture(link)
    cv2.namedWindow('video', cv2.WINDOW_NORMAL)
    while cap.isOpened(): # программа выполняется, пока работает соединение
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('video', frame)

            if cv2.waitKey(1) & 0xFF == 27: # трансляция прерывается с клавиатуры
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    IP = input('Введите IP адрес: ')
    username = input('Введите имя пользователя: ')
    password = input('Введите пароль: ')
    path_to_wsdl = 'venv\Lib\site-packages\wsdl'

    address_list = IP.split(':')     # для проверки введенного IP-адреса: с портом или без
    rtsp_links = get_links_by_producer(address_list, username, password, path_to_wsdl)

    if isinstance(rtsp_links, list):
        for link in rtsp_links:
            get_stream(link)
    else:
        get_stream(rtsp_links)
