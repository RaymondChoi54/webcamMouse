var base_zoom = 1;
var cur_zoom = base_zoom;
document.documentElement.style.zoom = base_zoom;

var height = '120px';
var iframe = document.createElement('div');
var sw=0;
// iframe.src = chrome.extension.getURL('toolbar.html');
/*iframe.style.height = height;
iframe.style.width = '100%';
iframe.style.position = 'absolute';
iframe.style.top = '0';
iframe.style.left = '0';
iframe.style.zIndex = '938089'; // Some high value
iframe.background = 'yellow';*/

var btn = document.createElement("BUTTON");
btn.setAttribute("id","acc-btn-1");
btn.setAttribute("class","btn btn-default btn-circle btn-xl");
btn.setAttribute("style", "	font-size:20px;font-family: inherit;border: 1px solid transparent;color: #FFF;background-color: #0095ff;border-color: #07c;box-shadow: inset 0 1px 0 #66bfff;position: fixed;left: 0; top: 0;");
btn.style.zIndex="100";
var t = document.createTextNode("NEW TAB");
btn.appendChild(t);
btn.onclick = function(){window.open('http://www.google.com', '_blank');};

iframe.appendChild(btn);

var btn2 = document.createElement("BUTTON");
btn2.setAttribute("id","acc-btn-2");
btn2.setAttribute("class","btn btn-default btn-circle btn-xl");
btn2.setAttribute("style", "	font-size:20px;font-family: inherit;border: 1px solid transparent;color: #FFF;background-color: #0095ff;border-color: #07c;box-shadow: inset 0 1px 0 #66bfff;position: fixed;left: 0; bottom: 0;");
btn2.style.zIndex="100";
var t2 = document.createTextNode("ZOOM IN");
btn2.appendChild(t2);
btn2.onclick = function(){
	document.documentElement.style.zoom = cur_zoom + 0.1;
	cur_zoom += 0.1;
};

iframe.appendChild(btn2);

var btn3 = document.createElement("BUTTON");
btn3.setAttribute("id","acc-btn-3");
btn3.setAttribute("class","btn btn-default btn-circle btn-xl");
btn3.setAttribute("style", "	font-size:20px;font-family: inherit;border: 1px solid transparent;color: #FFF;background-color: #0095ff;border-color: #07c;box-shadow: inset 0 1px 0 #66bfff;position: fixed;right: 0; bottom: 8px;");
btn3.style.zIndex="100";
var t3 = document.createTextNode("ZOOM OUT");
btn3.appendChild(t3);
btn3.onclick = function(){
	document.documentElement.style.zoom = cur_zoom - 0.1;
	cur_zoom -= 0.1;
};

iframe.appendChild(btn3);

var btn4 = document.createElement("BUTTON");
btn4.setAttribute("id","acc-btn-4");
btn4.setAttribute("class","btn btn-default btn-circle btn-xl");
btn4.setAttribute("style", "	font-size:20px;font-family: inherit;border: 1px solid transparent;color: #FFF;background-color: #0095ff;border-color: #07c;box-shadow: inset 0 1px 0 #66bfff;position: fixed;right: 0; top: 0;");
btn4.style.zIndex="100";
var t4 = document.createTextNode("RESET");
btn4.appendChild(t4);
btn4.onclick = function(){
	document.documentElement.style.zoom = base_zoom;
	cur_zoom = base_zoom;
};

iframe.appendChild(btn4);

var btn5 = document.createElement("BUTTON");
btn5.setAttribute("id","acc-btn-5");
btn5.setAttribute("class","btn btn-default btn-circle btn-xl");
btn5.setAttribute("style", "	font-size:20px;font-family: inherit;border: 1px solid transparent;color: #FFF;background-color: #0095ff;border-color: #07c;box-shadow: inset 0 1px 0 #66bfff;position: fixed;right: 50%; top: 0;");
btn5.style.zIndex="100";
var t5 = document.createTextNode("Go Back");
btn5.appendChild(t5);
btn5.onclick = function(){
	window.history.back();
};

iframe.appendChild(btn5);

var btn6 = document.createElement("BUTTON");
btn6.setAttribute("id","acc-btn-6");
btn6.setAttribute("class","btn btn-default btn-circle btn-xl");
btn6.setAttribute("style", "	font-size:20px;font-family: inherit;border: 1px solid transparent;color: #FFF;background-color: #0095ff;border-color: #07c;box-shadow: inset 0 1px 0 #66bfff;position: fixed;right: 50%; bottom: 0;");
btn6.style.zIndex="100";
btn6.innerHTML="Hide";
btn6.onclick = function(){
	if(sw==0){
		sw=1;
		document.getElementById("acc-btn-6").innerHTML="Show";
		for(var i=1;i<=5;i++){
			document.getElementById("acc-btn-"+i).remove();
		}

	}
	else{
		sw=0;
		document.getElementById("acc-btn-6").innerHTML="Hide";
		iframe.appendChild(btn);
		iframe.appendChild(btn2);
		iframe.appendChild(btn3);
		iframe.appendChild(btn4);
		iframe.appendChild(btn5);
	}
};

iframe.appendChild(btn6);

// Etc. Add your own styles if you want to
document.documentElement.appendChild(iframe);

//continuing add-toolbar.js
var bodyStyle = document.body.style;
var cssTransform = 'transform' in bodyStyle ? 'transform' : 'webkitTransform';
bodyStyle[cssTransform] = 'translateY(' + height + ')';
