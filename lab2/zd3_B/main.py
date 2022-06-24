import hashlib
file1 = "./Secret_file_11.txt"
file2 = "./Secret_file_12.pdf"
file3 = "./Secret_file_22.png"
file4 = "./Secret_file_48.docx"
file5 = "./Secret_file_49.pdf"
file6 = "./Secret_file_52.jpg"
file7 = "./Secret_file_72.docx"
file8 = "./Secret_file_92.jpg"
BLOCK_SIZE = 65536
TARGET_HASH = "c15e32d27635f248c1c8b66bb012850e5b342119"
file1_sha1 = hashlib.sha1()
file2_sha1 = hashlib.sha1()
file3_sha1 = hashlib.sha1()
file4_sha1 = hashlib.sha1()
file5_sha1 = hashlib.sha1()
file6_sha1 = hashlib.sha1()
file7_sha1 = hashlib.sha1()
file8_sha1 = hashlib.sha1()
with open(file1, 'rb') as f:
    fb = f.read(BLOCK_SIZE)
    while len(fb) > 0:
        file1_sha1.update(fb)
        fb = f.read(BLOCK_SIZE)
if file1_sha1.hexdigest() == TARGET_HASH:
    print("Trazeni dokument je Secret_file_11.txt")
with open(file2, 'rb') as f:
    fb = f.read(BLOCK_SIZE)
    while len(fb) > 0:
        file2_sha1.update(fb)
        fb = f.read(BLOCK_SIZE)
if file2_sha1.hexdigest() == TARGET_HASH:
    print("Trazeni dokument je Secret_file_12.pdf")
with open(file3, 'rb') as f:
    fb = f.read(BLOCK_SIZE)
    while len(fb) > 0:
        file3_sha1.update(fb)
        fb = f.read(BLOCK_SIZE)
if file3_sha1.hexdigest() == TARGET_HASH:
    print("Trazeni dokument je Secret_file_22.png")
with open(file4, 'rb') as f:
    fb = f.read(BLOCK_SIZE)
    while len(fb) > 0:
        file4_sha1.update(fb)
        fb = f.read(BLOCK_SIZE)
if file4_sha1.hexdigest() == TARGET_HASH:
    print("Trazeni dokument je Secret_file_48.docx")
with open(file5, 'rb') as f:
    fb = f.read(BLOCK_SIZE)
    while len(fb) > 0:
        file5_sha1.update(fb)
        fb = f.read(BLOCK_SIZE)
if file5_sha1.hexdigest() == TARGET_HASH:
    print("Trazeni dokument je Secret_file_49.pdf")
with open(file6, 'rb') as f:
    fb = f.read(BLOCK_SIZE)
    while len(fb) > 0:
        file6_sha1.update(fb)
        fb = f.read(BLOCK_SIZE)
if file6_sha1.hexdigest() == TARGET_HASH:
    print("Trazeni dokument je Secret_file_52.jpg")
with open(file7, 'rb') as f:
    fb = f.read(BLOCK_SIZE)
    while len(fb) > 0:
        file7_sha1.update(fb)
        fb = f.read(BLOCK_SIZE)
if file7_sha1.hexdigest() == TARGET_HASH:
    print("Trazeni dokument je Secret_file_72.docx")
with open(file8, 'rb') as f:
    fb = f.read(BLOCK_SIZE)
    while len(fb) > 0:
        file8_sha1.update(fb)
        fb = f.read(BLOCK_SIZE)
if file8_sha1.hexdigest() == TARGET_HASH:
    print("Trazeni dokument je Secret_file_92.jpg")