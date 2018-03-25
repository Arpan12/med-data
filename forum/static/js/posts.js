function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var state=parseInt($("#upvote-btn1").attr("state"));
var upvotes=parseInt($("#upvote-btn1").attr("upvotes"));
var value=0;



$("#upvote-btn1").click(function(e){
	e.preventDefault();
	  
var csrftoken = getCookie('csrftoken'); 
	var this_=$(this);
	var csrf=$("#btn-txt").attr("csrf")
	var answer_id=this_.attr("answer_id");
	var username=this_.attr("user");
  


	$.ajax({
            url: '/users/'+username+'/forum/'+answer_id+'/like/',
            method:'POST',
            data: {
                   'csrfmiddlewaretoken': csrftoken
            },
            success: function(){
              if (state){
                console.log(state);
                if(value){               
                $("#button-txt").text("upvoted|"+(upvotes).toString());
                 value=0;
              }
              else{
                $("#button-txt").text("upvote|"+(upvotes-1).toString());                 
                 value=1;
                 
              }
            }
              else{
                console.log(state);

                if(value){
                $("#button-txt").text("upvote|"+(upvotes).toString());
                 value=0;
              }
              else{
                $("#button-txt").text("upvoted|"+(upvotes+1).toString());                 
                 value=1;
                 
              }
              }

              }
          });

});





$("#upvote-btn2").click(function(e){
  e.preventDefault();
var csrftoken = getCookie('csrftoken');


  console.log(11);
  var this_=$(this);
  var csrf=$("#btn-txt").attr("csrf")
  var answer_id=this_.attr("answer_id");
  var username=this_.attr("user");

  console.log(username);
  $.ajax({
            url: '/users/'+username+'/forum/'+answer_id+'/like/',
            method:'POST',
            data: {
                   'csrfmiddlewaretoken': csrftoken
            },
            success: function(){
              alert("upvoted");
              }
          });

});





