<html>		
		<style>  
		form { width: 400px; position:fixed;left:30%; }
		label1 { float: left; width: 150px; }
		.clear { clear: both; height: 0; line-height: 0; }
		</style>
		<body>
		
		<form action="/select/search-update/artistResult/edit/done" method="get">
			<h2>Update Artist Information with id {{var1}}</h2>
			<hr></hr>
			<label1 for="name">Name:</label1><input name="name" type="text" value="{{var2}}" /><br>
			<label1 for="surname">Surname:</label1><input name="surname" type="text" value="{{var3}}" /><br>
			<label1 for="year">Birth Year:</label1><input name="year" type="text" value="{{var4}}" /><br>
			<input type="hidden" name="code" value={{var1}} />
			<input value="Update Information" type="submit" style="width: 150px; position:fixed; left:38%" /><br>
			
			<hr></hr>
		</form>
</html>