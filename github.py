#Rose Parker - GitHub Link
import time

my_website = "http://github.com/skulldevops/"

slice = slice(7, -1)

print("...")

print(my_website[slice])

for seconds in range(3, 0, -1):
    print(seconds)
    time.sleep(1)
print("Continue...")