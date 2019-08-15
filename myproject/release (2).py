#!/usr/bin/env/python3
# _*_ coding : utf-8 _*_
#create 2019-08-02
#version: 0.0.1
#description:
import os
# base_path = [
#     "obs://backup-nextomics-wh/Sequencing/Nanopore/PCT0009/",
#     "obs://backup-nextomics-wh/Sequencing/Nanopore/PCT0020/"
# ]
#
# project_name = input("请输入合同编号：")
# print("请选择需要释放的类型：1、fastq; 2、原始数据")
# type_release = int(input("请选择："))
#
# with open('/home/liuy/ont.txt','r') as files:
#     cell_sample_list = files.readlines()
#     for cell_sample in cell_sample_list:
#         cell_list=cell_sample.split('\t')
#         cell_name = cell_list[0]
#         sample_name = cell_list[1]
#         if len(cell_name.split("-")) >= 5:
#             date, library, marchine, chip,barcode = cell_name.split("-")
#             barcode_cell = date+'-'+library+"-"+marchine+"-"+chip+"-barcode"+"-"+barcode+"/"
#             date_new = date[0:6]
#             if type_release == 1:
#                 if marchine == "P1":
#                     cell_path = base_path[1]+date_new+"/"+barcode_cell+"qc_report/"
#                     sign=os.system("obsutil cp -r -f -u {} obs://nextomcs6/{}/raw_data/genome/Nanopore/{}_{}".format(cell_path,project_name,sample_name,library))
#                     if sign == 1:
#                         print("释放完成")
#                 elif marchine == "P5":
#                     cell_path = base_path[0]+date_new+"/"+barcode_cell+"qc_report/"
#                     print(cell_path)
#             elif type_release == 2:
#                 if marchine == "P1":
#                     cell_path = base_path[1] + date_new + "/" + barcode_cell
#                     print(cell_path)
#                 elif marchine =="P5":
#                     cell_path = base_path[0] + date_new + "/" + barcode_cell
#                     print(cell_path)
#         elif len(cell_name.split("-")) == 4:
#             date, library, marchine, chip = cell_name.split("-")
#             if  type_release == 1:#释放fastq
#                 if marchine == "P1":#判断是否是p1
#                     cell_path = base_path[1]+date_new+"-"+cell_name+"-"+chip+"/qc_report/"
#                     print(cell_path)
#                 elif marchine == "P5":
#                     cell_path = base_path[0] + date_new + "-" + cell_name + "-" +chip+ "/qc_report/"
#                     print (cell_path)
#             elif type_release ==2: #释放原始数据
#                 if marchine =="P1":
#                     cell_path = base_path[1] + date_new + "-" + cell_name + "/"
#                     print(cell_path)
#                 elif marchine =="P5":
#                     cell_path = base_path[0] + date_new + "/" + cell_name + "/"
#                     print(cell_path)
#
#
#
#
#
#         else:
#             pass



import os
compact = input("请输入合同编号：   ")
type_release = input("请输入要释放的类型：\n 1. 原始数据 ；2.fastq  :")
type_choice=input("请输入释放方式：\n 1.obs释放 \n 2.硬盘释放：  ")
with open('ont.txt','r') as files:
    cell_sample_list = files.readlines()
    #print(cell_sample_list)
    for cell_sample in cell_sample_list:
        try:
            cell_list=cell_sample.split('\t')
            sample_name = cell_list[0].strip()
            cell_path = cell_list[1].strip()
            library_id = cell_path.split("-")[3]
            cell_name = cell_path.split("/")[7]
            #print(cell_name)
            chip_name = cell_name.split("-")[3]
            #print(chip_name)
            cell_path_list = cell_path.split("/")
            #print(cell_name)
        except Exception as e:
            cell_list = cell_sample.split(' ')
            sample_name = cell_list[0].strip()
            cell_path = cell_list[1].strip()
            library_id = cell_path.split("-")[3]
            cell_name = cell_path.split("/")[7]
            # print(cell_name)
            chip_name = cell_name.split("-")[3]
            # print(chip_name)
            cell_path_list = cell_path.split("/")
            # print(cell_name)
        #print(cell_path)
        if type_choice == "1":
            if "NB" in cell_path:
                #print(cell_path)
                barcode_id = cell_path.strip().split("/")[-2]
                #print(barcode_id)

                if type_release == "1":
                    target_path = "obs://nextomics6/FTP/{}/raw_data/genome/Nanopore/{}_{}/{}/".format(compact, sample_name,
                                                                                                    library_id, cell_name)
                    #print("obsutil cp -r -f {} {}".format(cell_path,target_path))
                    os.system("obsutil cp -r -f {} {}".format(cell_path,target_path))
                elif type_release == "2":#释放fastq
                    target_path = "obs://nextomics6/FTP/{}/raw_data/genome/Nanopore/{}_{}/{}/{}/".format(compact, sample_name,library_id,cell_name,barcode_id)
                    #print("obsutil cp -r -f {}qc_report {}".format(cell_path,target_path))
                    os.system("obsutil cp -r -f {}qc_report {}".format(cell_path, target_path))


            else :
                if type_release == "1":
                    target_path = "obs://nextomics6/FTP/{}/raw_data/genome/Nanopore/{}_{}/".format(compact, sample_name,
                                                                                                   library_id)
                    #print("obsutil cp -r -f {} {}".format(cell_path,target_path))
                    os.system("obsutil cp -r -f {} {}".format(cell_path, target_path))
                elif type_release == "2":#仅释放fastq
                    target_path = "obs://nextomics6/FTP/{}/raw_data/genome/Nanopore/{}_{}/{}/{}/".format(compact, sample_name,
                                                                                                   library_id,cell_name,chip_name)
                    #print(target_path)
                    #print("obsutil cp -r -f {}{}/qc_report {}".format(cell_path,chip_name,target_path))
                    os.system("obsutil cp -r -f {}{}/qc_report {}".format(cell_path,chip_name,target_path))
        elif type_choice == "2":
            pass
    os.system("obsutil cp -r -f ~/software/Nanopore_Data_documentation.doc obs://nextomics6/FTP/{}/raw_data/".format(compact))
    os.system("tree -L 5 /nextomics6/FTP/{} >> /nextomics6/FTP/{}/dirctory".format(compact,compact))









