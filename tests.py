import unittest
import os
from functions.run_python_file import run_python_file

class TestGetFileContent(unittest.TestCase):
    def test_valid_current_dir(self):
        response = run_python_file("calculator", "main.py")
        print(response)
         
        
    
    def test_valid_sub_dir(self):
        response = run_python_file("calculator", "tests.py",)
        print(response)
        assert 'Process exited with code' not in response
        
    
    def test_outside_working_dir(self):
        response = run_python_file("calculator", "../main.py")
        print(response)
        assert f'Error: Cannot execute "../main.py" as it is outside the permitted working directory' in response
    
    
    def test_nonexistent_file(self):
        response = run_python_file("calculator", "nonexistent.py")
        print(response)
        assert f'Error: File "nonexistent.py" not found.' in response
    
if __name__ == "__main__":
    unittest.main()