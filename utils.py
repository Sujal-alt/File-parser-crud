import time, json
from database import SessionLocal
from models import FileUpload

progress_tracker = {}

def simulate_processing(file_id, filepath):
    db = SessionLocal()
    for p in range(0, 101, 20):
        progress_tracker[file_id] = {"status": "processing", "progress": p}
        time.sleep(1)  # simulate work

    # Pretend parsing CSV/JSON
    parsed_data = json.dumps({"message": "File parsed successfully!"})

    file = db.query(FileUpload).filter(FileUpload.id == file_id).first()
    file.status = "ready"
    file.parsed_content = parsed_data
    db.commit()

    progress_tracker[file_id] = {"status": "ready", "progress": 100}
