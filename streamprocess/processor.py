#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
此文件主要是表现对文件流处理器的体现
"""


class Processor:
    """
        这个类定义了转换器的方法，但是需要通过子类来填充
        读取器和写入器对象会内嵌在类实例当中——组合的方式
        但是需要在子类中提供转换器，而不是传入一个转换器函数
        详情见converters.py中定义的converter方法——当前的
        process.py体现了抽象基类
    """

    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def process(self):
        while 1:
            data = self.reader.readline()
            if not data:
                break

            data = self.converter(data)
            self.writer.write(data)

    def converter(self, data):
        assert False, "converter must be defined"
