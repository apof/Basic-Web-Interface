<html>		
		<style>  
		form { width: 400px; position:fixed;left:30%;}
		label1 { float: left; width: 150px; }
		select { text-align:center; }
		.clear { clear: both; height: 0; line-height: 0; }
		</style>
		
		<body>
		<form action="/select/insertArt/update" method="get">
			<h2>Insert Artist</h2>
			<hr></hr>
			<label1 for="id">National Id:</label1> <input name="id" type="text" /><br>
			<label1 for="name">Name:</label1> <input name="name" type="text" /><br>
			<label1 for="surname">Surname:</label1> <input name="surname" type="text" /><br>
			<label1 for="birthyear">Birth Year</label1> <input type="number" name="birthyear" min="1900" max="2000"><br>
			<input value="Update Information" type="submit" style="width: 150px; position:fixed; left:38%" /><br>
			<hr></hr>
			<h3 style="color:red;">Please fill in all input fields</h3>
		</form>
		</body>
</html>