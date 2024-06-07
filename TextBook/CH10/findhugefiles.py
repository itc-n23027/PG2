import os

def find_large_files(directory, size_threshold):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getsize(file_path) > size_threshold:
                relative_path = os.path.relpath(file_path, directory)
                print(f"Found: {relative_path}, Size: {os.path.getsize(file_path)} bytes")

search_directory = '/path/to/search_directory'
size_threshold_bytes = 100 * 1024 * 1024  

find_large_files(search_directory, size_threshold_bytes)
