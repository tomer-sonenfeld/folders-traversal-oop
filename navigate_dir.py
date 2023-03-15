import os
import dir

def find_word(root_dir: str, word: str):
    matched_file_paths = []
    for path in os.listdir(root_dir):
        abs_path = os.path.join(root_dir,path)
        if os.path.isdir(abs_path):
            matched_file_paths += find_word(abs_path, word)

        elif os.path.isfile(abs_path):
            try:
                with open(abs_path, "r") as file:
                    if word in file.read():
                        matched_file_paths.append(abs_path)
            except UnicodeDecodeError:
                continue

    return matched_file_paths


if __name__ == "__main__":
    print("cwd: " + os.getcwd())
    print(find_word(os.getcwd(), "hello"))

    d = dir.Dir(os.getcwd())
    print(d.test_file.hello)
