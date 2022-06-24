import magic
print(magic.from_buffer(open("file1", "rb").read(2048)))
print(magic.from_buffer(open("file2.txt", "rb").read(2048)))
print(magic.from_buffer(open("file3", "rb").read(2048)))
