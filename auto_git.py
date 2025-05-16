import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

REPO_PATH = r"C:\Users\marks\OneDrive\Документы\GitHub\MarkSam999.github.io"
BRANCH = "main" 

class GitAutoCommit(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.event_type in ["modified", "created", "deleted"]:
            print(f"File changed: {event.src_path}, commiting...")
            os.system(f'cd /d "{REPO_PATH}" && git add . && git commit -m "Auto commit" && git push origin {BRANCH}')
            time.sleep(5)

if __name__ == "__main__":
    event_handler = GitAutoCommit()
    observer = Observer()
    observer.schedule(event_handler, path=REPO_PATH, recursive=True)
    observer.start()
    
    print("Auto-Git launched! Waiting for changes...")

    try:
        while True:
            time.sleep(30)
    except KeyboardInterrupt:
        print("Авто-Git stopped.")
        observer.stop()
    observer.join()
