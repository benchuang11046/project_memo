from checksumdir import _filehash
import hashlib
import sys
import os

def filehash(filepath):
    blocksize = 64 * 1024
    sha = hashlib.sha256()
    with open(filepath, 'rb') as fp:
        while True:
            data = fp.read(blocksize)
            if not data:
                break
            sha.update(data)
    return sha.hexdigest()

def check_file_hash(file):
    md5hash = filehash(file)
    return {'md5hash': md5hash}


def compare_two_file_hash(directory1, directory2):
    num = range(1, 21)
    num = ['Stress' + str(i).zfill(2) + '.JSON' for i in num]
    paths_one = [os.path.join(directory1, file_name) for file_name in num]
    paths_two = [os.path.join(directory2, file_name) for file_name in num]
    paths_all = [[paths_one[i], paths_two[i]] for i in range(0,20)]

    for path_both in paths_all:
        return_data_one = check_file_hash(path_both[0])
        md5hash_one = return_data_one['md5hash']
        return_data_two = check_file_hash(path_both[1])
        md5hash_two = return_data_two['md5hash']
        if md5hash_one == md5hash_two:
            print('md5 same')
        else:
            print('md5 not same, {0} and {1}'.format(path_both[0], path_both[1]))


if __name__ == '__main__':
    compare_two_file_hash(sys.argv[1], sys.argv[2])