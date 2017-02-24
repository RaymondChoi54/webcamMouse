var base_zoom = 1;
var cur_zoom = base_zoom;
document.documentElement.style.zoom = base_zoom;

var height = '120px';
var iframe = document.createElement('div');
// iframe.src = chrome.extension.getURL('toolbar.html');
iframe.style.height = height;
iframe.style.width = '100%';
iframe.style.position = 'fixed';
iframe.style.top = '0';
iframe.style.left = '0';
iframe.style.zIndex = '938089'; // Some high value
iframe.background = 'yellow';

var btn = document.createElement("BUTTON");
btn.setAttribute("style", "	font-size:20px;	font-style:italic;	font-weight:bold;	height: 100px;	width: 100px;	border-radius: 50%;	border: 1px solid red;");
var t = document.createTextNode("NEW TAB");
btn.appendChild(t);
btn.onclick = function(){window.open('http://www.google.com', '_blank');};

iframe.appendChild(btn);

var btn2 = document.createElement("BUTTON");
btn2.setAttribute("style", "	font-size:20px;	font-style:italic;	font-weight:bold;	height: 100px;	width: 100px;	border-radius: 50%;	border: 1px solid red;");
var t2 = document.createTextNode("ZOOM IN");
btn2.appendChild(t2);
btn2.onclick = function(){
	document.documentElement.style.zoom = cur_zoom + 0.1;
	cur_zoom += 0.1;
};

iframe.appendChild(btn2);

var btn3 = document.createElement("BUTTON");
btn3.setAttribute("style", "	font-size:20px;	font-style:italic;	font-weight:bold;	height: 100px;	width: 100px;	border-radius: 50%;	border: 1px solid red;");
var t3 = document.createTextNode("ZOOM OUT");
btn3.appendChild(t3);
btn3.onclick = function(){
	document.documentElement.style.zoom = cur_zoom - 0.1;
	cur_zoom -= 0.1;
};

iframe.appendChild(btn3);

var btn4 = document.createElement("BUTTON");
btn4.setAttribute("style", "	font-size:20px;	font-style:italic;	font-weight:bold;	height: 100px;	width: 100px;	border-radius: 50%;	border: 1px solid red;");
var t4 = document.createTextNode("RESET");
btn4.appendChild(t4);
btn4.onclick = function(){
	document.documentElement.style.zoom = base_zoom;
	cur_zoom = base_zoom;
};

iframe.appendChild(btn4);

// Etc. Add your own styles if you want to
document.documentElement.appendChild(iframe);

//continuing add-toolbar.js
var bodyStyle = document.body.style;
var cssTransform = 'transform' in bodyStyle ? 'transform' : 'webkitTransform';
bodyStyle[cssTransform] = 'translateY(' + height + ')';