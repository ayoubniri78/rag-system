from fastapi import FastAPI,APIRouter,UploadFile , Depends,status
import os
from helpers.config import get_settings,Settings
from controllers import DataController,ProjectController
from processor.chunks.chunk_processor import ChunkProcessor

data_router = APIRouter(
    prefix="/data",
    tags=["api_v1" , 'data']
)

@data_router.post("/upload/{project_id}",status_code=status.HTTP_201_CREATED)
async def upload_file(
    project_id: str,
    file: UploadFile,
    project_controller : ProjectController = Depends(ProjectController),
    chunks_processor : ChunkProcessor = Depends(ChunkProcessor)
    ):
    is_valid = await DataController().uploadFile(file)
    project_dir_path = project_controller.getProjectPath(project_id=project_id)
    file_path  = os.path.join(
        project_dir_path,
        file.filename
    )
    await chunks_processor.process(file_path=file_path,file=file)
    return {
        "valid":is_valid
    }