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
        if (data.msg==0) {
          var welecome = '<h2>Welcome  ' + data.username + '</h2>'
          $("#welcome").html(welecome)
          $("#login").hide()
          $("#logout-button").toggle()
        }
        else{
            console.log("666")
            alert("InputError:please check your username or password!")
            $("#user").val("")
            $("#passwd").val("")
        }

      }

    }).done(function(data){
      console.log(data);
    });
   });

    $("#logout-button").click(function (){

    $.ajax({
      url: '/logout',
      type: "POST",
      contentType: "application/json",
      data: JSON.stringify({}),
      success: function(data){
          $("#welcome").html("")
          $("#login").toggle()
          $("#logout-button").hide()
          $("#user").val("")
          $("#passwd").val("")
      }

    }).done(function(data){
      console.log(data);
    });
   });


});



console.log('Yajing Huang');
console.log('1008239');
