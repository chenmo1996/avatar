# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import urllib
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

from avatar import settings

class DetailPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):  # 重写ImagesPipeline   get_media_requests方法
        '''
        :param item:
        :param info:
        :return:
        在工作流程中可以看到，
        管道会得到文件的URL并从项目中下载。
        为了这么做，你需要重写 get_media_requests() 方法，
        并对各个图片URL返回一个Request:
        '''
        for image_url in item['image_urls']:
            print(image_url)
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        '''

        :param results:
        :param item:
        :param info:
        :return:
        当一个单独项目中的所有图片请求完成时（要么完成下载，要么因为某种原因下载失败），
         item_completed() 方法将被调用。
        '''
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item
    #

    # def process_item(self, item, spider):
    #     return item
