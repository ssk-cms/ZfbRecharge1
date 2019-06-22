import urllib.request
import json
import pymysql

id = '1226244970' #选取爬数据用户，打开微博用户首页，查看源代码，搜索oid,该值便是
# 本次选取的用户是吴京

proxy_addr = "183.129.207.82:11031"


def use_proxy(url, proxy_addr):
    req = urllib.request.Request(url)
    req.add_header(
        "User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
    proxy = urllib.request.ProxyHandler({'http': proxy_addr})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
    return data


def get_containerid(url):
    data = use_proxy(url, proxy_addr)
    content = json.loads(data).get('data')
    for data in content.get('tabsInfo').get('tabs'):
        if(data.get('tab_type') == 'weibo'):
            containerid = data.get('containerid')
    return containerid


def get_userInfo(id):
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value='+id
    data = use_proxy(url, proxy_addr)
    content = json.loads(data).get('data')
    profile_image_url = content.get('userInfo').get('profile_image_url')
    description = content.get('userInfo').get('description')
    profile_url = content.get('userInfo').get('profile_url')
    verified = content.get('userInfo').get('verified')
    guanzhu = content.get('userInfo').get('follow_count')
    name = content.get('userInfo').get('screen_name')
    fensi = content.get('userInfo').get('followers_count')
    gender = content.get('userInfo').get('gender')
    urank = content.get('userInfo').get('urank')
    # print(type(name),type(profile_url),type(profile_image_url),type(str(verified)),type(description),type(str(guanzhu)),type(str(fensi)),type(gender),type(str(urank)))
    print("微博昵称："+name+"\n"+"微博主页地址："+profile_url+"\n"+"微博头像地址："+profile_image_url+"\n"+"是否认证："+str(verified)+"\n" +
          "微博说明："+description+"\n"+"关注人数："+str(guanzhu)+"\n"+"粉丝数："+str(fensi)+"\n"+"性别："+gender+"\n"+"微博等级："+str(urank)+"\n")

    with open(name+".txt", 'a', encoding='utf-8') as fh:
        fh.write("微博昵称："+name+"\n"+"微博主页地址："+str(profile_url)+"\n"+"微博头像地址："+str(profile_image_url)+"\n"+"是否认证："+str(verified)+"\n" +
          "微博说明："+str(description)+"\n"+"关注人数："+str(guanzhu)+"\n"+"粉丝数："+str(fensi)+"\n"+"性别："+str(gender)+"\n"+"微博等级："+str(urank)+"\n")


    try:
        Conn = pymysql.connect(host="localhost", user="root", passwd="123456", db="weibo_data",
                               charset="utf8")
        Cur = Conn.cursor()
    except Exception as e:
        print('Failed to Get SQL!')
        exit(1)

    sql = "INSERT INTO weibo_user(name,home_address,img_address,active,abstract,concern_number,fans_number,sex,level) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    Cur.execute(sql,(name,profile_url,profile_image_url,str(verified),description,str(guanzhu),str(fensi),gender,str(urank)) )
    Conn.commit()

    print('成功插入', Cur.rowcount, '条数据')

    Cur.close()
    Conn.close()

    file = id+".txt"
    get_weibo_store(id,file,name)


# 获取微博内容信息,并保存到文本中，内容包括：每条微博的内容、微博详情页面地址、点赞数、评论数、转发数等

def get_weibo_store(id, file,name):
    i = 1
    Conn = pymysql.Connect(host="localhost", user="root", passwd="123456", db="weibo_data",
                           charset="utf8")
    Cur = Conn.cursor()
    while i<=50: #选取爬取多少页内容，可选
        url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value='+id
        weibo_url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=' + \
            id+'&containerid='+get_containerid(url)+'&page='+str(i)
        try:
            data = use_proxy(weibo_url, proxy_addr)
            print(data)
            content = json.loads(data).get('data')
            cards = content.get('cards')
            if(len(cards) > 0):

                for j in range(len(cards)):

                    card_type = cards[j].get('card_type')
                    if(card_type == 9):
                        mblog = cards[j].get('mblog')
                        attitudes_count = mblog.get('attitudes_count')
                        comments_count = mblog.get('comments_count')
                        created_at = mblog.get('created_at')
                        reposts_count = mblog.get('reposts_count')
                        scheme = cards[j].get('scheme')
                        text = mblog.get('text')
                        with open(file, 'a', encoding='utf-8') as fh:
                            fh.write("----第"+str(i)+"页，第" +
                                     str(j)+"条微博----"+"\n")
                            fh.write("微博地址："+str(scheme)+"\n"+"发布时间："+str(created_at)+"\n"+"微博内容："+text+"\n"+"点赞数："+str(
                                attitudes_count)+"\n"+"评论数："+str(comments_count)+"\n"+"转发数："+str(reposts_count)+"\n")


                        sql = "INSERT INTO weibo_user_message(username,address,time,text,zan_number,ping_number,zhuan_number) VALUES(%s,%s,%s,%s,%s,%s,%s)"
                        Cur.execute(sql,(name,str(scheme),str(created_at),text,str(
                                attitudes_count),str(comments_count),str(reposts_count)))
                        Conn.commit()


            else:
                break

        except Exception as e:
            print(e)
            pass
        i+=1
    Cur.close()
    Conn.close()

if __name__ == "__main__":
    get_userInfo(id)
    # get_weibo_store(id, file,name)
