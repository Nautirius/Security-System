import os
from django.conf import settings
from pathlib import Path

class FileStorage:
    def __init__(self, base_dir=None):
        self.base_dir = base_dir or settings.MEDIA_ROOT

    def save_file(self, file, relative_path):
        full_path = Path(self.base_dir) / relative_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        with open(full_path, 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)
        return str(full_path)

    def delete_file(self, relative_path):
        full_path = Path(self.base_dir) / relative_path
        if full_path.exists():
            full_path.unlink()

    def get_file_path(self, relative_path):
        return Path(self.base_dir) / relative_path
