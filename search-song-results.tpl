<html>		
		<style>  
		form { width: 600px; position:fixed;left:30%;}
		label1 { float: left; width: 150px; }
		.clear { clear: both; height: 0; line-height: 0; }
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
		
		<form action="/select/show" method="post" >
		<h2>Show Search Results</h2>
		<hr></hr>
		<div class="scroll">
		<table style="width:100%">
		<tr>
		<th>Title</th>		
		<th>Production Year</th>
		<th>Company</th>
		</tr>
  		%for item1 in var1:
			<tr>
			<td>{{item1[1]}}</td>
			<td>{{item1[2]}}</td>
			<td>{{item1[0]}}</td>

			</tr>
		%end
		</table>
		</div>
		<hr></hr>
		</form>
		</body>
</html>