<html>		
<style>  
form { width: 400px; position:fixed;left:30%; }
label1 { float: left; width: 150px; }
.clear { clear: both; height: 0; line-height: 0; }
</style>

<body>
<form action="/select/search-update/artistResult" method="get accept-charset="utf8"">
<h2>Presentation of Artists</h2>
<hr></hr>
<label1 for="firstname">Name:</label1> <input name="firstname" type="text" /><br>
<label1 for="surname">Surname:</label1> <input name="surname" type="text" /><br>
<label1 for="birthfrom">Birth Year-from:</label1> <input name="birthfrom" type="text" /><br>
            <label1 for="birthto">Birth Year-to:</label1> <input name="birthto" type="text" /><br>
			Type:<br>
			<label1 for="type">	a)</label1>	<input value="singer" name="type" type="radio" checked="checked"> Singer<br>
			<label1 for="type">b)</label1>	<input value="song writer" name="type" type="radio"> Song Writer<br>
			<label1 for="type">	c)</label1>	<input value="composer" name="type" type="radio"> Composer<br>
            <input value="submit" type="submit" style="width: 150px; position:fixed; left:38%" /><br>
			<hr></hr>
        </form>
		</body>
</html