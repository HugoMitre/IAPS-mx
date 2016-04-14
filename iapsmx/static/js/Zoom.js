var Zoom = {
isIE :  navigator.appVersion.match(/MSIE/),
scale : 1,
properties : new Array("width", "left", "height", "top", "fontSize"),
resolutions : {
r1024X600:0.70,
r800X600:0.60,
r1024X768:0.65
},
attach : function(){
var r = "r"+screen.width+"X"+screen.height;
if(Zoom.resolutions[r] != null){
Zoom.scale = Zoom.resolutions[r];
}
if(Zoom.scale != 1){
var images = document.getElementsByTagName("img");
var maps = document.getElementsByTagName("map");
var css = document.styleSheets;
var i=0;
for(i=0;images && i<images.length;i++){
Zoom.imageScale(images[i]);
}
for(i=0;maps && i<maps.length;i++){
map = maps[i];
for(j=0;j<map.childNodes.length;j++){
area = map.childNodes[j];
if(String(area.nodeName).toUpperCase() == "AREA"){
Zoom.areaScale(area);
}
}
}
for(i=0; css && i<css.length;i++){
try{
var rule = Zoom.isIE ?css[i].rules:css[i].cssRules;
Zoom.cssScale(rule);
}catch(e){
//Algunos navegadores no permiten modificar ciertos CSS por cuestiones de seguridad
//se cacha la excepcion y se continua con el resto de los estilos
}
}
}
},
removePX : function(toRemove){
if(String(toRemove).toLowerCase().indexOf("px") >0){
return String(toRemove).substr(0, String(toRemove).length-2);
}
return null;
},
imageScale : function(image){
var w = (image.offsetWidth*Zoom.scale).toFixed(2);
var h = (image.offsetHeight*Zoom.scale).toFixed(2);
image.style.height = h+"px";
image.style.width = w+"px";
},
cssScale : function(cssRules){
for(var j=0;cssRules!=null && j<cssRules.length;j++){
for(var k=0;k<Zoom.properties.length;k++){
var name = Zoom.properties[k];
var size = Zoom.removePX(cssRules[j].style[name]);
if(size != null){
size*=Zoom.scale;
size = size.toFixed(2);
cssRules[j].style[name] = size+"px";
}
}
if(String(cssRules[j].selectorText).toLowerCase() == "#main"){
cssRules[j].style.left = "50%";
cssRules[j].style.marginLeft = -(document.getElementById("main").offsetWidth/2)+"px";
}
if(String(cssRules[j].selectorText).toLowerCase() == "#mainmenu"){
cssRules[j].style.left = "50%";
cssRules[j].style.marginLeft = -(document.getElementById("mainMenu").offsetWidth/2)+"px";
}
}
},
areaScale : function(area){
var coords = String(area.coords).split(",");
var strCoords = area.coords;
for(var i=0;coords!=null && i<coords.length;i++){
if(i==0){
strCoords = "";
}
coords[i] = (coords[i]*Zoom.scale).toFixed(0);
strCoords+=((strCoords.length>0?",":"")+coords[i]);
}
area.coords = strCoords;
}
}
