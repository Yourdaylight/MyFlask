$(document).ready(function (){

    $("#get-button").click(function (){

      $.ajax({
        type: "GET",
        url: "/user",
        result:JSON.stringify({"name":name}),
        success: function(result){
          console.log("yes");
          console.log(name)
          alert("Getting infomation from the user");}
        });

   });

   $("#post-button").click(function (){

     $.ajax({
       type: "POST",
       url: "/user",
       result:JSON.stringify({"name":name}),

       success: function(result){
         console.log("yes");
         alert("Create infomation from the user");}
       });

  });

  $("#put-button").click(function (){

    $.ajax({
      type: "PUT",
      url: "/user1",
      result:JSON.stringify({"name":name}),

      success: function(result){
        console.log("yes");
        alert("Update infomation from the user");}
      });

 });

 $("#delete-button").click(function (){

   $.ajax({
     type: "DELETE",
     url: "/user1",
     result:JSON.stringify({"name":name}),

     success: function(result){
       console.log("yes");
       alert("Delete infomation from the user");}
     });
  });

  $("#submit-button").click(function (){

    $.ajax({
      url: '/user',
      type: "POST",
      contentType: "application/json",
      data: JSON.stringify({"username":$("#user").val(),"password":$("#passwd").val()}),
      success: function(data){
        console.log("yes");
        console.log(data);
        var LOGOUT="<h2>Welcome  "+data.username+ "</h2>"+"<a href=\"#\" id=\"put-button\" class=\"btn btn-lg btn-info\">logout</a>"
        $("#login").html(LOGOUT)
      }

    }).done(function(data){
      console.log(data);
    });
   });

    $("#submit-button").click(function (){

    $.ajax({
      url: '/user',
      type: "POST",
      contentType: "application/json",
      data: JSON.stringify({"username":$("#user").val(),"password":$("#passwd").val()}),
      success: function(data){
        console.log("yes");
        console.log(data);
        if (data.username) {
          var welecome = '<h2>Welcome  ' + data.username + '</h2>'
          var logout = '<a href="#" id="logout-button" >logout</a>'
          $("#login").html(welecome)
          $("#button-group").html(logout)
        }

      }

    }).done(function(data){
      console.log(data);
    });
   });

    $("#button-group").click(function (){

    $.ajax({
      url: '/logout',
      type: "POST",
      contentType: "application/json",
      data: JSON.stringify({}),
      success: function(data){
        console.log("yes");
      }
    })
   });

});



console.log('Yajing Huang');
console.log('1008239');
