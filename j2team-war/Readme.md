## j2team-war: http://j2team-war.ghostclub.info/index.php/war

- giao diện : mọi flag đều nằm trong source của nó

<img src="http://image.prntscr.com/image/3740deda92b24453bf520e4313a796a5.png">

### Level 1: http://j2team-war.ghostclub.info/index.php/war/level/1

- flag :`122d8bd3f967b2cf1f78f86a568a32d8`
- hướng giải: củ chuối coi source là có 
<img src="http://image.prntscr.com/image/14112c11b1484abe8be9b2f2cd910a42.png">

### Level 2: http://j2team-war.ghostclub.info/index.php/war/level/2

-flag : `c9649fea5186c7a821eb8cc3557075afJ2TeaM`

<img src="http://image.prntscr.com/image/885be51529df4d0d9f328e6056e45066.png">
- đoạn code này `Password == 'c9649fea5186c7a821eb8cc3557075af' + x())` flag là đoạn trước+ 1 biến x tìm trong source

 -chú ý đoạn-vì nó có thể nằm trong đó: giờ phân tích đoạn code này:
```
	function x() {var j = String.fromCharCode(32);return 'Juno_okyo with love from J2TeaM'.split(j)['4'];}
```
