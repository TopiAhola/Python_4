



def read_binary_file(filename : str):
    try:
        with open(filename, "rb") as f:
            return f.read()

    except Exception:
        print("File not found")
        return None

def read_file_string(filename: str):
    try:
        with open(filename) as f:
            return f.read()

    except Exception:
        print("File not found")
        return None