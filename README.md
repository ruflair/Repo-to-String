# Repo to String (RTS)

Repo to String (RTS) is a Python utility for concatenating text files in a directory tree into a single output file. The script recursively explores all directories and subdirectories from a given root directory and concatenates the content of each text file it finds, creating a section in the output file for each source file. The script can also exclude specific files and directories based on a `.rtsignore` file.

## Usage

The script is invoked from the command line and takes two positional arguments:

```
python rts.py <src_dir> <out_file>
```

- `src_dir` is the source directory from which to start the recursion. The script will look for a `.rtsignore` file in this directory.
- `out_file` is the destination file where the script will write the combined output.

For example:

```
python rts.py ./my_repo stringified_repo.txt
```

This will concatenate all the text files found in `./my_repo` and its subdirectories into `stringified_repo.txt`.

## Ignore List

If there is a `.rtsignore` file in the source directory, the script will use it to determine which files and directories to ignore. This file should contain one filename or directory name per line. The script will ignore any files or directories (at any depth) whose names match an entry in the `.rtsignore` file.

Lines in the `.rtsignore` file that start with a `#` are considered comments and are ignored.

Here's an example `.rtsignore` file:

```
# This is a comment
file_to_ignore.txt
dir_to_ignore
```

This would cause the script to ignore any file named `file_to_ignore.txt` and any directory named `dir_to_ignore`.

## Limitations

- The script currently assumes that all files in the source directory tree are text files that can be read and written as strings. Binary files or files with unusual encodings may cause the script to fail.
- The `.rtsignore` file applies the same ignore list to all subdirectories. If you want to ignore a file or directory only in certain places, you will need to modify the script to include relative paths in the `.rtsignore` file.
- The script does not preserve the original file order when concatenating the files. If the order of files is important, you will need to modify the script to sort the files in the desired order.

## Requirements

- Python 3.6 or later
