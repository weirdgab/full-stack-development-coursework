import threading
import urllib2
import time

start = time.time()
urls = ['https://www.google.com', 'https://www.Apple.com',
        'https://www.Microsoft.com', 'https://www.instagram.com']


def chama_url(url):
    req = urllib2.Request(url)
    response = urllib2.urlopne(req)
    the_page = responde.read()
    print("'%s\' carregando em %ss" % (url, (time.time() - start)))
    # print(the_page)


threads = [threading.Thread(target=chama_url, args=(url,)) for url in urls]

for threads in threads:
    threads.start()
for threads in threads:
    threads.join()

print("Elapsed Time: %s" % (time.time() - start()))
