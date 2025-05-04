import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

REPO_PATH = r"C:\Users\marks\OneDrive\Документы\GitHub\MarkSam999.github.io"
BRANCH = "main" 

class GitAutoCommit(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.event_type in ["modified", "created", "deleted"]:
            print(f"Файл изменён: {event.src_path}, выполняю коммит...")
            os.system(f'cd /d "{REPO_PATH}" && git add . && git commit -m "Auto commit" && git push origin {BRANCH}')

if __name__ == "__main__":
    event_handler = GitAutoCommit()
    observer = Observer()
    observer.schedule(event_handler, path=REPO_PATH, recursive=True)
    observer.start()
    
    print("Авто-Git запущен! Ожидаю изменений...")
    time.sleep(5)

    try:
        while True:
            time.sleep(30)
    except KeyboardInterrupt:
        print("Авто-Git остановлен.")
        observer.stop()
    observer.join()
