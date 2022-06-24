import hashlib
file1 = "./test.docx"
file2 = "./test.jpg"
BLOCK_SIZE = 65536
file1_md5 = hashlib.md5()
file1_sha1 = hashlib.sha1()
file1_sha256 = hashlib.sha256()
file2_md5 = hashlib.md5()
file2_sha1 = hashlib.sha1()
file2_sha256 = hashlib.sha256()
with open(file1, 'rb') as f:
    fb = f.read(BLOCK_SIZE)
    while len(fb) > 0:
        file1_md5.update(fb)
        file1_sha1.update(fb)
        file1_sha256.update(fb)
        fb = f.read(BLOCK_SIZE)
print("test.docx md5: " + file1_md5.hexdigest())
print("test.docx sha1: " + file1_sha1.hexdigest())
print ("test.docx sha256: " + file1_sha256.hexdigest())
print("\n")
with open(file2, 'rb') as f:
    fb = f.read(BLOCK_SIZE)
    while len(fb) > 0:
        file2_md5.update(fb)
        file2_sha1.update(fb)
        file2_sha256.update(fb)
        fb = f.read(BLOCK_SIZE)
print("test.jpg md5: " + file2_md5.hexdigest())
print("test.jpg sha1: " + file2_sha1.hexdigest())
print ("test.jpg sha256: " + file2_sha256.hexdigest())