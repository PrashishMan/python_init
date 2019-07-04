playList = {
	"title" : "Patagonia Bus",
	"Creator" : "Colt Steele",
	"Songs" : [
		{"title" : "Turn It on", "author" : ["Culture Abuse"], "album_name" : "Peach", "Duration" : "3:27"},
		{"title" : "Eating Hooks", "author" : ["Moderate", "plater23"], "album_name" : "Title2", "Duration" : "3:22"}
	]

}

for songs in playList.get("Songs"):
	print( f"Song Title : {songs['title']} author : {songs.get('author')} album name : {songs.get('album_name')} duration : {songs.get('Duration')}")