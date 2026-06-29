import os
from os import listdir as l, path as p

def rename_photos():

    while True:
        path = input("程序会一直执行，按q退出，谢谢~\n"
                     "请输入文件地址：")
        path = path.strip('"')

        if path == "q":
            print("程序退出成功！")
            break
        else:
            dirs = l(path)
            count = 1
            for idx, old_name in enumerate(dirs):
                ext = os.path.splitext(old_name)[1]
                new_name = f"{count}{ext}"
                full_old_name = p.join(path, old_name)
                full_new_name = p.join(path, new_name)
                os.rename(full_old_name, full_new_name)
                count += 1
                print(f"重命名成功{count}张图片")
if __name__ == "__main__":
    rename_photos()