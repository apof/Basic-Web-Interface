<html>		
		<style>  
		form { width: 400px; position:fixed;left:30%;}
		label1 { float: left; width: 150px; }
		.clear { clear: both; height: 0; line-height: 0; }
		</style>
		
		<body>
		
		<form action="/select/song/show" method="get" accept-charset="utf8">
			<h2>Presentation of Songs</h2>
			<hr></hr>
			<label1 for="title">Song Title:</label1><input name="title" type="text" /><br>
			<label1 for="year">Production Year:</label1><input name="year" type="text" /><br>
			<label1 for="company">Company:</label1><input name="company" type="text" /><br>
			<input value="submit" type="submit" style="width: 150px; position:fixed; left:38%" /><br>
			<hr></hr>
			<h3 style="color:red;">Invalid Year</h3>
		</form>
		</body>
</html>