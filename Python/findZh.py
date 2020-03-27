
# coding = utf-8

import re
import os
import shutil
from collections import OrderedDict
import logging
import unittest

log = logging.getLogger("main")
log.setLevel("DEBUG")
fmt = logging.Formatter("%(levelname)s %(asctime)s %(module)s %(message)s")
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel("INFO")
consoleHandler.setFormatter(fmt)
fileHandler = logging.FileHandler("main.log")
fileHandler.setLevel("DEBUG")
fileHandler.setFormatter(fmt)
log.addHandler(consoleHandler)
log.addHandler(fileHandler)



def filter_file(filepath,suffix):
    """
    存在指定后缀的文件, 返回True
    :param filepath:
    :param suffix:
    :return:
    """
    if os.path.splitext(filepath)[1] in suffix:
        return True
    return False


def getDirs(source_dir, exclude=None):
    """
    获取所有符合的文件夹,
    :param source_dir:  dir
    :param exclude: 排除的文件夹 例如: [".git", ".idea", ".vs"]
    :return:
    """
    if exclude is None:
        exclude = []
    dirs = []
    for dir in os.listdir(source_dir):
        obspath = os.path.join(source_dir,dir)
        if os.path.isdir(obspath) and (dir not in exclude):
            dirs.append(obspath)
    return dirs


def getFiles(source_dirs,suffix=None,excludedir=None):
    """
    获取所有符合的文件
    :param source_dirs: [] 多个目录
    :param suffix: 文件后缀,例如: [".json",".txt"], 返回匹配后缀的文件
    :param excludedir: 排除的文件夹 例如: [".git", ".idea", ".vs"]
    :return:
    """
    if suffix is None:
        suffix = []
    if excludedir is None:
        excludedir = []

    obs_path_files = []
    for source_dir in source_dirs:
        subdirs = getDirs(source_dir,excludedir)
        for path in subdirs:
            for root, dirs, files in os.walk(path):
                for file in files:
                    if filter_file(file,suffix):
                        file_obs_path = os.path.join(root,file)
                        obs_path_files.append(file_obs_path)
    return obs_path_files


def transToLinesep(line,sep=os.linesep):
    """
    转换换行符
    :param line:
    :param sep:
    :return:
    """
    r = "\n\r|[\r\n]"
    repl = re.compile(r)
    transted_line = re.sub(repl, sep, line)
    return transted_line

# 检测存在中文字符,存在返回True
def check_hans(s):
    r = "[\u4e00-\u9fa5]"
    pattern = re.compile(r)
    result = re.search(pattern,s)
    if result is not None:
        return True

def parse_json():
    pass

if __name__ =="__main__":

    pass
