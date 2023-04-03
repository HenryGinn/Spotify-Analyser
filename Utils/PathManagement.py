import os

def make_folder(path, message=False):
    if not os.path.exists(path):
        output_make_folder_message(path, message)
        os.mkdir(path)

def output_make_folder_message(path, message):
    if message:
        base_name = os.path.basename(path)
        print(f"Making '{base_name}' folder at {path}")
