from structure import create_structure 
from mygit import gitiniate


if __name__ == '__main__':

    project_root_1 = '/home/urban/Documents/DITMaster2/structure_1' 
    project_root_2 = '/home/urban/Documents/DITMaster2/structure_2'
    project_root_3 = '/home/urban/Documents/DITMaster2/structure_3'

    folders_1 = create_structure.Structure(project_root_1)
    folders_2 = create_structure.Structure(project_root_2)
    folders_3 = create_structure.Structure(project_root_3)

    folders_1.method_1()
    folders_2.method_2()
    folders_3.method_3()

    strucutres = ['structure_1','structure_2', 'structure_3']

    myDict = {
        'structure_1': project_root_1,
        'structure_2': project_root_2,
        'structure_3': project_root_3
    }

    for repository, url in myDict.items():
        repo_path = url
        repo_url = 'https://github.com/billfass/versioning.git'
        branch_name = repository
        commit_message = f'commit pour le projet de la branche {branch_name}'
        username = 'billfass'
        token = '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'

        myGit = gitiniate.Gitinit(repo_path, repo_url, commit_message, branch_name, username, token)
        myGit.compute()
    

    
