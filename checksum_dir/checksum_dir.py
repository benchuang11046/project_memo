from checksumdir import dirhash
import sys

def check_dir_hash(directory):
    md5hash = dirhash(directory, 'md5')
    sha1hash = dirhash(directory, 'sha1')
    # print('directory: %s' % directory)
    # print("md5 value : %s" % md5hash)
    # print("sha1 value : %s" % sha1hash)
    return {'md5hash': md5hash, 'sha1hash': sha1hash}


def compare_two_dir_hash(directory1, directory2):
    return_data_one = check_dir_hash(directory1)
    md5hash_one = return_data_one['md5hash']
    sha1hash_one = return_data_one['sha1hash']
    return_data_two = check_dir_hash(directory2)
    md5hash_two = return_data_two['md5hash']
    sha1hash_two = return_data_two['sha1hash']
    if md5hash_one == md5hash_two:
        print('md5 same')
    else:
        print('md5 not same')
    if sha1hash_one == sha1hash_two:
        print('sha1hash same')
    else:
        print('sha1hash not same')


if __name__ == '__main__':
    compare_two_dir_hash(sys.argv[1], sys.argv[2])