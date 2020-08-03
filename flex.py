class Linebot:
    def flex(name, url, image):

        payload = {
            "type": "flex",
            "altText": "Flex Message",
            "contents": {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "image",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                        "type": "uri",
                        "label": "Line",
                        "uri": url
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": name,
                            "size": "xl",
                            "weight": "bold"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "margin": "lg",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "spacing": "sm",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "神げー攻略サイト",
                                            "flex": 1,
                                            "size": "sm",
                                            "color": "#AAAAAA"
                                        }
                                    ]
                                }
                            ]
                        }

                        #                 {
                        #                     "type": "text",
                        #                     "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
                        #                     "flex": 5,
                        #                     "size": "sm",
                        #                     "color": "#666666",
                        #                     "wrap": True
                        #                 }
                        #             ]
                        #         },
                        #         {
                        #             "type": "box",
                        #             "layout": "baseline",
                        #             "spacing": "sm",
                        #             "contents": [
                        #                 {
                        #                     "type": "text",
                        #                     "text": "Time",
                        #                     "flex": 1,
                        #                     "size": "sm",
                        #                     "color": "#AAAAAA"
                        #                 },
                        #                 {
                        #                     "type": "text",
                        #                     "text": "10:00 - 23:00",
                        #                     "flex": 5,
                        #                     "size": "sm",
                        #                     "color": "#666666",
                        #                     "wrap": True
                        #                 }
                        #             ]
                        #         }
                        #     ]
                        # }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "flex": 0,
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "spacer",
                            "size": "sm"
                        }
                    ]
                }
            }
        }
        return payload
