//JS to setup the view on the homepage


nav = function() {

};

about = function() {

	var tag = document.getElementById("section1");
	var heading = document.createElement("H4");
	var txt = document.createTextNode("About");
	heading.appendChild(txt);
	tag.appendChild(heading);

};

demo = function () {

	var tag = document.getElementById("section2");
	var heading = document.createElement("H4");
	var txt = document.createTextNode("Demo");
	heading.appendChild(txt);
	tag.appendChild(heading);

};

download = function() {

	var tag = document.getElementById("section3");
	var heading = document.createElement("H4");
	var txt = document.createTextNode("Download");
	heading.appendChild(txt);
	tag.appendChild(heading);

	var txt = "Download (.zip)";
	var tag1 = document.getElementById("section3");
	let button = document.createElement("BUTTON");
	button.id = txt;
	var text = document.createTextNode(txt);
	button.appendChild(text);
	//event listener
    button.addEventListener("click", function () {
		
    	//AJAX call, used link: http://www.w3schools.com/xml/ajax_intro.asp
    	//var data;
    	//var xhttp = new XMLHttpRequest();
    	//xhttp.onreadystatechange = function() {
  		//	if (this.readyState == 4 && this.status == 200) {
    	//		data = JSON.parse(xhttp.responseText);
    	//
  		//	}
  		//}
    	//xhttp.open("GET", "/applicants", true);
    	//xhttp.send();
    	alert("Download Started");
    });

    //add button to dom
	tag1.appendChild(button);

};

feedback = function() {
	
	var tag = document.getElementById("section4");
	var heading = document.createElement("H4");
	var txt = document.createTextNode("Feedback");
	heading.appendChild(txt);
	tag.appendChild(heading);

};

team = function() {

	var tag = document.getElementById("section5");
	var heading = document.createElement("H4");
	var txt = document.createTextNode("Meet The Team");
	heading.appendChild(txt);
	tag.appendChild(heading);

};

//Main
nav();
about();
demo();
download();
feedback();
team();