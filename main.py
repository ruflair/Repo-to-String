import os
import argparse


def list_files(startpath):
    full_str = ''
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f'{indent}{os.path.basename(root)}/')
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            full_str += f'{subindent}{f}\n'
    return full_str


def concatenate_files(startpath, outfile):
    with open(outfile, 'w') as out:
        print(os.path.exists(startpath))
        print('Directory structure:')
        print(list_files(startpath))
        out.write(f'Directory structure:\n')
        out.write(f'{list_files(startpath)}\n\n')
        for root, dirs, files in os.walk(startpath):
            for f in files:
                rel_path = os.path.relpath(os.path.join(root, f), startpath)
                out.write(f'START OF {rel_path}\n\n')
                with open(os.path.join(root, f), 'r') as file:
                    out.write(file.read())
                out.write(f'\n\nEND OF {rel_path}\n\n')


def main():
    parser = argparse.ArgumentParser(description="Concatenate files for LLM digesting.")
    parser.add_argument('src_dir', type=str, help="The source directory containing files.")
    parser.add_argument('out_file', type=str, help="The output file for concatenation.")
    args = parser.parse_args()

    print('\n\nStarting file concatenation...')
    concatenate_files(args.src_dir, args.out_file)
    print('Concatenation done. Check your output file.')


if __name__ == "__main__":
    main()
