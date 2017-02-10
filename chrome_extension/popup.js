document.addEventListener('DOMContentLoaded', function() {

	document.getElementById("button_1").addEventListener("click", function(){
  		var ele = document.createElement("P");
  		ele.innerHTML="Hello World!";
  		document.getElementById("body").appendChild(ele);
	},false);

	document.getElementById("button_2").addEventListener("click", function(){
  		chrome.tabs.create({'url':'chrome://newtab', 'selected': true});
	},false);

},false);
