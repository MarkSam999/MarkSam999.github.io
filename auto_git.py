import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Путь к репозиторию (убедись, что он правильный)
REPO_PATH = r"C:\Users\marks\OneDrive\Документы\GitHub\MarkSam999.github.io"
BRANCH = "main"  # Укажи нужную ветку (может быть "master" или другая)

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

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        print("Авто-Git остановлен.")
        observer.stop()
    observer.join()
