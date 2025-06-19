from google.genai import types
from .get_files_info import get_files_info
from .get_file_content import get_file_content
from .run_python_file import run_python_file
from .write_file import write_file

available_function_map = {"get_files_info": get_files_info,
                          "get_file_content": get_file_content,
                          "run_python_file": run_python_file,
                          "write_file": write_file}

working_directory = "./calculator"

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    
    # call function
    # if invalid function name; return types.Content explaining the error
    function_name = function_call_part.name
    if function_name not in available_function_map:
        return types.Content(
                    role="tool",
                    parts=[
                        types.Part.from_function_response(
                            name=function_name,
                            response={"error": f"Unknown function: {function_name}"},
                        )
                    ],
                )
    function_args = function_call_part.args
    function_args["working_directory"] = working_directory
    function_result = available_function_map[function_name](**function_args) 
    
    return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_name,
                        response={"result": function_result},
                    )
                ],
            )           