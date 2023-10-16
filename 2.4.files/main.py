import glob
files = {}
for filename in glob.glob("sorted/*.txt"):
    with open(filename) as f:
        filename = filename.split('\\')[1]
        file_lines = f.read().splitlines()
        files[filename] = [str(len(file_lines)), file_lines]
files_list = files.items()
files_list = sorted(files_list, key=lambda a:a[1][0])
list_finish = []
for file in files_list:
    list_finish += (file[0], file[1][0])
    list_finish.extend(file[1][1])
list_finish = '\n'.join(list_finish)
with open('Result.txt', 'w') as f:
    f.write(list_finish)


