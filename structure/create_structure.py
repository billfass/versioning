import os
from pathlib import Path
import shutil

class Structure:
    def __init__(self, project_root):
        self.project_root = project_root

    def method_1(self):
        os.makedirs(self.project_root, exist_ok=True)
        os.makedirs(os.path.join(self.project_root, 'data', 'cleaned'), exist_ok=True)
        os.makedirs(os.path.join(self.project_root, 'data', 'raw'), exist_ok=True)
        os.makedirs(os.path.join(self.project_root, 'docs'), exist_ok=True)
        os.makedirs(os.path.join(self.project_root, 'models'), exist_ok=True)
        os.makedirs(os.path.join(self.project_root, 'notebooks'), exist_ok=True)
        os.makedirs(os.path.join(self.project_root, 'reports'), exist_ok=True)
        os.makedirs(os.path.join(self.project_root, 'src'), exist_ok=True)

        self.edit_files()

    def method_2(self):
        Path(self.project_root+"/data/cleaned").mkdir(parents=True, exist_ok=True)
        Path(self.project_root+"/data/raw").mkdir(parents=True, exist_ok=True)
        Path(self.project_root+"/docs").mkdir(parents=True, exist_ok=True)
        Path(self.project_root+"/models").mkdir(parents=True, exist_ok=True)
        Path(self.project_root+"/notebooks").mkdir(parents=True, exist_ok=True)
        Path(self.project_root+"/reports").mkdir(parents=True, exist_ok=True)
        Path(self.project_root+"/src").mkdir(parents=True, exist_ok=True)

        self.edit_files()

    def method_3(self):
        directories = [
        self.project_root+"/data/cleaned",
        self.project_root+"/data/raw",
        self.project_root+"/docs",
        self.project_root+"/models",
        self.project_root+"/notebooks",
        self.project_root+"/reports",
        self.project_root+"/src",
        ]

        for directory in directories:
            shutil.os.makedirs(directory, exist_ok=True)
        self.edit_files()
    
    def edit_files(self):
        # Création des fichiers spécifiques avec du contenu générique
        with open(os.path.join(self.project_root, 'data/cleaned', 'data.txt'), 'w') as f:
            f.write("hello world")

        with open(os.path.join(self.project_root, 'data/raw', 'data.txt'), 'w') as f:
            f.write("hello world")

        with open(os.path.join(self.project_root, 'docs', 'docs.txt'), 'w') as f:
            f.write("hello world")

        with open(os.path.join(self.project_root, 'models', 'mymodel.ipynb'), 'w') as f:
            f.write("import numpy as np")

        with open(os.path.join(self.project_root, 'reports', 'report.log'), 'w') as f:
            f.write("hello world")

        with open(os.path.join(self.project_root, 'LICENSE'), 'w') as f:
            f.write("Mettez ici votre licence ou les termes de distribution du projet.")

        with open(os.path.join(self.project_root, 'Makefile'), 'w') as f:
            f.write("# Mettez ici les commandes make utiles pour votre projet.")

        with open(os.path.join(self.project_root, 'notebooks', 'main_notebook.ipynb'), 'w') as f:
            f.write("import numpy as np")

        with open(os.path.join(self.project_root, 'README.md'), 'w') as f:
            f.write("# Titre de votre projet\n\nMettez ici une description générale de votre projet.")

        with open(os.path.join(self.project_root, 'requirements.txt'), 'w') as f:
            f.write("# Liste des dépendances de votre projet\n\nPackage1==1.0\nPackage2==2.3.1\n")

        # Création du fichier utils.py avec du contenu générique
        utils_code = """def foo_bar():
        # Ajouter le code de votre fonction utilitaire ici
        return "Hello world"
        """
        with open(os.path.join(self.project_root, 'src', 'utils.py'), 'w') as f:
            f.write(utils_code)
