from fastapi import Depends,UploadFile
import aiofiles
from exceptions import FileStorageException

from helpers.config import Settings,get_settings

class ChunkProcessor:

    def __init__(
            self, 
            app_setting:Settings = Depends(get_settings)
            ):
        self.chunk_size = app_setting.FILE_DEFAULT_CHUNK_SIZE

    async def process(self,file_path,file:UploadFile):
        try:
            async with aiofiles.open(file_path,"wb") as f:

                while chunk := await file.read(self.chunk_size):
                    await f.write(chunk)
        except OSError:
            raise FileStorageException()
