import datetime
import shutil


def make_reserve_arc(source, dest):
    cur_time = datetime.datetime.now().time()
    cur_time = f'{cur_time.hour}{cur_time.minute}{cur_time.second}'
    archive_name = f'archive_{cur_time}'
    archive_type = 'zip'
    shutil.make_archive(archive_name, archive_type, root_dir=source)
    shutil.move(archive_name + '.' + archive_type, dest)
