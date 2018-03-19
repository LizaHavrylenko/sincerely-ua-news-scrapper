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
       "article_title_template" : "header h1",
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
   "www.censor.net.ua":{
   + "articles_list_by_day_template" : "https://censor.net.ua/news/all/page/{page_number}/archive/{date}/category/0/sortby/date",
    +   "articles_list_content_blocks_template" : "div.curpane",
     +  "article_link_template" : "h3 a",
      + "date_template" : "%Y-%m-%d",
      # "pages_template" : "div.col-12",
      + "article_title_template" : "h1.entry-title",
      + "article_publication_datetime" : "time.published.dateline",
      + "article_text_template" : "div.text",
       +"tags_template2" : "div.tags", 
      + "tags_template": "div.news_by_theme",
   },
    "www.gordonua.com"{
        "articles_list_by_day_template" : "http://gordonua.com/html/newsitemap/%Y-%m/{date}.html",
        "articles_list_content_blocks_template" : "body",
       ? "article_link_template" :"body.ul.remove() a", ?
        "date_template" : "%Y-%m-%d",
        # "pages_template" : "div.col-12",
        "article_title_template" : "h1.a_head.flipboard-title",
        "article_publication_datetime" :"div.a_footer time.flipboard-date",
        "article_text_template" :"div.block.article",
        #"tags_template2" : "", 
       "tags_template": "div.tags.flipboard-endArticle"
    },
    "www.unian.ua"{
        "articles_list_by_day_template" : " https://www.unian.ua/news/archive/{date}",
        "articles_list_content_blocks_template" : "div.publications-archive",
        "article_link_template" : "a.publication-title",
        "date_template" : "%Y%m%d", 
        #"pages_template" : "div.pagination ul.pages li:last",
        "article_title_template" : "h1",
        "article_publication_datetime" : "div.item.time.no-padding",
        "article_text_template" : "div.article-text",
        "tags_template2" : "div.mp-level.main-menu",
        #"tags_template": "meta[name=keywords]",
        #"news_keywords": "meta[name=news_keywords]"
    },
    "www.comments.ua"{
        "articles_list_by_day_template" : "https://comments.ua/archive/{date}/",
        "articles_list_content_blocks_template" : "div.archive_feed_box",
        "article_link_template" : "a.link_search_result_title",
        "date_template" : "%Y-%m-%d",
        #"pages_template" : "div.pagination ul.pages li:last",
        "article_title_template" : "h1.text_news_header_text",
        "article_publication_datetime" : "p.text_news_header_date",
        "article_text_template" : "div.news_content_box",
       "tags_template2" : "p.text_news_source",
       # "tags_template": "meta[name=keywords]",
       # "news_keywords": "meta[name=news_keywords]"
    },
    "www.112.ua"{
        "articles_list_by_day_template" :  "https://112.ua/archive?date_from={date}-10&date_to={date}",
        "articles_list_content_blocks_template" : "ul.news-list",
        "article_link_template" : "li p a",
        "date_template" : "%Y-%m-%d",
        "pages_template" : "ul.pagination",
        "article_title_template" : "h1.itemprop",
        "article_publication_datetime" : "div.meta-info div.time",
        "article_text_template" : "div.article-text",
        "tags_template2" : "div.article-tags",
        #"tags_template": "meta[name=keywords]",
        #"news_keywords": "meta[name=news_keywords]" 
    },
    "www.gazeta.ua"{
        "articles_list_by_day_template" : "https://gazeta.ua/news/{date}#100/",
        "articles_list_content_blocks_template" : "div.news-wrapper",
        "article_link_template" : "a.news-title.block.black.fs16.mb5",
        "date_template" : "%Y-%m-%d",
       # "pages_template" : "div.pagination ul.pages li:last",
        "article_title_template" : "article h1",
        "article_publication_datetime" : "div.pull-right.news-date",
        "article_text_template" : "section.article-content.clearfix",
       #"tags_template2" : "div.tag a",
       #"tags_template": "meta[name=keywords]",
       #"news_keywords": "meta[name=news_keywords]"
    },
    "wwww.fakty.ua"{
        "articles_list_by_day_template" : "http://fakty.ua/archive/index?d={date}&ArticlesItem_page={page_number}",
        "articles_list_content_blocks_template" : "div.items",
        "article_link_template" : "a.tit",
        "date_template" : "%Y%m%d",
        "pages_template" : "div.pager ul li:last",
        "article_title_template" : "div.zag3 h1",
        "article_publication_datetime" : "span.g-gate",
        "article_text_template" : "div#article_content3",
        #"tags_template2" : "div.tag a",
        #"tags_template": "meta[name=keywords]",
        #"news_keywords": "meta[name=news_keywords]"
    },
    "www.kp.ua"{
        "articles_list_by_day_template" : "https://kp.ua/archive/{date}/",
        "articles_list_content_blocks_template" : "ul.news-online.news-per-day",
        "article_link_template" : "ul.news-online.news-per-day li a",
        "date_template" : "%Y/%B/%d",
       #"pages_template" : "div.pagination ul.pages li:last",
        "article_title_template" : "div.content-img__main h1",
        "article_publication_datetime" : "a.meta__date",
        "article_text_template" : "div.content",
        "tags_template2" : "div.related__title a",
        #"tags_template": "meta[name=keywords]",
        #"news_keywords": "meta[name=news_keywords]"
    },
    "zn.ua":
   {
       "articles_list_by_day_template" : "https://zn.ua/all-news/?page={page_number}&date={date}",
       "articles_list_content_blocks_template" : "div.left_news_list.wide ul.news_list", 
       "article_link_template" : "div.left_news_list.wide a.news_link",
       "date_template" : "%Y-%m-%d",
       "pages_template" : "div.navigate a.page",
       "article_title_template" : "h1.title",
       "article_publication_datetime" : "div.central_article .date",
       "article_text_template" : "div.article_body .text p",
       #"tags_template2" : "div.keywords_block", #loop through a
       "tags_template": ".hashtags a",
   },
    "podrobnosti.ua":
   {
       "articles_list_by_day_template" : "https://podrobnosti.ua/all/archive/{date}/all/page{page_number}/",
       "articles_list_content_blocks_template" : "div.news-list.news-table",
       "article_link_template" : "div.news-list.news-table a",
       "date_template" : "%Y/%m/%d",
       "pages_template" : "ul.pagination",
       "article_title_template" : "div.print_container h1",
       "article_publication_datetime" : "div.print_container span.date",
       "article_text_template" : "div#article_content p",
       #"tags_template2" : "div.keywords_block", #loop through a
       "tags_template": ".tags a",
   }
}


