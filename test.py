from datetime import datetime
import re

now = datetime.now()
print(now)
time = '2022-03-29T02:54:04.375Z'.split('.')[0].replace('T', ' ').replace('Z', ' ')
print(time)
time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
diff = now - time
print(diff)
times = str(diff).split(':')
print(times)