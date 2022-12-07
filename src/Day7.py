import queue

#operating on a set
def day7_base():
    f = open("../inputs/day7.txt", "r")
    searched_size = 0
    MAX_SIZE = 100000
    current_folders_data = []

    while True:
        command = f.readline()
        if not command:
            while len(current_folders_data) > 1:
                if current_folders_data[-1] < MAX_SIZE:
                    searched_size += current_folders_data[-1]
                current_folders_data[-2] += current_folders_data[-1]
                current_folders_data.pop()
            break
        processed = command.split(" ")
        if processed[0] == '$':
            if processed[-1] == "..\n":
                if current_folders_data[-1] < MAX_SIZE:
                    searched_size += current_folders_data[-1]
                current_folders_data[-2] += current_folders_data[-1]
                current_folders_data.pop()
            elif processed[1] != "ls\n":
                current_folders_data.append(0)
        elif processed[0] != "dir":
            current_folders_data[-1] += int(processed[0])
    f.close()
    if current_folders_data[0] < MAX_SIZE:
        searched_size += current_folders_data[0]
    print("Total size of searched folders: " + str(searched_size))

#using recurrence
def day7_extra():
    f = open("../inputs/day7.txt", "r")
    TOTAL = 70000000
    MIN_FREE = 30000000
    sizes = queue.Queue()
    f.readline()
    top_folder, sizes = calc_folder_size(f, sizes)
    f.close()
    min_f_size = MIN_FREE - (TOTAL - top_folder)
    folder_to_del = top_folder
    while not sizes.empty():
        current = sizes.get()
        if min_f_size < current:
            if folder_to_del > current:
                folder_to_del = current
    print("Folder to delete size: " + str(folder_to_del))


def calc_folder_size(f, sizes):
    folder_size = 0
    while True:
        command = f.readline()
        if not command:
            sizes.put(folder_size)
            return folder_size, sizes
        processed = command.split(" ")
        if processed[0] == '$':
            if processed[-1] == "..\n":
                sizes.put(folder_size)
                return folder_size, sizes
            elif processed[1] != "ls\n":
                temp_size, sizes = calc_folder_size(f, sizes)
                folder_size += temp_size
        elif processed[0] != "dir":
            folder_size += int(processed[0])
