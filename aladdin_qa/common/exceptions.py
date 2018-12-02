# -*- coding:utf-8 -*-
# author: songyangyang
# time: 2018/10/15

class RegistException(Exception):
    def __init__(self, err):
        Exception.__init__(self)
        self.err = err


class ImageUploadToOssFailException(Exception):
    def __init__(self, err):
        Exception.__init__(self)
        self.err = err