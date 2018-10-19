# -*- coding: utf-8 -*-
"""
    LearningFluentyPython.create_flask_project_tree
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    create flask project tree

    :copyright: (c) 2018 by  Raymond.
    :last modified by 2018-10-19 11:45:37
"""

import argparse
import logging
import os

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


parser = argparse.ArgumentParser(description="create flask app project script")
parser.add_argument('--name', type=str, default="myproject")
parser.add_argument('--path', type=str, default=".")
parser.add_argument('--appname', type=str, default="app")

args = parser.parse_args()

path = os.path.abspath(args.path)
project_name = args.name
default_app_name = args.appname

init_file = "__init__.py"

root = project_name
next_node = {
    default_app_name: "views.py,models.py,forms.py,static,templates",
    "files": "config.py,requirements.txt,run.py",
    "instance": "config.py"}


def generator_tree(root, next_node, path=path):
    """
    通过默认配置结构, 在指定路径下创建 flask 项目结构
    """
    if path != args.path:
        path = os.path.abspath(path)
    path = os.path.join(path, root)
    if os.path.exists(path):
        logging.info("project already exists.")
        return
    os.mkdir(path)
    if not os.path.exists(os.path.join(root, default_app_name)):
        os.mkdir(os.path.join(root, default_app_name))
    for root, files in next_node.items():
        for file in files.split(","):
            if root == "files":
                file_path = os.path.join(path, file)
                logging.info("touch {} is ok.".format(file_path))
                open(file_path, "a").close()
                continue
            dir_path = os.path.join(path, root)
            file_path = os.path.join(path, root, file)
            init_file_path = os.path.join(path, root, init_file)
            if not os.path.exists(dir_path):
                logging.info("mkdir {} is ok".format(dir_path))
                os.mkdir(dir_path)
            if not file.endswith(".py"):
                os.mkdir(file_path)
                logging.info("mkdir {} is ok".format(file_path))
                continue
            open(file_path, "a").close()
            open(init_file_path, "a").close()
            logging.info("touch {} is ok.".format(file_path))


if __name__ == "__main__":
    generator_tree(root, next_node, ".")
