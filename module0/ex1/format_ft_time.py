import time
from datetime import datetime

time = time.time()
answer = f"{time:,.4f} or {time:.2e} in scientific notation"
print("Seconds since January 1, 1970:", answer)

date = datetime.now()
print(date.strftime("%b %d %Y"))
