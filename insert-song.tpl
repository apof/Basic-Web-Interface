<html>		
		<style>  
		form { width: 400px; position:fixed;left:30%;}
		label1 { float: left; width: 150px; }
		.clear { clear: both; height: 0; line-height: 0; }
		</style>
		<body>
		
		<form action="/select/insertSong/update" method="get">
			<h2>Insert Song</h2>
			<hr></hr>
			<label1 for="title">Title:</label1> <input name="title" type="text" /><br>
			<label1 for="year">Production Year:</label1> <input name="year" type="text" /><br>
			<label1 for="cd">CD:</label1>
			<select id="cd" name="cd">
			%for item in var1:
				<option value="{{item}}">{{item}}</option>
			%end
            </select><br>
			<label1 for="singer">Singer:</label1>
			<select id="singer" name="singer">
            %for item in var2:
				<option value="{{item}}">{{item}}</option>
			%end
            </select><br>
			<label1 for="composer">Composer:</label1>
			<select id="composer" name="composer">
			%for item in var3:
				<option value="{{item}}">{{item}}</option>
			%end
            </select><br>
			<label1 for="song writer">Song Writer:</label1>
			<select id="song writer" name="songwriter">
            %for item in var4:
				<option value="{{item}}">{{item}}</option>
			%end
            </select><br>
			<input type="hidden" name="codes" value="{{var1}}">
			<input type="hidden" name="singers" value="{{var2}}">
			<input type="hidden" name="composers" value="{{var3}}">
			<input type="hidden" name="song_writers" value="{{var4}}">
			<input value="submit" type="submit" style="width: 150px; position:fixed; left:38%" /><br>
			<hr></hr>
		</form>
		</body>
</html>