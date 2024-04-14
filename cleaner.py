import os

for i in os.listdir("test"):
    if i.endswith(".jpg"):
        os.remove("test/" + i)

for i in os.listdir("matrix"):
    if i.endswith(".pkl"):
        os.remove("matrix/" + i)
