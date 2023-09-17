import os
import pandas as pd

seletorLinguagens = input('<Linguagem>> ')

match seletorLinguagens:
    case 'python':
        path = input('<Path>> ')
        os.system(f'python {path}')

    case 'nodejs':
        path = input('<Path>> ')
        os.system(f'node {path}')

    case '#python':
        AllTheProjects = pd.read_csv('ProjectsPath.csv')
        name = input('<Nome>> ')
        achou = False
        for i in range(len(AllTheProjects['Nome'])):
            if name == AllTheProjects.loc[i, 'Nome']:
                if AllTheProjects.loc[i, 'Linguagem'] == 'python':
                    path = AllTheProjects.loc[i, 'Path']
                    os.system(f'python {path}')
                    achou = True
                else:
                    print('Esse Item Não Está Em Linguagem Python')
            
        if achou:
            pass
        else:
            print('Item Não Encontrado')

    case '#nodejs':
        AllTheProjects = pd.read_csv('ProjectsPath.csv')
        name = input('<Nome>> ')
        achou = False
        for i in range(len(AllTheProjects['Nome'])):
            if name == AllTheProjects.loc[i, 'Nome']:
                if AllTheProjects.loc[i, 'Linguagem'] == 'nodejs':
                    path = AllTheProjects.loc[i, 'Path']
                    os.system(f'node {path}')
                    achou = True
                else:
                    print('Esse Item Não Está Em Linguagem NodeJs')

        if achou:
            pass
        else:
            print('Item Não Encontrado')

    case 'html':
        path = input('<Path>> ')
        os.system(f'start {path}')

    case '#html':
        AllTheProjects = pd.read_csv('ProjectsPath.csv')
        name = input('<Nome>> ')
        achou = False
        for i in range(len(AllTheProjects['Nome'])):
            if name == AllTheProjects.loc[i, 'Nome']:
                if AllTheProjects.loc[i, 'Linguagem'] == 'html':
                    path = AllTheProjects.loc[i, 'Path']
                    os.system(f'start {path}')
                    achou = True
                else:
                    print('Esse Item Não Está Em Linguagem HTML')

        if achou:
            pass
        else:
            print('Item Não Encontrado')

    case 'Write':
        AllTheProjects = pd.read_csv('ProjectsPath.csv')
        tamanhoAtual = len(AllTheProjects['Nome'])
        newName = input('<Novo Nome>> ')
        newPath = input('<Novo Path>> ')
        newLing = input('<Nova Linguagem>> ')

        AllTheProjects.loc[tamanhoAtual, 'Nome'] = newName
        AllTheProjects.loc[tamanhoAtual, 'Path'] = newPath
        AllTheProjects.loc[tamanhoAtual, 'Linguagem'] = newLing

        AllTheProjects.to_csv('ProjectsPath.csv', index=False)

    case 'ReWrite':
        AllTheProjects = pd.read_csv('ProjectsPath.csv')
        indexAtual = int(input('<Index>> '))
        newName = input('<Novo Nome>> ')
        newPath = input('<Novo Path>> ')
        newLing = input('<Nova Linguagem>> ')

        AllTheProjects.loc[indexAtual, 'Nome'] = newName
        AllTheProjects.loc[indexAtual, 'Path'] = newPath
        AllTheProjects.loc[indexAtual, 'Linguagem'] = newLing

        AllTheProjects.to_csv('ProjectsPath.csv', index=False)