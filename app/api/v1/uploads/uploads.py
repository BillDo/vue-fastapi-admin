from datetime import datetime
import uuid
from pathlib import Path

from fastapi import APIRouter, File, UploadFile

from app.schemas import Success


router = APIRouter()


@router.post("/upload", summary="Upload a file and return its public URL")
async def upload_file(file: UploadFile = File(...)):
    uploads_dir = Path("static") / "uploads"
    uploads_dir.mkdir(parents=True, exist_ok=True)

    ext = Path(file.filename).suffix or ""
    filename = f"{datetime.utcnow().strftime('%Y%m%d%H%M%S')}_{uuid.uuid4().hex}{ext}"
    dest_path = uploads_dir / filename

    content = await file.read()
    dest_path.write_bytes(content)

    url = f"/static/uploads/{filename}"
    return Success(data={"url": url, "filename": filename})


