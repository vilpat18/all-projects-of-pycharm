import psutil

battery = psutil.sensors_battery()
percent = str(battery.percent)

print('now ur battery charging left: ',percent)