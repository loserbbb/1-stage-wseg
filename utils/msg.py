import requests

def send_msg(text, desp):
    url = "https://sc.ftqq.com/SCU45994T70a722abd7419375801ea659faf5d7d25c8245c719a8a.send?text={}&desp={}".format(text, desp)
    return requests.get(url)