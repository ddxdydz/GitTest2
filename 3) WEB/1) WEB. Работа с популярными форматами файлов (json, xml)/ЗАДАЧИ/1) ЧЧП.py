def human_read_format(size):  # size — размер файла в байтах — целое неотрицательное число.
    prf = ['Б', 'КБ', 'МБ', 'ГБ']
    cur_prf = 0
    while size >= 1024:
        size /= 1024
        cur_prf += 1
    return f'{round(size)}{prf[cur_prf]}'
