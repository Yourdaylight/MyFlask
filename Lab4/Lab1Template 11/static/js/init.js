$(document).ready(function (){

    $("#get-button").click(function (){

      $.ajax({
        type: "GET",
        url: "/user",
        result:JSON.stringify({"name":name}),
        success: function(result){
          console.log("yes");
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

    var message = $("#message").val();
    var username=$("#username").val();
    alert(username);
    var password=$("#password").val();
    $.ajax({
      url: '/user',
      type: "POST",
      contentType: "application/json",
      data: JSON.stringify({"username":$("#username").val()}),
      success: function(result){
        console.log("yes");
        console.log(result);
        alert("success!");}

    }).done(function(data){
      console.log(data);
    });


   });


});



console.log('Yajing Huang');
console.log('1008239');
