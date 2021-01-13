url = "https://www.naver.com/blog/travel/seoul.html"

els = url.split("://")
print(els[0])   # https
print(els[1])   # www.naver.com/blog/travel/seoul.html

path = els[1].split('/')
fname = path[-1]
print(fname)

