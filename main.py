import os
import shutil

question_menu = ["[QUEST] Select options - 1.Coping file with tag 2.Coping format files "]
question_txt = ["[QUEST] What the name tag ","[QUEST] Path from copy ","[QUEST] Path copy to ","[QUEST] Choose number - 1.View formats 2.View all 3.Continue Coping ","[QUEST] What the name format ","[QUEST] You sure to copied Y/N "]
warning_txt = ["[ERROR] You dont enter path, please try again ", "[ERROR] You dont enter tag, please try again "]

#_File_With_Tag_#

def file_tag(tag,path_after,path_before):
    
    if path_after == "": 
        print(warning_txt[0])
        return
    if path_before == "": 
        print(warning_txt[0])
        return
    if tag == "": 
        print(warning_txt[1])
        return

    path_after = path_after.replace(f'\\',"/")
    path_before = path_before.replace(f'\\',"/")

    files_tag = []
    folder = os.listdir(path_after)
    for file in folder:
        if tag in file:
            files_tag.append(file)

    print("[INFO] You want to copy :")

    if len(files_tag) >= 5:
        formats(files_tag)
    else:
        default(files_tag)

    answ = input(question_txt[3])
    match answ:
        case "1":
            formats(files_tag)
        case "2":
            default(files_tag)
        case "3":
            copinf_files(files_tag,path_after,path_before)


def copinf_files(files, path_af,path_bf):
    for file in files:
        shutil.copy(f"{path_af}/{file}", path_bf)
        print(f"[INFO] File - {file} ; Copied successful")


def default(files):
    i = 0
    for item in files:
        i = i + 1
        print(f"[INFO] {i}. {item}")


def formats(files):
    format_list = {}
    for item in files:
        if item[item.find(".")+ 1:] not in format_list: format_list[item[item.find(".")+ 1:]] = format_list[item[item.find(".")+ 1:]] = []
        format_list[item[item.find(".")+ 1:]].append(item)
    for key in format_list:
        print(f"[INFO] {key} - {len(format_list[key])}")
        

#_Format_In_Folder_#

def files_format(format,path_after,path_before):
    if path_after == "": 
        print(warning_txt[0])
        return
    if path_before == "": 
        print(warning_txt[0])
        return
    if format == "": 
        print(warning_txt[1])
        return

    path_after = path_after.replace(f'\\',"/")
    path_before = path_before.replace(f'\\',"/")

    files_format = []
    folder = os.listdir(path_after)
    for file in folder:
        if format in file:
            files_format.append(file)

    print("[INFO] You want to copy :")
    i = 0
    for item in files_format:
        i = i + 1
        print(f"[INFO] {i}. {item}")

    answ = input(question_txt[5]).upper()
    match answ:
        case "Y":
            copinf_files(files_format,path_after,path_before)
        case "N":
            return

def copinf_files(files, path_af,path_bf):
    for file in files:
        shutil.copy(f"{path_af}/{file}", path_bf)
        print(f"[INFO] File - {file} ; Copied successful")

def main():
    answ = input(question_menu[0])
    match answ:
        case "1":
            file_tag(input(question_txt[0]),input(question_txt[1]),input(question_txt[2]))
        case "2":
            files_format(input(question_txt[4]),input(question_txt[1]),input(question_txt[2]))
            
if __name__ == "__main__":
    main()