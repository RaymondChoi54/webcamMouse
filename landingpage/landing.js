var home = home || {};

home.init =function(){
  console.log("hi");
  jQuery.ajax({
    url: "/list",
    type: "GET",
    dataType: "json",
    contentType: "application/json; charset=utf-8",
    success: function(response) {
      var name=["but3","but4"];
      var id=["temp1","temp2"];
      console.log(response);
      if(response.length!=0){
        for(var i in response){
          document.getElementById(name[i]).removeChild(document.getElementById(id[i]));
          var tbutt=document.createElement("button");
          var tt=parseInt(i)+3;
          var cl = "w3-btn-block button"+tt;
          tbutt.setAttribute("class",cl);
          tbutt.innerHTML=response[i].name;
          tbutt.setAttribute("id",response[i].link);
          tbutt.onclick=function(){
            location.href=this.id;

        };
          document.getElementById(name[i]).appendChild(tbutt);
        }
      }
  }
});
}

home.init();
