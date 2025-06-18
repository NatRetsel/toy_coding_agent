import os
import subprocess

def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    file_dir = abs_working_dir
    
    if file_path:
        file_dir = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not file_dir.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(file_dir):
        return f'Error: File "{file_path}" not found.'
    
    # print(os.path.splitext(file_dir))
    # print(os.path.splitext(file_dir)[1], ".py",  not os.path.splitext(file_dir)[1] == ".py")
    
    if os.path.splitext(file_dir)[1] != ".py":
        print("here")
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        output_list = []
        commands = ["python", file_dir]
        output = subprocess.run(commands, timeout=30, capture_output=True,
                    cwd=abs_working_dir, text=True)
        
        if output.stdout:
            output_list.append(f'STDOUT: {output.stdout}')
        if output.stderr:
            output_list.append(f'STDERR: {output.stderr}')
        
        if output.returncode != 0:
            output_list.append(f'Process exited with code {output.returncode}')
        
        return "\n".join(output_list) if output_list else "No output produced"
        
    except Exception as e:
        return f"Error: executing Python file: {e}"
