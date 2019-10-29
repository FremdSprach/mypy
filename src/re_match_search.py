"""
The difference between match and search in Python re module.
"""
from traceback import format_exc
from re import compile, match, search, split, sub


def main():
    # match method usage: match(pattern, string, [,flags]
    # return true if the beginning of string matches pattern,
    # return false otherwise.
    print(match('super', 'superstition').span())
    try:
        print(match('super', 'anti-superstition').span())
    except AttributeError as e:
        print(format_exc())

    # search method usage: search(pattern, string, [.flags]
    # return the first occurrence of pattern in string.
    print(search('super', 'superstition').span())
    print(search('super', 'anti-superstition').span())

    # match given string in a tag of an html class.
    html = '<a class="nation">China</a>'
    regexp = r'^.*\>(.*?)\<.*$'
    m = search(regexp, html)
    print(m.group(1))

    # one more example.
    resp = '404 not found TARGET and PREY'
    regexp = r'^([0-9a-z ]*)([A-Z]*)([0-9a-z ]*)([A-Z]*)$'
    m = search(regexp, resp)
    print(m.group(2), m.group(4))

    # re.compile
    target = '123abc'
    pattern = compile(r'.*[a-z]+')
    m = pattern.match(target)
    print(m.span())

    # re.sub
    record = 'score of Jimmy is 90.'
    print(sub('90', '100', record))

    # re split.
    entry = 'info:Anna 33 German'
    print(split(r'\W+', entry))

    # match email boxes ending with 163.com.
    email_boxes = [
        'foo@qq.com', 'bar@google.com',
        'foo@163.com', 'bar@sina.com',
        'foo@outlook.com', 'bar@163.com'
    ]
    for e in email_boxes:
        m = match(r'.*163\.com', e)
        if m is not None:
            print(e)


if __name__ == '__main__':
    main()
