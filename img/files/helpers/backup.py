#! /usr/bin/python3.9

import os
import shutil as sh
from datetime import date

base_path='/app/config/backup/'
backup_categories=['world/', 'mods/']

for category in backup_categories:
    base_name=base_path + category + str(date.today())

    sh.make_archive(base_name, 'gztar', '/app/minecraft/', category)

    backups = os.listdir(base_path + category)

    while len(backups) > int(os.environ.get('BACKUP_LENGTH')):
        oldest = min(backups, key=os.path.getctime)
        os.remove(base_path + category + oldest)