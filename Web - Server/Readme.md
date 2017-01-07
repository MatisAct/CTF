### HTML: http://challenge01.root-me.org/web-serveur/ch1/
password:nZ^&@q5&sjJHev0
 
 câu này rất chuối: chỉ cần coi source :
<img src="http://image.prntscr.com/image/63e72e1d796a471d8628fe9d6971da97.png">


### Weak password:http://challenge01.root-me.org/web-serveur/ch3/
password:`admin` : cái bài củ chuối này , chỉ ngồi đoán pass thôi ! sau chục phút đoán thì cái pass sida là admmin.Hướng giải : đoán mò :))

### HTTP directory indexing:http://challenge01.root-me.org/web-serveur/ch4/
password:`LINUX`

- đầu phải đọc gợi ý , gợi ý là cây thư mục . Tiếp tục coi source:

<img src="http://image.prntscr.com/image/43dddb9bd582456b8fafafcdffff80a2.png">

thấy đoạn quan trọng :)) coppy đoạn đó dán vào url

<img src="http://image.prntscr.com/image/e9eec740e9ec4bcd973a859bdb0e934a.png">

đọc mấy dòng đó , trên url xóa đi đoạn pass.html ! thấy 1 cây thư mục , với nhiều thư mục tìm 1 lúc thấy ngay cái pass

<img src="http://image.prntscr.com/image/eaa7c9da904843139346c19855272beb.png">

### SQL injection - authentication:https://www.root-me.org/en/Challenges/Web-Server/SQL-injection-authentication
pass:`t0_W34k!$`
bài này mang tính chất ăn hên là nhiều :)) ! gợi ý của đề là, tìm ra pass của admin !
tham khảo tại http://securityidiots.com/Web-Pentest/SQL-Injection/bypass-login-using-sql-injection.html

bài này chỉ cần nhập , pass và username giống nhau theo dạng! `admin' or 1=0--` , lúc này hiện ra 1 bảng có username và pass , chỉ cần coi source là có pass! 
<img src="http://image.prntscr.com/image/bb9dcc0ef3844b76b7d939570c6f147e.png">
