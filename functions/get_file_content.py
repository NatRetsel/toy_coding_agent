import os

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    file_dir = abs_working_dir
    
    if file_path:
        file_dir = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not file_dir.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
 
    if not os.path.isfile(file_dir):
        return f'Error: "{file_path}" is not a file'
    
    MAX_CHARS = 10000
    file_contents_str = ""
    try:
        with open(file_dir, "r") as f:
            file_contents_str = f.read(MAX_CHARS)
        if os.path.getsize(file_dir) > MAX_CHARS:
            file_contents_str += f'[...File "{file_path}" truncated at 10000 characters]'
        return file_contents_str
    except Exception as e:
        return f"Error reading file contents: {e}"