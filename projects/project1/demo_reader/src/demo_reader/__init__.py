""" this is the test module
"""
print ('demo_reader is being imported')
from demo_reader.compressed.bzipped import opener as bz2_opener
from demo_reader.compressed.gzipped import opener as gzip_opener
__all__ = ['bz2_opener','gzip_opener']

