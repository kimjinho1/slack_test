import os
from slack_notifications import *

if __name__ == '__main__':
    SLACK_TOKEN = os.environ("SLACK_TOKEN")
    slack = Slack(SLACK_TOKEN)
    attachment = Attachment(
        # color = "#2eb886",
        # title = "너의 절친 에덴이 원붕이에게",
        # text = "나의 친구, 갤스 출첵 했어?",
        author_name = "너의 절친 에덴",
        author_icon = "https://i.pinimg.com/564x/76/de/01/76de01995777c76d2df7d5f597a73150.jpg",
        image_url = "https://ac-p2.namu.la/20220711sac/162ae7191c77dd11b27e1aff7e854dc75317f60870fc0bb79b4dcf8432f62099.png",
        thumb_url = "https://ac-p2.namu.la/20220711sac/162ae7191c77dd11b27e1aff7e854dc75317f60870fc0bb79b4dcf8432f62099.png",
        # footer = "불을 쫒는 나방",
        # footer_icon = "https://static.wikia.nocookie.net/hoducks/images/4/40/Fire_Moth.jpg/revision/latest?cb=20200901074934",
    )

    slack.send_notify(channel = "#app-test", 
                    icon_url= "https://ac-p2.namu.la/20220711sac/162ae7191c77dd11b27e1aff7e854dc75317f60870fc0bb79b4dcf8432f62099.png",
                    attachments=[attachment]
    )

