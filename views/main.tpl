<!doctype html>
<html>
  <head>
    <title>Raspi Camera</title>
  </head>
  <body>
   <h1>Raspi Camera</h1>
   <p><img src="static/snap.jpg" width="400"></p>
   <form action="drive" method="GET">
     Angle: <input id="rangebar" type="range" min="0" max="180" name="angle" value="{{angle}}" onchange="showValue(this.value)">
     <input id="rangeinput" name="angle" value="{{angle}}" size="3" onchange="showValue(this.value)">
     <input type="submit" value="Snap Photo">
     <script type="text/javascript">
	function showValue(newValue) {
		document.getElementById("rangeinput").value=newValue;
		document.getElementById("rangebar").value=newValue;
	}
     </script>
   </form>
  </body>
</html>
