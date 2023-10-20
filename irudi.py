import zipfile
import hashlib


# Function to calculate the hash of a file
def md5Kalkulatu(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(65536)  
            if not data:
                  break
            hasher.update(data)
    return hasher.hexdigest()

zip_file_path = '/home/erreka/segur/1 Laborategia -  Zifraketa I-20230921/irudia.zip'
with zipfile.ZipFile(zip_file_path, 'r') as archive:
	for file_info in archive.infolist():
	# Calculate the hash for each file in the archive
		file_name = file_info.filename
		file_hash = md5Kalkulatu(archive.extract(file_info))
		if "e5ed313192776744b9b93b1320b5e268" == file_hash:
			print(f'File: {file_name}, MD5: {file_hash}')
			archive.extract(file_info, "/home/erreka/segur/irudizuzen")
		
