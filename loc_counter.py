import os

def is_binary(file_path):
    """Check if a file is binary by looking for null bytes."""
    try:
        with open(file_path, 'rb') as f:
            chunk = f.read(1024)  # Read the first 1KB
            return b'\0' in chunk
    except Exception as e:
        print(f"Could not check file {file_path}: {e}")
        return True # Assume binary on error

def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            return len(f.readlines())
    except Exception as e:
        print(f"Could not read file {file_path}: {e}")
        return 0

def main():
    total_lines = 0
    for root, _, files in os.walk('.'):
        for file in files:
            file_path = os.path.join(root, file)
            if not is_binary(file_path):
                total_lines += count_lines_in_file(file_path)
    
    print(f"Total lines of code in current directory (excluding binary files): {total_lines}")

if __name__ == "__main__":
    main()