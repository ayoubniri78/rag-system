from fastapi import  FastAPI,APIRouter,UploadFile , Depends,status 
import os
from helpers.config import get_settings,Settings
from controllers import DataController,ProjectController
from processor.chunks.chunk_processor import ChunkProcessor
from handlers.file_name_handler import FileProcessor
from .schemas.data import ProcessRequest
from controllers import ProcessController
import logging


logger = logging.getLogger('univcorn.error')
data_router = APIRouter(
    prefix="/data",
    tags=["api_v1" , 'data']
)

@data_router.post(
    "/upload/{project_id}",
    status_code=status.HTTP_201_CREATED
)
async def upload_file(
    project_id: str,
    file: UploadFile,
    project_controller: ProjectController = Depends(ProjectController),
    chunks_processor: ChunkProcessor = Depends(ChunkProcessor)
):
    await DataController().uploadFile(file)

    processor = FileProcessor(project_controller)

    result = processor.process(
        orig_file_name=file.filename,
        project_id=project_id
    )

    file_id = result["file_id"]
    file_path = result["file_path"]

    await chunks_processor.process(
        file_path=file_path,
        file=file
    )

    return {
        "file_path": file_path,
        "file_id": file_id
    }


@data_router.post(
    "/process/{project_id}",
    )
async def process_endpoint(project_id:str,process_request:ProcessRequest):
    file_id = process_request.file_id
    chunk_size=process_request.chunk_size
    overlap_size=process_request.overlap_size

    process_controller=ProcessController(project_id=project_id)
    file_content = process_controller.get_file_content(file_id=file_id)
    file_chunks=process_controller.process_file_content(
        file_content=file_content,
        file_id=file_id,
        overlap_size=overlap_size,
        chunk_size=chunk_size
    )

    if file_chunks is None or len(file_chunks)==0:
        return {
                "error": 'enable to process file'
            }
    return file_chunks