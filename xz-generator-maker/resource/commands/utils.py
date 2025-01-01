import os
from pathlib import Path


def get_basic_path():
    """
    获取 xz-generator-basic 所在路径
    :return:
    """
    path = Path(__file__).parent.parent.parent.absolute()
    return path


def get_root_path():
    """
    获取 xz-generator 所在路径
    :return:
    """
    path = Path(__file__).parent.parent.parent.parent.absolute()
    return path


def find_file_by_name(folder_path, target_filename):
    """
    在指定文件夹及其子文件夹中寻找指定名字的文件
    :param folder_path: 要搜索的文件夹路径
    :param target_filename: 要查找的文件名
    :return: 文件的完整路径列表
    """
    matching_files = []

    # 遍历文件夹及其子文件夹
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file == target_filename:  # 如果文件名匹配
                matching_files.append(os.path.join(root, file))

    return matching_files
