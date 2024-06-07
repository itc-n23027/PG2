#! python3
# backupTozip.py - ディレクトリ全体を連番付きZIPファイルにコピーする

import zipfile, os

def backup_to_zip(folder):
    #ディレクトリ全体をZIPファイルにバックアップする

    folder = os.path.abspath(folder) # folderを絶対パスにする

    #既存のファイル名からファイル名の連番を決める
    number = 1 
    while True:
        zip_filename = f'{os.path.basename(folder)}_{number}.zip'
        if not os.path.exists(zip_filename):
            break
        number += 1

    # TODO: ZIPファイルを作成する
    print(f'Creaup_zip =ting {zip_filename}')
    backup_zip = zipfile.ZipFile(zip_filename, 'w')
    # TODO:ディレクトリのツリーを渡り歩いてその中のファイルを圧縮する
    print('Done.')
    
backup_to_zip(r'C:\delicious')
