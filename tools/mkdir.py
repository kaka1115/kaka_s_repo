import os

class FolderCreator:
    def __init__(self):
        pass
    def create_deck_cn(self):
        base_dir = os.path.join(r"C:\Users\Lenovo\Desktop","甲板文件夹模板网盘")
        sub_folders = [
            "1配载图",
            "2合同&发票&滞期费",
            "3始发港文件",
            "4目的港文件",
            "现场照片",
            "6其他文件"
        ]
        self._create_folder_tree(base_dir, sub_folders)
    def create_deck_en(self):
        """创建英文甲板文件夹"""
        base_dir = os.path.join(self.desktop_path, "甲板文件夹模板")
        sub_folders = [
            "1stowage",
            "2Contract_Invoice_Demurrage",
            "3AgentFiles_POL",
            "4AgentFiles_POD",
            "5SitePhotos",
            "6Other"
        ]
        self._create_folder_tree(base_dir, sub_folders)

    def create_towing_cn(self):
        """创建中文拖带文件夹（网盘版）"""
        base_dir = os.path.join(self.desktop_path, "拖带文件夹模板网盘")
        sub_folders = [
            "1被拖船规范",
            "2合同&发票&滞期费",
            "3拖航计划",
            "4起拖港文件",
            "5目的港文件",
            "6现场照片",
            "7其他文件"
        ]
        self._create_folder_tree(base_dir, sub_folders)

    def create_towing_en(self):
        """创建英文拖带文件夹"""
        base_dir = os.path.join(self.desktop_path, "拖带文件夹模板")
        sub_folders = [
            "1TowSpec",
            "2Contract_Invoice_Demurrage",
            "3TowingManual",
            "4AgentFiles_POL",
            "5AgentFiles_POD",
            "6SitePhotos",
            "7Other"
        ]
        self._create_folder_tree(base_dir, sub_folders)
    def _create_folder_tree(self, base_dir, sub_folders):

        os.makedirs(base_dir)
        for folder in sub_folders:
            folder_path = os.path.join(base_dir, folder)
            os.makedirs(folder_path)
        print("创建成功")


def auto_classify():
    creator = FolderCreator()
    intent_map = {
        "11": creator.create_deck_cn,
        "12": creator.create_deck_en,
        "13": creator.create_towing_cn,
        "14": creator.create_towing_en
    }
    while True:
        # 提示信息
        print("\n===== 文件夹创建工具 =====")
        print("第一个数字：1=甲板 / 2=拖带")
        print("第二个数字：1=中文（网盘版） / 2=英文")
        print("示例：输入11=创建中文甲板文件夹，输入22=创建英文拖带文件夹")
        print("输入q退出程序")

