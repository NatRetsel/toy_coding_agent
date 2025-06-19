import os
from google.genai import types

def write_file(working_directory, file_path, content):
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


schema_write_file = types.FunctionDeclaration(
        name="write_file",
        description="Write content specified with content variable into the specified file in the given file path, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The file path to write content to, relative to the working directory. If not provided, lists files in the working directory itself.",
                ),
                "content": types.Schema(
                    type=types.Type.STRING,
                    description="content to be written in the file"
                ),
            },
        ),
    )