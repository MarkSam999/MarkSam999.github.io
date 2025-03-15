import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

REPO_PATH = "C:/Users/marks/OneDrive/Документы/GitHub/MarkSam999.github.io"
BRANCH = "main"  # Укажи свою ветку

class GitAutoCommit(FileSystemEventHandler):
    def on_any_event(self, event):
        os.system(f'cd "{REPO_PATH}" && git add . && git commit -m "Auto commit" && git push origin {BRANCH}')

if __name__ == "__main__":
    event_handler = GitAutoCommit()
    observer = Observer()
    observer.schedule(event_handler, path=REPO_PATH, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
