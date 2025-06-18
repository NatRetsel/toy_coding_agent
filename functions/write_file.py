import os

def write_files(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    file_dir = abs_working_dir
    
    if file_path:
        file_dir = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not file_dir.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
 
    try:
        with open(file_dir, 'w') as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error writing to "{file_path}": {e}'
    