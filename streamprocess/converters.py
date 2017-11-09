#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    该文件是针对process.py的继承，需要对converter方法重新定义
    完成对文件处理
"""
from processor import Processor


class Uppercase(Processor):
    def converter(self, data):
        return data.upper()


if __name__ == "__main__":
    import sys
    obj = Uppercase(open("spam.txt"), sys.stdout)
    obj.process()
