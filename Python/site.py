
import requests
#res=requests.get("https://www.facebook.com/100003475272512")
request={"robots.txt","sitemap.xml","index.php","flag.txt","flag.php","index.txt",
"index.php.txt","index.html.txt","index.old","index.php.old","index.html.old",
"index.sav","index.php.sav","index.html.sav",
"index.save","index.php.save","index.html.save",
"index.bk","index.php.bk","index.html.bk",
"index.rar","index.php.rar","index.html.rar",
"index.7z","index.php.7z","index.html.7z",
"index.backup","index.php.backup","index.html.backup",
}

url=raw_input("We take a url:")


for i in request:
  res=requests.get(url+i)
  print i,res.status_code
