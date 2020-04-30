# -*- encoding:utf-8 -*-

class Student:
    __sid = 0
    __sname = ""
    __ssex = ""
    __sage = 0

    def setSid(self, sid):
        self.__sid = sid

    def getSid(self):
        return self.__sid

    def setSname(self, sname):
        self.__sname = sname

    def getSname(self):
        return self.__sname

    def setSsex(self, ssex):
        self.__ssex = ssex

    def getSsex(self):
        return self.__ssex

    def setSage(self, sage):
        self.__sage = sage

    def getSage(self):
        return self.__sage


