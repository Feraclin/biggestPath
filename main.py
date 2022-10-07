from function.biggestPath import BiggestPath

if __name__ == '__main__':
    dir_dct1 = {
        'dir1': {},
        'dir2': ['file1'],
        'dir3': {
            'dir4': ['file2'],
            'dir5': {
                'dir6': {
                    'dir7': ['file2']
                }}},
        'dir8': {
            'dir9': ['file3'],
            'dir10': {
                'dir11': {}}},
    }
    dir_dct2 = {
        'dir1': {},
        'dir2': ['file1'],
        'dir3': {
            'dir4': ['file2'],
            'dir5': {
                'dir6': {
                    'dir7': {}
                }}},
        'dir8': {
            'dir9': ['file3'],
            'dir10': {
                'dir11': {}}},
    }
    biggestPath = BiggestPath()
    print('d1', biggestPath(dir_dct1))
    print('d1', biggestPath(dir_dct2))
