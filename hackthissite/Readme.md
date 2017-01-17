https://www.hackthissite.org/missions/basic/

###Basic 1:https://www.hackthissite.org/missions/basic/1/
-password:`b87d5ccb`

- level này đơn giản , coi source là có password:
<img src="http://image.prntscr.com/image/637e7a6313224a1ba0545caaf808dd63.png">
###basic 3: https://www.hackthissite.org/missions/basic/2/
-pasword:`c6246e33`

- cách giải: đọc gợi ý , `This time Network Security Sam remembered to upload the password file, but there were deeper problems than that.` tác giả gợi ý  , họ đa tải lên tệp chứa password. muốn tìm tệp đó thì coi source 

<img src="http://image.prntscr.com/image/bf90377b084d4bceaf6c43e70846b514.png">

giờ thêm file đó vào cuối đoạn url là có password!

<img src="http://image.prntscr.com/image/026603d4c5824a1298062ab58967e9b6.png">

###Javascript Mission 1:https://www.hackthissite.org/missions/javascript/1/?lvl_password=cookies

- password: `cookies`
- chú ý đoạn js là được : cách hoạt động đoạn js nếu x=cookie thì win , nếu khác thì sai
<img src ="http://image.prntscr.com/image/0dcb6edbda1a4388a4963fcc55608bf7.png">


###Javascript Mission 3:https://www.hackthissite.org/missions/javascript/3/
password:`xxxxxxxxxxxxxx`
- hướng giải:nhìn đoạn js, giải toán đơn thuần tìm ra moo=14 , chú ý hàm x.length đếm số kí tự của x , nếu nó =moo thì win

```
function check(x)
{
        if (x.length == moo)
        {
                        alert("win!");
                        window.location += "?lvl_password="+x;
        } else {
                        alert("fail D:");
	 }
}
```
