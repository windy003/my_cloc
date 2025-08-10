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
    for root, dirs, files in os.walk('.'):
        # 排除以.开头的文件夹
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            # 排除以.开头的文件
            if file.startswith('.'):
                continue
            file_path = os.path.join(root, file)
            if not is_binary(file_path):
                total_lines += count_lines_in_file(file_path)
    
    print(f"Total lines of code in current directory (excluding binary files,files  and folders start with .): {total_lines}")

if __name__ == "__main__":
    main()