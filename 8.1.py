import re


def mail_parsed(adress):
    re_mail = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]=\.\w+)', re.IGNORECASE)
    if not re_mail.match(adress):
        raise ValueError(f'wrong mail: {adress}')
    print(re_mail.match(adress).groupdict())

    for i in ['someone@geekbrains.ru', 'someone@geekbrainsru']:
        try:
            mail_parsed(i)
        except ValueError as ERR:
            print(ERR)
