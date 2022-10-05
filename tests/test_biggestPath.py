import pytest as pytest

from main import BiggestPath, LengthPathOutOfRange, DuplicateName

biggestPath = BiggestPath()


def test_path_depth():
    dir_dct = {'dir1': {},
               'dir2': ['file1'],
               'dir3': {
                   'dir4': ['file2'],
                   'dir5': {
                       'dir6': {
                           'dir7': {}
                               }
                           }
                       }
               }
    assert biggestPath(dir_dct) == '/dir3/dir5/dir6/dir7'


def test_path_with_whitespaces():
    dir_dct = {'dir1': {},
               'dir2': ['file1'],
               'dir3': {
                   'dir4': {},
                   'dir_5': {
                       'dir6': {
                           'dir7': {}
                               }
                           }
                       }
               }
    assert biggestPath(dir_dct) == '/dir3/dir4'


def test_path_not_depth():
    dir_dct = {'dir1': ['file1', 'file2'],
               }
    assert biggestPath(dir_dct) == '/'


def test_tree_path():
    dir_dct = {
        'dir1': {},
        'dir2': ['file1'],
        'dir3': {
            'dir4': ['file2'],
            'dir5': {
                'dir6': {
                    'dir7': {}
                        }
                    }
                },
        'dir8': {
            'dir9':{
                'dir10': {
                    'dir11': {}
                            }
                        }
                    },
            'dir12':  ['file3'],
                }
    assert biggestPath(dir_dct) == '/dir8/dir9/dir10/dir11'


def test_very_length_path_error():
    dir_dct = {'dir1': {
                        'dir2': {
                            'a'*255: {}
                                }
                        }
               }
    with pytest.raises(Exception) as e:
        biggestPath(dir_dct)
    assert e.type == LengthPathOutOfRange


def test_duplicate_name():
    dir_dct = {'dir1': ['file1', 'file1']}
    with pytest.raises(Exception) as e:
        biggestPath(dir_dct)
    assert e.type == DuplicateName
