# Import library datetime
from datetime import *

# Function untuk menghitung perbedaan tanggal
def diffDate(x):
    now = datetime.strptime(datetime.now().strftime(date_format), date_format)
    diffDate = now - (datetime.strptime(x, date_format))
    return (abs(diffDate).days)

# Format tanggal
date_format = "%Y-%m-%d"

# String untuk menentukan perebedaan tanggal
x = "2018-12-30"

print(diffDate(x))
