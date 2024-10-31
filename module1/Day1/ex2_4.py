# 2.4 - Variables and operations
# Write a program that calculates storage capabilities
# Instructions
# The company has a 5,000 GB data storage.

# The company was handed over 20 files for placement. The volume of one file is 256 GB. Not all the data will fit in the storage. How many files can we put in the storage? How much free space will be left?

# Write a program that does the computations.
# Expected output
# The storage will be able to fit 19 files
# 136 GB will remain

storage = 5000
number_of_files = 20
size_of_file = 256

files_that_fit = storage // size_of_file
remaining_space = storage % size_of_file
print(f"The storage will be able to fit {files_that_fit} files")
print(f"{remaining_space} GB will remain")