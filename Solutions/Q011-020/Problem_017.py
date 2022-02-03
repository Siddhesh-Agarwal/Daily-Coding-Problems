r"""
This problem was asked by Google.

Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

Note:
The name of a file contains at least a period and an extension.
The name of a directory or sub-directory will not contain a period.
"""


def find_longest_path(source):
    items = source.split(r"\n")
    prefix = []
    prefix_length = []
    max_length_so_far = -1
    max_path_so_far = r""

    for path in items:
        i = 0
        while path[i] == r"\t":
            i += 1
        if len(prefix) > i:
            prefix = prefix[:i]
            prefix_length = prefix_length[:i]

        prefix.append(path[i:])
        prefix_length.append(len(path[i:]))

        if sum(prefix_length) > max_length_so_far:
            max_length_so_far = sum(prefix_length)
            max_path_so_far = r"/".join(prefix)

    return max_path_so_far


if __name__ == "__main__":
    path_name = r"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    print(find_longest_path(path_name))

    path_name = r"dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    print(find_longest_path(path_name))
