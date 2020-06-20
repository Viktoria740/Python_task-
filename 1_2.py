qt_sec = int(input('Введите время в секундах: '))
hours = int(qt_sec / 3600)
hours_fm = int(qt_sec % 3600)
minutes = (hours_fm // 60)
seconds = int(hours_fm % 60)

print('%02d:%02d:%02d' % (hours, minutes, seconds))
