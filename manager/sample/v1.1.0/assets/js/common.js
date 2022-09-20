if ($(window).width() <= 400) {
  //My mobile specific code
  window.onload = function(){
 	document.getElementById('sidebarToggleTop').click();
 }
 
  input = document.getElementById("cmd-input")
  input.remove()

  var textarea = document.createElement("textarea");
  textarea.style.width = "100%"
  textarea.classList.add("text-dark");
  textarea.classList.add("cmd-input");
  textarea.setAttribute("rows", "10");
  textarea.setAttribute("rows", "10");
  container = document.getElementById("cmd-body")
  container.appendChild(textarea);

}


function setWidth(){
	body = document.getElementById("cmd-body")
	span = document.getElementById("cmd-path")
	bodyWidth = body.offsetWidth ;
 	spanWidth = span.offsetWidth;
 	document.getElementById("cmd-input").style.width = (bodyWidth-spanWidth-86) + "px";
 	console.log(bodyWidth-spanWidth + "px")
}
setWidth()



