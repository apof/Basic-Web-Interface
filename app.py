from bottle import get, post, request,run,route,template,TEMPLATE_PATH # or route
from imp import reload
import os
import settings

# -*- coding: utf-8 -*-

# MySQL Connection
import pymysql
conn = pymysql.connect(host = settings.mysql_host,port = settings.mysql_port,user = settings.mysql_user,passwd = settings.mysql_passwd,db = settings.mysql_schema,charset = settings.mysql_charset)
cur = conn.cursor()

# Find Current Path for .tpl Files
TEMPLATE_PATH.insert(0,os.path.dirname(os.path.realpath(__file__)))

#Home Page
@get('/select') 	
def select():
	
    return template('select.tpl')

#Search And Update Artist Button	
@post('/select/search-update')
def search():
	return template('artist-input.tpl')
		
@get('/select/search-update/artistResult')
def artistResult():
	name = request.GET.getunicode('firstname')
	surname = request.GET.getunicode('surname')
	year_from = request.GET.getunicode('birthfrom')
	year_to = request.GET.getunicode('birthto')
	year_f = 0
	year_t = 0
	if len(year_from)>0 and year_from.isdigit(): 
		year_f = int(year_from)
	if len(year_to)>0 and year_to.isdigit(): 
		year_t = int(year_to)
	choice = request.GET.getunicode('type')
	query = choiceSelected(choice)
	if len(name)>0:
		query+=" and onoma='%s' " % (name)
	if len(surname)>0:
		query+=" and epitheto='%s' " % (surname)
	if year_f>1900:
		query+=" and etos_gen>=%d " % (year_f)
	elif len(year_from)>0:
		return template('artist-input_error.tpl')
	if year_t>1900:
		query+=" and etos_gen<=%d " % (year_t)
	elif len(year_to)>0:
		return template('artist-input_error.tpl')
	cur.execute(query)
	results=cur.fetchall()
	return template('show-artist-results.tpl',varr=results)
	
def choiceSelected(choice):
	query=""
	if(choice=="singer"):
		query = "SELECT distinct(ar_taut),onoma,epitheto,etos_gen FROM kalitexnis,singer_prod where tragoudistis=ar_taut"
	elif(choice=="song writer"):
		query = "SELECT distinct(ar_taut),onoma,epitheto,etos_gen FROM kalitexnis,tragoudi where stixourgos=ar_taut"
	elif(choice=="composer"):
		query = "SELECT distinct(ar_taut),onoma,epitheto,etos_gen FROM kalitexnis,tragoudi where sinthetis=ar_taut"
	return query
	
	
@get('/select/search-update/artistResult/edit')
def artistEdit():
	row = request.GET.getunicode('row_selected')
	code = row[2:9]
	x=[]
	x=row.split()
	name = x[1]
	y=""
	for char in name:
		if char!='\'' and char!=',':
			y+=char
	name=y
	surname = x[2]
	y=""
	for char in surname:
		if char!='\'' and char!=',':
			y+=char
	surname=y
	date = x[3]
	date = date[0:4]
	return template('edit-artist.tpl',var1=code,var2=name,var3=surname,var4=date)
	
@get('/select/search-update/artistResult/edit/done')
def showUpdated():
	name = request.GET.getunicode('name')
	surname = request.GET.getunicode('surname')
	year = request.GET.getunicode('year')
	code = request.GET.getunicode('code')
	y=0
	if len(year)>0 and year.isdigit():
		y = int(year)
	if len(name)==0 or len(surname)==0 or len(year)==0:
		return template('edit-artist_error.tpl',var=code)
	elif y<=1900 or year.isdigit()==0:
		return template('edit-artist_error2.tpl',var=code)	
	else:
		cur.execute("UPDATE kalitexnis SET onoma=%s,epitheto=%s,etos_gen=%s where ar_taut=%s", (name,surname,year,code))
		cur.execute("SELECT * FROM kalitexnis where ar_taut=%s", (code))
		results=cur.fetchall()
		formatedResult=[]
		for char in results:
			for x in char:
				formatedResult.append(x)
		
		return template('''
			<head>		
			<style>  
			form { width: 400px; position:fixed;left:30%;}
			label1 { float: left; width: 150px; }
			select { text-align:center; }
			.clear { clear: both; height: 0; line-height: 0; }
			</style>
			</head>
			<body>
		
			<form action="/select/insertSong/update" method="get">
			<h2>Succefully Updated Artist!</h2>
			<br>
			{{var}}
			<hr></hr>
		''',var=formatedResult)


	
#Search Song Button
@post('/select/song')
def searchSong():
	return template('search-song.tpl')
	
@get('/select/song/show')
def showSongs():
	title = request.GET.getunicode('title')
	print(title)
	y = request.GET.getunicode('year')
	company = request.GET.getunicode('company')
	query ="select distinct(etaireia),titlos,etos_par from (tragoudi left join singer_prod on title=titlos) left join cd_production on cd=code_cd where 1=1"
	
	year = 1900
	if len(y)>0 and y.isdigit():
		year=int(y)
	if year>1900:
		query+="  and etos_par=%d" % (year)
	elif len(y)>0:
		return template('search-song_error.tpl')
	if len(company)>0:
		query+=" and etaireia='%s'" % (company)
	if len(title)>0:
		query+=" and titlos='%s'" % (title)
	
	cur.execute(query)
	results=cur.fetchall()
	formatedResults=[]
	for x in results:
		formatedResults.append(x)
	return template('search-song-results.tpl',var1=formatedResults)
	
#Insert Artist Button
@get('/select/insertArt')
def InsertArtist():
	return template('insert-artist.tpl')
	

@get('/select/insertArt/update')
def artistUpdate():
	id = request.GET.getunicode('id')
	name = request.GET.getunicode('name')
	surname = request.GET.getunicode('surname')
	birthyear = request.GET.getunicode('birthyear')
	if len(id)==0 or len(name)==0 or len(surname)==0 or len(birthyear)==0:
		return template('insert-artist_error')
	else:
		if len(id)==7 and id[0].isalpha() and id[1:7].isdigit() and id_already_exist(id)==0 :
			cur.execute("INSERT INTO kalitexnis (ar_taut,onoma,epitheto,etos_gen) VALUES (%s,%s,%s,%s)", (id,name,surname,birthyear))
			return '''
			<head>		
			<style>  
			form { width: 400px; position:fixed;left:30%;}
			label1 { float: left; width: 150px; }
			select { text-align:center; }
			.clear { clear: both; height: 0; line-height: 0; }
			</style>
			</head>
			<body>
		
			<form action="/select/insertArt" method="get">
			<h2>Succefully Inserted!</h2>
			<INPUT Type="submit" VALUE="Insert new">
			</form>
			</body>
			<hr></hr>
			'''
		elif id_already_exist(id)>0:
			return template('insert-artist_error3.tpl')
		else:	return template('insert-artist_error2.tpl')

def id_already_exist(id):
	cur.execute("select ar_taut from kalitexnis where ar_taut=%s",(id))
	result=cur.fetchall()
	return len(result)


#Insert Song Button
@get('/select/insertSong')
def InsertSong():
	cur.execute("select distinct(code_cd) from cd_production")
	code_cd=cur.fetchall()
	formatedCodes=[]
	for char in code_cd:
		for x in char:
			formatedCodes.append(x)
	
	cur.execute("select distinct(tragoudistis) from singer_prod")
	code_singer=cur.fetchall()
	formatedSingers=[]
	for char in code_singer:
		for x in char:
			formatedSingers.append(x)
		
	cur.execute("select distinct(sinthetis) from tragoudi")
	code_composer=cur.fetchall()
	formatedComposers=[]
	for char in code_composer:
		for x in char:
			formatedComposers.append(x)
			
	cur.execute("select distinct(stixourgos) from tragoudi")
	code_writer=cur.fetchall()
	formatedWriters=[]
	for char in code_writer:
		for x in char:
			formatedWriters.append(x)
	return template('insert-song.tpl',var1=formatedCodes,var2=formatedSingers,var3=formatedComposers,var4=formatedWriters)
	
@get('/select/insertSong/update')
def showSongsUpdated():
	title = request.GET.getunicode('title')
	y = request.GET.getunicode('year')
	cd=request.GET.getunicode('cd')
	singer = request.GET.getunicode('singer')
	composer = request.GET.getunicode('composer')
	songWriter = request.GET.getunicode('songwriter')
	year = 1900
	if y.isdigit():
		year = int(y)
		
	Codes = request.GET.getunicode('codes')
	Singers = request.GET.getunicode('singers')
	Composers = request.GET.getunicode('composers')
	Writers = request.GET.getunicode('song_writers')
	
#insert string values in lists
	formatedCodes=[]
	formatedSingers=[]
	formatedComposers=[]
	formatedWriters=[]
	f2 = len(Codes)
	
	if Codes[1]=='\'':
		i=2
		step=10
	else:
		i=1
		step=8
	while i<=f2:
		formatedCodes.append(Codes[i:i+6])
		i+=step
	f2 = len(Singers)
	i=2
	while i<=f2:
		formatedSingers.append(Singers[i:i+7])
		i+=11
	f2 = len(Composers)
	i=2
	while i<=f2:
		formatedComposers.append(Composers[i:i+7])
		i+=11
	
	f2 = len(Writers)
	i=2
	while i<=f2:
		formatedWriters.append(Writers[i:i+7])
		i+=11
		
	if len(title)==0 or len(y)==0:
		return template('insert-song_error.tpl',var1=formatedCodes,var2=formatedSingers,var3=formatedComposers,var4=formatedWriters)
	elif year<=1900 or y.isdigit()==0:
		return template('insert-song_error2.tpl',var1=formatedCodes,var2=formatedSingers,var3=formatedComposers,var4=formatedWriters)
	elif title_already_exist(title)!=0:
		return template('insert-song_error3.tpl',var1=formatedCodes,var2=formatedSingers,var3=formatedComposers,var4=formatedWriters)
	else:
		cur.execute("INSERT INTO tragoudi (titlos,sinthetis,etos_par,stixourgos) VALUES (%s,%s,%s,%s)", (title,composer,year,songWriter))
		cur.execute("INSERT INTO singer_prod (cd,tragoudistis,title) VALUES (%s,%s,%s)", (cd,singer,title))
		return'''
			<head>		
			<style>  
			form { width: 400px; position:fixed;left:30%;}
			label1 { float: left; width: 150px; }
			select { text-align:center; }
			.clear { clear: both; height: 0; line-height: 0; }
			</style>
			</head>
			<body>
		
			<form action="/select/insertSong" method="get">
			<h2>Succefully Inserted!</h2>
			<INPUT Type="submit" VALUE="Insert new">
			<hr></hr>
			'''
def title_already_exist(title):
	cur.execute("select titlos from tragoudi where titlos=%s",(title))
	result=cur.fetchall()
	return len(result)
	
run(host='localhost', port=settings.web_port, debug=True)



	
	




