from .BaseController import BaseController
from fastapi import UploadFile
from handlers.file_handler import TypeHandler,SizeHandler

class DataController(BaseController):

    def __init__(self):
        super().__init__()
        self.file_handler= TypeHandler()
        self.file_handler.set_next(SizeHandler())
       

    async def uploadFile(self,file:UploadFile):
        file = await self.file_handler.handle(file)
