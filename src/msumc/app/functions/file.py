import os
import uuid
import shutil

def write_file(base_dir, file):
    '''
    Write the file to the system to the directory base_dir

    Args:
        base_dir (str): The base directory to write the file in
        file (webob.compat.cgi_FieldStorage): The file to write to the filesystem

    Returns:
        The filepath of the file written if successful, else False

    '''
    try:
        print(type(file))
        filename, filetype = file.filename.split('.')
        filename = f'{uuid.uuid4()}.{filetype}'
        fp = os.path.join(base_dir, filename)
        temp_fp = os.path.join(base_dir, f'~{filename}')

        file.file.seek(0)
        with open(temp_fp, 'wb') as output_file:
            shutil.copyfileobj(file.file, output_file)
        os.rename(temp_fp, fp)

        return fp
    except Exception as e:
        return False

def remove_file(filepath):
    '''
    Remove the file from the system

    Args:
        filepath (str): The path to the file

    Returns:
        True if successful, else False
    '''
    try:
        if not os.path.isfile(filepath):
            raise ValueError('File does not exist')

        os.remove(filepath)

        return True
    except Exception as e:
        return False
