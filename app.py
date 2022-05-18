
# importing the "tarfile" module
import tarfile

# open file
file = tarfile.open('ANPR_Assignment.tar.gz')

# extracting file
file.extractall('./data')

file.close()
