#! /user/bin/env python
import openpyxl

class WriteData:

    array = ["地铁线", "片区", "小区名称", "户型", "方位", "面积", "总价", "均价", "楼层", "装修", "建造时间", "区域", "挂牌时间", "url"]
    info = {"地铁线": "", "片区": "", "小区名称": "", "户型": "", "方位": "", "面积": "", "总价": "",
                                 "均价": "", "楼层": "", "装修": "", "建造时间": "", "区域": "", "挂牌时间": "", "url": ""}

    number = 1
    path = "./building.xlsx"
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = '地铁沿线房价'

    def __init__(self, tile_array):
        #value = ["小区名称", "户型", "面积", "总价", "单价", "成交时间", "中介", "链接"]
        self._writeData(tile_array)

    def _writeData(self, array):
        for info in array:
            print(info)
        print("Append number = " + str(WriteData.number))
        for i in range(0, len(array)):
            WriteData.sheet.cell(WriteData.number, i + 1, str(array[i]))
        WriteData.wb.save(WriteData.path)
        WriteData.number = WriteData.number + 1
        print("写入数据成功！")

    def write(self, dict_value):
        print("Write >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        info_array = []
        for item in WriteData.array:
            print("write", item)
            info_array.append(dict_value.get(item))
        self._writeData(info_array)
        print("Write <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
         #_writeData(info_array)


if __name__ == '__main__':
    data = WriteData(WriteData.array)
