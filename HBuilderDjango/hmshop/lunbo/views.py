from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
import random

# Create your views here.

def lunbo(request):
    data = {"status": 0, "message": [
        {"id": 0, "url": "http://www.itcast.cn/subject/phoneweb/index.html", "image": "http://p4.zbjimg.com/task/2011-06/15/817810/4df8c99f97d14.jpg"},
        {"id": 1, "url": "http://www.itcast.cn/subject/phoneweb/index.html", "image": "http://hbimg.b0.upaiyun.com/7f003af8d08f2b4e874a12d4fdfb104f1a86dd0d2c88-Ot1Mbr_fw658"},
        {"id": 2, "url": "http://www.itcast.cn/subject/phoneweb/index.html", "image": "http://hbimg.b0.upaiyun.com/059e265ab33640251cbf8eae08ea64ee53dcec21339cc-kNnnqu_fw658"},
    ]}
    return JsonResponse(data)

def goodsList(request,id):
    if id>5:
        data = {
            "status": 0,
            "message": [

            ]
        }
    elif id==5:
        data = {
            "status": 0,
            "message": [
                {
                    "id": random.randint(10,10000000),
                    "title": "vivo 手机【大屏更爽哦】64G大内存 超越你和我",
                    "image_url": "https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=1389148820,1481325689&fm=26&gp=0.jpg",
                    "sell_price": "3000",
                    "market_price": "3500",
                    "quantity": 60
                }]}
    else:
        data = {
            "status": 0,
            "message": [
                {
                    "id": random.randint(10,10000000),
                    "title": "vivo 手机【大屏更爽哦】64G大内存 超越你和我",
                    "image_url": "https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=1389148820,1481325689&fm=26&gp=0.jpg",
                    "sell_price": "3000",
                    "market_price": "3500",
                    "quantity": 60
                },
                {
                    "id": random.randint(10,10000000),
                    "title": "oppo4G 手机【照亮你和我】128G大内存",
                    "image_url": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1586078688219&di=b96afbc3b69630e2ab95292518202e49&imgtype=0&src=http%3A%2F%2F08.imgmini.eastday.com%2Fmobile%2F20180107%2F20180107071420_5b54479a5c8758cd6494da1f33b49798_1.jpeg",
                    "sell_price": "3100",
                    "market_price": "3550",
                    "quantity": 60
                },
                {
                    "id": random.randint(10,1000000),
                    "title": "华为3G 手机【畅玩版】64G大内存",
                    "image_url": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1586078688225&di=d150601527af1399c1cc42b41672604d&imgtype=0&src=http%3A%2F%2Fbpic.588ku.com%2Felement_origin_min_pic%2F17%2F09%2F19%2F595b607573e287864f331b60a267463a.jpg",
                    "sell_price": "2000",
                    "market_price": "2200",
                    "quantity": 60
                },
                {
                    "id": random.randint(10,1000000),
                    "title": "荣誉P40 手机至尊版 国内首次上市",
                    "image_url": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1586078688225&di=fd78fe944fffdb05b053cf5b71076b52&imgtype=0&src=http%3A%2F%2Fimage.it168.com%2Fn%2F0x0%2F8%2F8258%2F8258050.jpg",
                    "sell_price": "3200",
                    "market_price": "3400",
                    "quantity": 60
                }, {
                    "id": random.randint(10,1000000),
                    "title": "iphone 4G 手机【黄金灰】64G大内存 畅玩",
                    "image_url": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1586078688224&di=65b3b338be15a401ab87221fd1a47bfc&imgtype=0&src=http%3A%2F%2Fm.97wyw.com%2Fimages%2F201609%2Fgoods_img%2F32854_P_1474358765303.jpg",
                    "sell_price": "2000",
                    "market_price": "2500",
                    "quantity": 60
                }, {
                    "id": random.randint(10,1000000),
                    "title": "iphone MAX 手机【畅玩版】64G大内存",
                    "image_url": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1586078688220&di=c292864fb4920060104327be672de039&imgtype=0&src=http%3A%2F%2Fpic6.58cdn.com.cn%2Fzhuanzh%2Fn_v1bkujjdycwadfsneaujga_750_0.jpg",
                    "sell_price": "2400",
                    "market_price": "2670",
                    "quantity": 60
                },
                {
                    "id": random.randint(10,1000000),
                    "title": "中兴4G 手机【双面屏】64G大内存",
                    "image_url": "https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=1389148820,1481325689&fm=26&gp=0.jpg",
                    "sell_price": "2700",
                    "market_price": "3300",
                    "quantity": 30
                },                {
                    "id": random.randint(10,1000000),
                    "title": "小米4G 手机【高清视频版】64G大内存",
                    "image_url": "https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=1389148820,1481325689&fm=26&gp=0.jpg",
                    "sell_price": "2700",
                    "market_price": "3300",
                    "quantity": 30
                }

            ]
        }
    return JsonResponse(data)

def getCategory(request):
    data={
        "status":0,
        "message":[
            {
                "id": 0,
                "title": "生活家居"
            },
            {
                "id": 1,
                "title": "吧里趣味"
            },
            {
                "id": 2,
                "title": "摄影设计"
            },
            {
                "id": 3,
                "title": "明星写真"
            },
            {
                "id": 4,
                "title": "时尚图形"
            },
            {
                "id": 5,
                "title": "趣味生活"
            },
            {
                "id": 10,
                "title": "那个屌丝"
            },
            {
                "id": 6,
                "title": "情趣用品"
            },
            {
                "id": 7,
                "title": "用了真好"
            },
            {
                "id": 8,
                "title": "装修设计"
            },
            {
                "id": 9,
                "title": "茶具杯具"
            }
        ]
    }
    return JsonResponse(data)

def categoryId(request,id):
    if id%3==0:
        data={
            "status":0,
            "message":[
                {
                    "id":0,
                    "image":"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1586100997701&di=fc29306f53d082cf0a6a617b361c3e8e&imgtype=0&src=http%3A%2F%2Fpic1.win4000.com%2Fwallpaper%2F1%2F57c66e1e37837.jpg",
                    "title":"猴哥猴哥 你真了不得 五行大圣压不住你变出个孙行者"
                },
                {
                    "id": 1,
                    "image": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1586100997701&di=fc29306f53d082cf0a6a617b361c3e8e&imgtype=0&src=http%3A%2F%2Fpic1.win4000.com%2Fwallpaper%2F1%2F57c66e1e37837.jpg",
                    "title": "猴哥猴哥 你真了不得 五行大圣压不住你变出个孙行者"
                },
                {
                    "id": 2,
                    "image": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1586100997701&di=fc29306f53d082cf0a6a617b361c3e8e&imgtype=0&src=http%3A%2F%2Fpic1.win4000.com%2Fwallpaper%2F1%2F57c66e1e37837.jpg",
                    "title": "猴哥猴哥 你真了不得 五行大圣压不住你变出个孙行者"
                },
                {
                    "id": 3,
                    "image": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1586100997701&di=fc29306f53d082cf0a6a617b361c3e8e&imgtype=0&src=http%3A%2F%2Fpic1.win4000.com%2Fwallpaper%2F1%2F57c66e1e37837.jpg",
                    "title": "猴哥猴哥 你真了不得 五行大圣压不住你变出个孙行者"
                }
            ]
        }
    elif id%3==1:
        data = {
            "status": 0,
            "message": [
                {
                    "id":0,
                    "image":"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1586101174677&di=2c6706199a41c85fd8ee323644ada19d&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201511%2F28%2F20151128182741_Mywkf.png",
                    "title":"曾经有一个女孩站在厕所里我没有打她，当她拉裤裆里时后悔莫及"
                },
                {
                    "id": 1,
                    "image": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1586101174677&di=2c6706199a41c85fd8ee323644ada19d&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201511%2F28%2F20151128182741_Mywkf.png",
                    "title": "曾经有一个女孩站在厕所里我没有打她，当她拉裤裆里时后悔莫及"
                },
                {
                    "id": 2,
                    "image": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1586101174677&di=2c6706199a41c85fd8ee323644ada19d&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201511%2F28%2F20151128182741_Mywkf.png",
                    "title": "曾经有一个女孩站在厕所里我没有打她，当她拉裤裆里时后悔莫及"
                },
                {
                    "id": 3,
                    "image": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1586101174677&di=2c6706199a41c85fd8ee323644ada19d&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201511%2F28%2F20151128182741_Mywkf.png",
                    "title": "曾经有一个女孩站在厕所里我没有打她，当她拉裤裆里时后悔莫及"
                },
            ]
        }
    else:
        data = {
            "status": 0,
            "message": [
                {
                    "id":0,
                    "image":"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1586101174675&di=b0ea32e4d9a06bc6337865daa6b97039&imgtype=0&src=http%3A%2F%2Fa.hiphotos.baidu.com%2Fzhidao%2Fpic%2Fitem%2Fadaf2edda3cc7cd92d82d6b73b01213fb80e9135.jpg",
                    "title":"白云 黑土 大地 我的青春 我的梦 还有我那袜子没有洗"
                },
                {
                    "id": 1,
                    "image": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1586101174675&di=b0ea32e4d9a06bc6337865daa6b97039&imgtype=0&src=http%3A%2F%2Fa.hiphotos.baidu.com%2Fzhidao%2Fpic%2Fitem%2Fadaf2edda3cc7cd92d82d6b73b01213fb80e9135.jpg",
                    "title": "白云 黑土 大地 我的青春 我的梦 还有我那袜子没有洗"
                },
                {
                    "id": 2,
                    "image": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1586101174675&di=b0ea32e4d9a06bc6337865daa6b97039&imgtype=0&src=http%3A%2F%2Fa.hiphotos.baidu.com%2Fzhidao%2Fpic%2Fitem%2Fadaf2edda3cc7cd92d82d6b73b01213fb80e9135.jpg",
                    "title": "白云 黑土 大地 我的青春 我的梦 还有我那袜子没有洗"
                }
            ]
        }
    return JsonResponse(data)

def getgouwu(request,id):
    data={
        "status":0,
        "message":[
            {"src": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1586078688225&di=d150601527af1399c1cc42b41672604d&imgtype=0&src=http%3A%2F%2Fbpic.588ku.com%2Felement_origin_min_pic%2F17%2F09%2F19%2F595b607573e287864f331b60a267463a.jpg"},
            {"src": "https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=1389148820,1481325689&fm=26&gp=0.jpg"},
            {"src": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1586078688219&di=b96afbc3b69630e2ab95292518202e49&imgtype=0&src=http%3A%2F%2F08.imgmini.eastday.com%2Fmobile%2F20180107%2F20180107071420_5b54479a5c8758cd6494da1f33b49798_1.jpeg"},
    ]
    }
    return JsonResponse(data)
