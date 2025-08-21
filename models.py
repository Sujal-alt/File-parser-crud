from sqlalchemy import Column, String, Text, DateTime
from datetime import datetime
from database import Base

class FileUpload(Base):
    __tablename__ = "files"

    id = Column(String, primary_key=True, index=True)
    filename = Column(String)
    filepath = Column(String)
    status = Column(String, default="uploading")
    parsed_content = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
