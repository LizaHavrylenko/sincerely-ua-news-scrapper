# get 

import os
from pyquery import PyQuery as pq
import requests
# from lxml import etree

from dateutil.rrule import rrule, DAILY
from datetime import date
import datetime
import json

import dateparser

import html2text


import re

import settings

import html

# import time

with open('parties', 'r') as f:
    parties = f.read().splitlines()


from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

import requests





f = open('out.tsv','w')
f2 = open('all.tsv','w')




# print(dir(lst[0]))
    # print("-".join([str(item.day)   ,str(item.month), str(item.year)]))


# print("here")


def print_page(h3s):
    for h3 in h3s:
        # h3 = q('h3')[1]
        href_elem = h3.getparent().getparent().getparent().getchildren()[0]
        if 'href' in href_elem.attrib:
            full_href = "".join(['https://www.segodnya.ua', href_elem.attrib['href']])
        else:
            print("improper h3:", h3.text)
            continue
        date = h3.getnext()
        if date:
            date = date.getchildren()[0].text
        else:
            print("no date for h3:", h3.text)
        keywords = ['Ляшк', 'Мосийчук', 'Лозово', 'Радикальная партия', 'радикалы']
        f2.write('\t'.join([h3.text, full_href, date]) + '\n')
        if any(word in h3.text for word in keywords):
            print('\t'.join([h3.text, full_href, date]))
            f.write('\t'.join([h3.text, full_href, date]) + '\n')


def print_day(day="02-11-2017"):
    i = 1
    while (True):
        q = pq("https://www.segodnya.ua/allnews/archive/" + day + "/p" + str(i) + ".html")
        # time.sleep(1)
        h3s = q('h3')
        print(len(h3s))
        if len(h3s) < 2:
            break
        print("page:", i)
        print_page(h3s)
        i += 1


class Site():
    def __init__(self, json_input_path):
        # ISO data
        self.iso_date_template = "%Y-%m-%d"
        json1_file = open(json_input_path)
        json1_str = json1_file.read()
        input = json.loads(json1_str)
        json1_file.close()

        self.domain_name = input['site_domain_name']

        if self.domain_name in settings.settings:
            self.templates = settings.settings[self.domain_name]
        else:
            print("No templates for this domain name")



        self.start_date = datetime.datetime.strptime(input['start_date'], self.iso_date_template).date()
        self.end_date = datetime.datetime.strptime(input['end_date'], self.iso_date_template).date()

        path = os.path.join(os.getcwd(),'articles',self.domain_name)

        if not os.path.exists(path):
            os.mkdir(path)
        self.articles_path = path

    def get_articles_urls(self, link_to_links):
        print(link_to_links)
        article_template = self.templates["article_link_template"]
        q = pq(link_to_links)(self.templates['articles_list_content_blocks_template'])
        a_tags = q(article_template)
        urls = []
        for a in a_tags:

            urls.append("".join([a.base, a.attrib['href']]))

        # urls = ['https://' + self.domain_name + url if 'https://' not in url else url for url in urls ]
        return urls

    def getlinks(self, remember = False):
        """Get articles' links given domain name and a date range"""

        links_to_links = []
        links = []
        current_date = ""
        if os.path.exists("links"):
            os.remove("links")


        if "articles_list_by_day_template" in self.templates:
            date_template = self.templates["date_template"]
            dates = [date_time.date() for date_time in
                     rrule(DAILY, dtstart=self.start_date, until=self.end_date)]


            articles_list_url = self.templates["articles_list_by_day_template"]
            if "{page_number}" in articles_list_url:

                for day in dates:
                    print("Procesing", day)
                    day_links = []
                    if "pages_template" in self.templates:

                        starting_link_to_links = articles_list_url.format(date=day.strftime(date_template),
                                                                          page_number=str(1))
                        q = pq(starting_link_to_links)
                        max_pages = int(q(self.templates["pages_template"]).text())
                    else:
                        max_pages = 20
                    print("MaxPages:", max_pages)
                    for page in range(max_pages):
                        print("     Processing", page+1)

                        link_to_links = articles_list_url.format(date=day.strftime(date_template), page_number=str(page+1))

                        day_links = day_links + self.get_articles_urls(link_to_links)

                    self.to_memory(day, day_links)
            else:
                for day in dates:
                    print("Procesing", day)
                    link_to_links = articles_list_url.format(date=day.strftime(date_template))
                    day_links = self.get_articles_urls(link_to_links)
                    self.to_memory(day, day_links)
        else:
            print("Got no links.")
            return None

        # for link_to_links in links_to_links:
        #     links_by_day = self.get_articles_urls(link_to_links)
        #     print(links_by_day)
        #     links = links + links_by_day
        #
        # full_links = []
        # for link in links:
        #     if self.domain_name not in link:
        #         link = 'https://' + self.domain_name + link
        #     full_links.append(link)
        #
        # for link in full_links:
        #     print(link)
        # return full_links

    def getarticles(self):
        """get articles along with metadata"""
        with open('links') as links_file:
            links = links_file.read().splitlines()
        # for link in links():
        for link in links:
            article = self.getarticle(link)
            es.index(index='news', doc_type='article', body=article)

        # link = links[0]
        # os.makedirs(os.path.join(self.articles_path,link), exist_ok=True)


    def getarticle(self, link):
        print(link)
        response = requests.get(link)
        q = pq(response.text)

        title = q(self.templates['article_title_template']).text()
        print("Title", title)

        pub_tag = q(self.templates['article_publication_datetime'])
        print("here", pub_tag.text())
        if len(pub_tag) > 0:
            pub_tag = pub_tag[0]

        if 'datetime' in pub_tag.attrib:
            publication = pub_tag.attrib['datetime']
        else:
            publication = pub_tag.text()

        publication = str(dateparser.parse(publication))
        print(publication)

        article_html = q(self.templates['article_text_template'])
        h = html2text.HTML2Text()
        h.ignore_links = True
        article_text = h.handle(str(article_html))

        symbol_count = len(h.handle(str(article_html)))

        tags = str(q(self.templates['tags_template']).attr("content")).split(", ")

        if "news_keywords" in self.templates:
            marking = str(q(self.templates["news_keywords"]).attr("content")).split(", ")
        else:
            marking = ""

        metadata = {
            'domain': self.domain_name,
            'link' : link,
            'title' : title,
            'pubdate' : publication,
            'article_html' : str(article_html),
            'article_text' : article_text,
            'party' : '',
            'symbol_count' : symbol_count,
            'tags' : tags,
            'marking': marking
        }

        print(metadata)
        return metadata

        # folder_path = "/".join(["articles", self.domain_name])
        #
        #
        # if not(os.path.exists(folder_path)):
        #     os.mkdir(folder_path)
        #
        # with open("".join([folder_path, '/', title, ".json"]), 'w') as f:
        #     json.dump(metadata, f)

    def to_memory(self, current_date, date_links):
        with open('memory', 'w') as memory:
            start_date = (current_date + datetime.timedelta(days=1)).strftime(self.iso_date_template)
            site = {
                "site_domain_name" : self.domain_name,
                "start_date" : start_date,
                "end_date" : self.end_date.strftime(self.iso_date_template)
            }
            json.dump(site, memory)

        with open("links", "a") as links_file:
            for item in date_links:
                print(item)
            joined_links = '\n'.join(date_links) + '\n'
            links_file.write(joined_links)





def recall_site():
    return Site(json_input_path='memory')


# 876

#1053






# print(os.getcwd())
# site = Site()
# site.getarticles()
    #
    #
    #
    #
    # for url in articles_list_urls[:2]:
    #     print(url)
    #
    # for date in dates[:2]:
    #     print(date)
    #     print_day(str(date))



# getinfo()



# print(h3.text, href.attrib['href'])
# # print(etree.tounicode(parentparent, pretty_print=True))
# # print(q('h3').parent().parent())
# # elements = q('h3')[1].getparent().getparent().getchildren()
# for element in parentparent:
#   print("Element:")
#   print(etree.tounicode(element, pretty_print=True))
#   # print(type(element))
    # print(element.tag, element.text)


