from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print("Создался файл:", event.src_path)
        
    def on_modified(self, event):
        print("Модифицированный файл:", event.src_path)
        grad = "aeiouаоуеиэюя"
        file = open(event.src_path)
        for k in file.read():
            if k in grad: print(str(k).lower())
            else: print(str(k).upper())



event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path=r"G:\files", recursive=False)
observer.start()
while True:
    try:
        pass
    except KeyboardInterrupt:
        observer.stop()
