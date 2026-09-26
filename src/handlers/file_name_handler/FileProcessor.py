import os
import re
import uuid

from controllers import ProjectController


class FileProcessor:

    _pattern = r"[^a-zA-Z0-9._-]"

    def __init__(self, project_controller: ProjectController):
        self.project_controller = project_controller

    def process(self, orig_file_name: str, project_id: str):

        # 1. Nettoyer le nom
        clean_name = re.sub(
            self._pattern,
            "_",
            orig_file_name.lower()
        )

        # 2. Générer une clé
        random_key = uuid.uuid4().hex

        # 3. Générer le file_id
        file_id = f"{random_key}_{clean_name}"

        # 4. Récupérer le dossier du projet
        project_path = self.project_controller.getProjectPath(project_id)

        # 5. Construire le chemin physique
        file_path = os.path.join(
            project_path,
            file_id
        )

        return {
            "file_id": file_id,
            "file_path": file_path
        }