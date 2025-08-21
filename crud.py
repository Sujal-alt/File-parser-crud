from models import FileUpload

def save_file_db(db, file_id, filename, filepath):
    file_entry = FileUpload(id=file_id, filename=filename, filepath=filepath, status="uploading")
    db.add(file_entry)
    db.commit()
    db.refresh(file_entry)
    return file_entry

def get_file_db(db, file_id):
    return db.query(FileUpload).filter(FileUpload.id == file_id).first()

def list_files_db(db):
    return db.query(FileUpload).all()

def delete_file_db(db, file_id):
    file = db.query(FileUpload).filter(FileUpload.id == file_id).first()
    if file:
        db.delete(file)
        db.commit()
        return {"message": "File deleted"}
    return {"message": "File not found"}
