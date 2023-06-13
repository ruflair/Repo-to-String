import os
import argparse


def list_files(startpath, ignore_set):
    full_str = ''
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        full_str += f'{indent}{os.path.basename(root)}/\n'
        subindent = ' ' * 4 * (level + 1)
        dirs[:] = [d for d in dirs if d not in ignore_set]  # modify dirs in-place
        for f in files:
            if f not in ignore_set:
                full_str += f'{subindent}{f}\n'
    return full_str


def concatenate_files(startpath, outfile, ignore_set):
    with open(outfile, 'w') as out:
        print(os.path.exists(startpath))
        print('Directory structure:')
        print(list_files(startpath, ignore_set))
        out.write(f'Directory structure:\n')
        out.write(f'{list_files(startpath, ignore_set)}\n\n')
        for root, dirs, files in os.walk(startpath):
            dirs[:] = [d for d in dirs if d not in ignore_set]  # modify dirs in-place
            for f in files:
                if f not in ignore_set:
                    rel_path = os.path.relpath(os.path.join(root, f), startpath)
                    out.write(f'START OF {rel_path}\n\n')
                    with open(os.path.join(root, f), 'r') as file:
                        out.write(file.read())
                    out.write(f'\n\nEND OF {rel_path}\n\n')


def load_ignore_list(startpath):
    ignore_file = os.path.join(os.getcwd(), ".rtsignore")
    ignore_set = set()
    if os.path.exists(ignore_file):
        with open(ignore_file, 'r') as file:
            for line in file:
                stripped = line.strip()
                if stripped and not stripped.startswith('#'):  # ignore empty lines and comments
                    ignore_set.add(stripped)
    return ignore_set


def main():
    parser = argparse.ArgumentParser(description="Concatenate files for LLM digesting.")
    parser.add_argument('src_dir', type=str, help="The source directory containing files.")
    parser.add_argument('out_file', type=str, help="The output file for concatenation.")
    args = parser.parse_args()

    ignore_set = load_ignore_list(args.src_dir)

    print('\n\nStarting file concatenation...')
    concatenate_files(args.src_dir, args.out_file, ignore_set)
    print('Concatenation done. Check your output file.')


if __name__ == "__main__":
    main()
