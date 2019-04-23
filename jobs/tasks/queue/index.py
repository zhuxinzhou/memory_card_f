# -*- coding: utf-8 -*-
from config.DB import db
from appf import app
from common.models.queue import QueueList
import json,requests,datetime
from common.libs.helper import getCurrentDate
from common.libs.member.WeChatService import WeChatService

from common.models.Oauth_member_bind import OauthMemberBind
from common.models.Card import Card
from sqlalchemy import func

'''
python manager.py runjob -m queue/index
'''

class JobTask():
    def __init__(self):
        pass
    def run(self,params):
        list = QueueList.query.filter_by(status=-1, next_time=getCurrentDate())\
            .order_by( QueueList.id.asc() ).limit(1).all()
        for item in list:
            # if item.queue_name == "pay":
            self.handlePay( item )

            # item.status = 1
            item.updated_time = getCurrentDate()
            db.session.add( item )
            db.session.commit()

    def handlePay(self,item ):
        card_id = item.queue_name
        if not card_id:
            return False

        card_info = Card.query.filter_by(id=card_id).first()
        member_id  = card_info.member_id
        oauth_bind_info = OauthMemberBind.query.filter_by(member_id=member_id).first()
        if not oauth_bind_info:
            return False



        #更新销售总量

        key_1 = card_info.study_status
        keyword1_val = "艾宾浩斯记忆曲线第"+str(key_1)+"/7次复习"
        keyword2_val = str(card_info.card_name)
        keyword3_val = getCurrentDate()
        keyword4_val = "未完成"
        textID=card_info.id
        page = "/pages/fuxi/fuxi?textId=%s"%(textID)

        #发送模板消息
        target_wechat = WeChatService( )
        access_token = target_wechat.getAccessToken()
        headers = {'Content-Type': 'application/json'}
        url = "https://api.weixin.qq.com/cgi-bin/message/wxopen/template/send?access_token=%s"%access_token
        params = {
            "touser": oauth_bind_info.openid,
            "template_id":"fiI_mGWuXaItSt1USpvaoFiUpy0OBx-qvDoToXARDRo",
            "page": page,
            "form_id": card_info.fromid,
            "data": {
                "keyword1": {
                    "value": keyword1_val
                },
                "keyword2": {
                    "value": keyword2_val
                },
                "keyword3": {
                    "value": keyword3_val
                },
                "keyword4": {
                    "value": keyword4_val
                }
            }
        }

        r = requests.post(url=url, data= json.dumps( params ).encode('utf-8'), headers=headers)
        r.encoding = "utf-8"
        print(r.text)
        return True

