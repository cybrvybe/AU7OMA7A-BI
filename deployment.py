import os

ip = "192.168.1.149"
def launch_application_over_wifi(wifi_ip):
    os.system("python manage.py runserver " + wifi_ip + ":8000")

def master():
    launch_application_over_wifi(ip)

master()