import os
import configparser
import nmap
import requests
import socket

def scan_ports(target, ports):                                                         
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
	# Сканирование веб-сайтов на наличие открытых портов
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

if __name__ == "__main__":
    target_host = input("Введите IP-адрес для сканирования: ")
    target_ports = range(1, 1025)  # Сканируем порты с 1 по 1024

    open_ports = scan_ports(target_host, target_ports)

    if open_ports:
        print("Открытые порты на целевом хосте:")
        for port in open_ports:
            print(f"Порт {port} открыт")
    else:
        print("На целевом хосте нет открытых портов.")


def get_service_name(port):                                             
    try:
        # Получаем информацию о службе для данного порта
        service_name = socket.getservbyport(port)
        return service_name
    except OSError:
        # Если служба не найдена, возвращаем "Unknown"
        return "Unknown"

if __name__ == "__main__":
    target_host = input("Введите IP-адрес для сканирования: ")
    target_ports = range(1, 1025)  # Сканируем порты с 1 по 1024

    open_ports = scan_ports(target_host, target_ports)

    if open_ports:
        print("Открытые порты на целевом хосте:")
        for port in open_ports:
            service_name = get_service_name(port)
            print(f"Порт {port} открыт, служба: {service_name}")
    else:
        print("На целевом хосте нет открытых портов.")


def vulnerability_scan(target, port):
    # Код для сканирования уязвимостей на заданном порту
    
    if is_vulnerable:
        return f"Порт {port} уязвим"
    else:
        return f"Порт {port} не уязвим"

def analyze_response(target, port):
    try:
        # Устанавливаем соединение с портом
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((target, port))

        if result == 0:
            # Получаем ответ от порта
            response = sock.recv(1024)  # Пример чтения 1024 байт ответа
            # Далее можно провести анализ ответа, например, искать конкретные строки, характерные для определенной службы

            # Возвращаем анализ
            return f"Ответ на порту {port}: {response.decode('utf-8')}"

    except Exception as e:
        return f"Ошибка при анализе порта {port}: {str(e)}"
    finally:
        sock.close()

    return f"Порт {port} закрыт или не отвечает"


# Сканирование на основе словаря (Fuzzer)
def fuzz(target_url, payloads):
    for payload in payloads:
        url = target_url + payload
        response = requests.get(url)
        if "Error" in response.text:
            print(f"Уязвимость обнаружена: {url}")


def check_for_outdated_components():
    # Проверяем зависимости приложения (например, Python-пакеты) на наличие обновлений
    os.system("pip list --outdated")


# Анализируем конфигурационные параметры на наличие уязвимостей
def analyze_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    

# Сканирование конфигурации
def scan_open_ports(target_ip):
    scanner = nmap.PortScanner()
    scanner.scan(target_ip, arguments='-p 1-1024')
    open_ports = scanner[target_ip]['tcp'].keys()
    return open_ports

# Другие проверки на уязвимости в API
def scan_api_vulnerabilities(api_endpoint):
    # Попытка отправки запросов с недостаточными правами доступа и анализ ответов
    response = requests.get(api_endpoint)
    if response.status_code == 401:
        print("Незащищенное API: требуется аутентификация")
    

# Сканирование на наличие открытых доступных служб
def scan_services(target_host, target_ports):
    open_services = []
    for port in target_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_host, port))
        if result == 0:
            open_services.append(port)
        sock.close()
    return open_services