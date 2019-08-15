#!/usr/bin/env/python3
#!-*- codong : utf-8 -*-
#author : liuy
#create on ; 2019-08-02
#version 1.0



import os
import logging
logging.basicConfig(filename="/data/basecalled/log/putfile.log",filemode='a',level=logging.INFO,format="%(asctime)s - %(name)s - %(levelname)s -  %(message)s")

class PutDonefile(object):
    '''
    此类的主要功能就是提供批量投放done文件
    '''

    def __init__(self,base_path):
        self.path = base_path
        self.cell_list = os.listdir(base_path)


    def get_cell_path(self):
        cell_name = []
        with open("/home/prom/cellname.txt",'r') as f:
            cell_list = f.readlines()
            for cell in cell_list:
                cell_name.append(cell.strip())
        return cell_name

    def pufiles(self,lis):
        for cell in lis:
            if cell in self.cell_list:
                chip_list=cell.split("-")
                chip = chip_list[3]
                cell_abs_path = self.path+cell+"/"+chip+"/"
                if os.path.exists(cell_abs_path):
                    sign = os.system("echo {}done".format(cell_abs_path))
                    if sign == 0:
                        print("创建成功")
                        logging.info("%s : has add done"%(cell,))
                    else:
                        print("创建文件失败")
            else:
                print("%s 的路径不存在"%(cell,))
                continue


if  __name__ == "__main__":
    put_obj = PutDonefile("/data/basecalled/")
    cell_name = put_obj.get_cell_path()
    put_obj.pufiles(cell_name)






