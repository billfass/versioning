import os
from git import Repo
def create_project_structure(project_root):
    # Création des répertoires principaux
    os.makedirs(project_root, exist_ok=True)
    os.makedirs(os.path.join(project_root, 'data', 'cleaned'), exist_ok=True)
    os.makedirs(os.path.join(project_root, 'data', 'raw'), exist_ok=True)
    os.makedirs(os.path.join(project_root, 'docs'), exist_ok=True)
    os.makedirs(os.path.join(project_root, 'models'), exist_ok=True)
    os.makedirs(os.path.join(project_root, 'notebooks'), exist_ok=True)
    os.makedirs(os.path.join(project_root, 'reports'), exist_ok=True)
    os.makedirs(os.path.join(project_root, 'src'), exist_ok=True)

    # Création des fichiers spécifiques avec du contenu générique
    with open(os.path.join(project_root, 'LICENSE'), 'w') as f:
        f.write("Mettez ici votre licence ou les termes de distribution du projet.")

    with open(os.path.join(project_root, 'Makefile'), 'w') as f:
        f.write("# Mettez ici les commandes make utiles pour votre projet.")

    with open(os.path.join(project_root, 'notebooks', 'main_notebook.ipynb'), 'w') as f:
        f.write("import numpy as np")

    with open(os.path.join(project_root, 'README.md'), 'w') as f:
        f.write("# Titre de votre projet\n\nMettez ici une description générale de votre projet.")

    with open(os.path.join(project_root, 'requirements.txt'), 'w') as f:
        f.write("# Liste des dépendances de votre projet\n\nPackage1==1.0\nPackage2==2.3.1\n")

    # Création du fichier utils.py avec du contenu générique
    utils_code = """def foo_bar():
    # Ajouter le code de votre fonction utilitaire ici
    return "Hello world"
    """
    with open(os.path.join(project_root, 'src', 'utils.py'), 'w') as f:
        f.write(utils_code)

if __name__ == '__main__':
    project_root = '/home/urban/Documents/DITMaster2/versioning'  # Remplacez cela par le chemin souhaité
    create_project_structure(project_root)


    # Chemin vers le dépôt Git existant
    git_repo_path = os.path.join(project_root, ".git")

    # Ouvrir le dépôt Git existant
    repo = Repo(git_repo_path)

    # Ajouter tous les fichiers au commit
    repo.index.add('*')

    # Faire le commit
    commit_message = "Mise à jour du projet"
    repo.index.commit(commit_message)

    # Lier le dépôt local à un dépôt GitHub distant
    remote_url = "https://github.com/billfass/versioning2.git"
    origin = repo.create_remote('origin', remote_url)

    # Pousser le code vers GitHub
    origin.push()






