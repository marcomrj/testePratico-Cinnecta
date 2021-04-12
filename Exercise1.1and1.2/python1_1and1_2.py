import os

# 1.1 function
def list_file_n_owners(path):
    file_owners = []
    files = os.listdir(path)
    for fl in files:
            file_owners.append(os.stat(path+'/'+fl).st_uid)
    return files, file_owners

# 1.2 function
def group_owners(files,owners):
    dictio = {}
    for fl,owner in zip(files,owners):
        dictio[fl] = owner
    return dictio


files, owners = list_file_n_owners('./ExtrasCinnecta')
print(owners)
print(group_owners(files,owners))