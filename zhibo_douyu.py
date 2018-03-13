import urllib.request
import re
import time
import pymysql
import datetime


baseurl="https://www.douyu.com/directory/game/"
#爬取目录
def opener(url):
    headers = ("User-Agent",
               "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36")
    # proxy = urllib.request.ProxyHandler({"http": proxy_addr})
    opener = urllib.request.build_opener()  # 代理参数proxy,urllib.request.HTTPHandler
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read()
    data = data.decode('UTF-8', 'ignore')
    return data
def mulu(url):
    try:
        # 浏览器伪装
        data=opener(url)
        #正则
        pat='/directory/game/(.*?)"'
        mulunum=re.compile(pat).findall(data)
        return mulunum

    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
#爬取link
def douyu(url):
    try:
        data=opener(url)
        #正则
        pat1 = 'dy-name ellipsis fl">(.*?)</span>' #id
        pat2 = 'class="ellipsis">.*?\r\n (.*?)</h3>' #title
        pat3 = 'dy-num fr.*?>(.*?)</span>' #js
        pat4 = 'play-list-link.*? href="/(.*?)"'#link
        pat5='tag ellipsis">(.*?)</span>'#game
        id = re.compile(pat1).findall(data)
        title = re.compile(pat2,re.S).findall(data)
        for i in range(0,len(title)):
            title[i]=title[i].strip()
        js = re.compile(pat3).findall(data)
        for j in  range(0,len(js)):
            if (re.compile("万").findall(js[j])):
                js[j] = js[j].replace("万", "0000")
                js[j] = js[j].replace(".", "")
        link = re.compile(pat4,re.S).findall(data)
        game = re.compile(pat5).findall(data)
        num=min(len(id),len(title),len(js),len(link))
        now= datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
           conn= pymysql.connect(host="localhost", user="root",password="pljc8833", db="zhibo", charset="utf8")
           for i in range(0,num):
               sid=pymysql.escape_string(id[i])
               stitle=pymysql.escape_string(title[i]).strip()
               sjs=pymysql.escape_string(js[i])
               slink=pymysql.escape_string(link[i])
               slink="https://www.douyu.com/"+slink
               sgame=pymysql.escape_string(game[i])
               sql="""INSERT INTO douyu_link(id,title,js,game,link,time) VALUES("%s","%s","%s","%s","%s","%s")""" % (sid,stitle,sjs,sgame,slink,now)
               conn.query(sql)
               #print("正在爬取分区："+sgame+"第"+str(i+1)+"主播")
        except Exception as e:
           raise e
        finally:
            conn.close()


    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return link
#斗鱼很难提取订阅量
'''
def zhubo(url):
    data=opener(url)
    pat1='<h2.*?>(.*?)</h2>'#title
    pat2='id="activityCount">(.*?)</div>'#count
    pat3='host-name.*?>(.*?)</h3>'#id
    pat4='display: inline;">(.*?)</h3>'#game
    title=re.compile(pat1).findall(data)
    count=re.compile(pat2).findall(data)
    id=re.compile(pat3).findall(data)
    game=re.compile(pat4).findall(data)
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(count)
    try:
        conn = pymysql.connect(host="localhost", user="root", password="pljc8833", db="huya", charset="utf8")
        sid = pymysql.escape_string(id[0])
        stitle = pymysql.escape_string(title[0])
        scount= pymysql.escape_string(count[0])
        sgame= pymysql.escape_string(game[0])
        sql = """INSERT INTO zhubo(id,title,count,game,link,time) VALUES("%s","%s","%s","%s","%s","%s")""" % (sid, stitle,scount,sgame ,url, now)
        #conn.query(sql)
        print("正在爬取分区："+sgame+"第" + str(i+1) + "名主播")
        #print("values('"+sid+"','"+stitle+"','"+scount+"','"+url+"','"+now+"'\n")
    except Exception as e:
        raise e
    finally:
        conn.close()

'''
#爬取目录
classify=mulu( "https://www.douyu.com/directory/")
print("爬取目录成功一共有"+str(len(classify))+"个分区\n是否开始爬取页面[Y/N]")
start=input()
if(start=="Y" or start=="y"):
    #爬取页面
    for ci in range(0,len(classify)):
        url=baseurl+classify[ci]
        mydata=douyu(url)
        print("正在爬取分区："+classify[ci]+"共"+str(len(mydata))+"名主播")
    print("爬虫结束")
else:
    print("再见")






