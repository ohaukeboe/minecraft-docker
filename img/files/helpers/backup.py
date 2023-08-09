#! /usr/bin/python3.9

import os
import shutil as sh
from datetime import date

base_path='/app/config/backup/'
backup_categories=['world/', 'mods/']

def verbose_print(string):
    verbose = os.environ.get("VERBOSE")
    if verbose:
        print(string, flush=True)

for category in backup_categories:
    verbose_print('Starting backup')
    base_name=base_path + category + str(date.today())

    sh.make_archive(base_name, 'gztar', '/app/minecraft/', category)

    backups = os.listdir(base_path + category)
    backups = [base_path+category+file for file in backups]
    verbose_print(backups)

    while len(backups) > int(os.environ.get('BACKUP_LENGTH')):
        oldest = min(backups, key=os.path.getctime)
        os.remove(oldest)
        backups.remove(oldest)
    verbose_print('Backup complete')