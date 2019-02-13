<html>		
		<style>  
		body {width: 400px; position:fixed;left:30%;}
		table, th, td {
		border: 1px solid black;
		border-collapse: collapse;
		}
		th, td {
		padding: 3px;
		}
		div.scroll {
    background-color: pink;
    width: 600px;
    height: 600px;
    overflow: scroll;
}

		</style>
		
		<body>
		
		<h2>View Artist Results</h2>
		<hr></hr>
		<div class="scroll">
		<table style="width:100%">
		<tr>
		<th>National ID</th>
		<th>Name</th>
		<th>Surname</th>		
		<th>BirthYear</th>
		<th>Edit</th>
		</tr>
  		%for item1 in varr:
			<tr>
			%for x in item1:
			<td>{{x}}</td>
			%end
			<td>		
			<form action="/select/search-update/artistResult/edit" method="get">
			<input value="Edit Me" type="submit" />
			<input type="hidden" name="row_selected" value="{{item1}}"></form>
			</td>
			</tr>
		%end
		</table>
		</div>
		<br><br><br><br><br><br>
		</body>
</html>