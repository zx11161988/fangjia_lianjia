import requests
from bs4 import BeautifulSoup
from PageUri import Page
from WriteExcel import WriteData
from MetrolineUri import Metroline
from CommunityUri import Community
from PageUri import Page
from BuildingUri import Building
from BuildingInfo import BuildingInfo
import time

if __name__ == '__main__':
    data = WriteData(WriteData.array)
    metro_line = Metroline(url="https://cd.lianjia.com/ershoufang/ng1hu1nb1/")
    dict_metro = metro_line.getMetroline()
    for k_metro, v_metro in dict_metro.items():
        print("Main, metro: ", k_metro, v_metro)
        WriteData.info["地铁线"] = k_metro
        community = Community(v_metro)
        community_url = community.getDictUrl()
        for k_community, v_community in community_url.items():
            print("Main, community: ", k_community, v_community)
            WriteData.info["片区"] = k_community
            page = Page(v_community)
            array_page_url = page.getUriList()
            for page in array_page_url:
                print("Main, page: ", page)
                building = Building(page)
                building_url = building.getUriList()
                for building in building_url:
                    time.sleep(0.01)
                    print("Main, building", building)
                    try:
                        building_info = BuildingInfo(building)
                        dict_building_info = building_info.getInfoDict()
                        for k_building_info, v_building_info in dict_building_info.items():
                            print("Main,buildingInfo:", k_building_info, v_building_info)
                        WriteData.info["小区名称"] = dict_building_info["小区名称"]
                        WriteData.info["户型"] = dict_building_info["户型"]
                        WriteData.info["方位"] = dict_building_info["方位"]
                        WriteData.info["面积"] = dict_building_info["面积"]
                        WriteData.info["总价"] = dict_building_info["总价"]
                        WriteData.info["均价"] = dict_building_info["均价"]
                        WriteData.info["楼层"] = dict_building_info["楼层"]
                        WriteData.info["装修"] = dict_building_info["装修"]
                        WriteData.info["建造时间"] = dict_building_info["建造时间"]
                        WriteData.info["区域"] = dict_building_info["区域"]
                        WriteData.info["挂牌时间"] = dict_building_info["挂牌时间"]
                        WriteData.info["url"] = dict_building_info["url"]
                        data.write(WriteData.info)
                    except Exception as e:
                        print("Main, Exception:", e)

