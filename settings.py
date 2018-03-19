# settings = {
#     "www.segodnya.ua":
#         {
#         "articles_list_by_day_template" : "https://www.segodnya.ua/allnews/archive/{date}/p{page_number}.html",
#         "articles_list_content_blocks_template" : "div.content-blocks",
#         "article_link_template" : "div.overflow-wrap.white-frame a",
#         "date_template" : "%d-%m-%Y",
#         "pages_template" : "div.pagination ul.pages li:last",
#         "article_title_template" : "h1",
#         "article_publication_datetime" : "div.title div span:first",
#         "article_text_template" : "span._ga1_on_",
#         "tags_template2" : "div.tag a",
#         "tags_template": "meta[name=keywords]",
#         "news_keywords": "meta[name=news_keywords]"
#         }
#
# }
#


settings = {
    "www.segodnya.ua":
    {
        "articles_list_by_day_template" : "https://www.segodnya.ua/allnews/archive/{date}/p{page_number}.html",
        "articles_list_content_blocks_template" : "div.content-blocks",
        "article_link_template" : "div.overflow-wrap.white-frame a",
        "date_template" : "%d-%m-%Y",
        "pages_template" : "div.pagination ul.pages li:last",
        "article_title_template" : "h1",
        "article_publication_datetime" : "div.title div span:first",
        "article_text_template" : "span._ga1_on_",
        "tags_template2" : "div.tag a",
        "tags_template": "meta[name=keywords]",
        "news_keywords": "meta[name=news_keywords]"
    },
    "www.tsn.ua":
    {
        "articles_list_by_day_template" : "https://tsn.ua/sitemap/text/{date}/index.html",
        "articles_list_content_blocks_template" : "ul:last",
        "article_link_template" : "a",
        "date_template" : '%Y/%-m/%-d',
        "article_title_template" : "h1.p-name.c-post-title.u-uppercase",
        "article_publication_datetime" : "div.c-bar-unit time.dt-published.c-post-time",
        "article_text_template" : "div.o-cmr.u-content-read.js-select-bar-wrap",
        "tags_template": "meta[name=keywords]",
    },
    "www.24tv.ua":
    {
        "articles_list_by_day_template": "https://24tv.ua/archive/{date}/index.html",
        "articles_list_content_blocks_template": "div.news-list.category_list.b_video",
        "article_link_template": "li a.news_title",
        "date_template": "%d_%B_%Y",
        # "pages_template" : "div.col-12",
        "article_title_template": "h1.article_title",
        "article_publication_datetime": "div.news-info-big span.date",
        "article_text_template": "div.news_text",
        "tags_template2": "div.tags a",  # loop through a
        "tags_template": "",
    },
    "www.korrespondent.net":
    {
        "articles_list_by_day_template": "https://ua.korrespondent.net/all/{date}/p{page_number}",
        "articles_list_content_blocks_template": "div.article.article_rubric_top,div.article.article_top.article_right a:first",
        "article_link_template": "ul.list",
        "date_template": "%Y/%B/%d",
        "pages_template": "div.col-12",
        "article_title_template": "h1.article_title",
        "article_publication_datetime": "h1.article_title div span:date",
        "article_text_template": "div.news_text",
        "tags_template2": "div.tags a",  # loop through a
        "tags_template": "",
    },
    "www.telegraf.com.ua":
   {
       "articles_list_by_day_template" : "https://telegraf.com.ua/sitemap/{date}.html",
       "articles_list_content_blocks_template" : "", #taka-to hernia
       "article_link_template" : "a.href",
       "date_template" : "%Y_%B_%d",
       # "pages_template" : "div.col-12",
       "article_title_template" : "h1.itemprop",
       "article_publication_datetime" : "div.article div span:date",
       "article_text_template" : "div.block-post-text",
       "tags_template2" : "div.keywords_block", #loop through a
       "tags_template": "",
   },
   "www.strana.ua":
   {
       "articles_list_by_day_template" : "https://strana.ua/archive/day={date}/page-{page_number}.html",
       "articles_list_content_blocks_template" : "section.main",
       "article_link_template" : "div.title a:article",
       "date_template" : "%Y_%B_%d",
       "pages_template" : "div.col-12",
       "article_title_template" : "h1.article",
       "article_publication_datetime" : "div.article-meta div time:date",
       "article_text_template" : "div.article-body",
       "tags_template2" : "div.tags", #loop through a
       "tags_template": "",
   }
   "censor.net.ua":{
   + "articles_list_by_day_template" : "https://censor.net.ua/news/all/page/{page_number}/archive/{date}/category/0/sortby/date",
    +   "articles_list_content_blocks_template" : "div.curpane",
     +  "article_link_template" : "h3 a",
      + "date_template" : "%Y_%m_%d",
      # "pages_template" : "div.col-12",
      + "article_title_template" : "h1.entry-title",
      + "article_publication_datetime" : "time.published.dateline",
      + "article_text_template" : "div.text",
       +"tags_template2" : "div.tags", 
      + "tags_template": "div.news_by_theme",
   }
}


