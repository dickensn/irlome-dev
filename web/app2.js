/* still a work in progress */


var $ = jQuery;

function submitToAPI(e) {
       e.preventDefault();
       var URL = "https://9nzri28mzh.execute-api.us-east-1.amazonaws.com/test2";

/*       var photoupload = /^([\/\w-\.]+)?$/;
         if (!photoupload.test($("#photoupload").val())) {
             alert ("Please select a photo!");
             return;
         }
         */

      /* var photoupload = $("#photoupload").val();*/


       $.ajax({
         type: "POST",
         url : "https://9nzri28mzh.execute-api.us-east-1.amazonaws.com/test2",
         headers: {  'Access-Control-Allow-Origin': 'http://irlo.me' },
         data: $('#photoupload').attr('files'),
         processData: false,
         crossDomain: true,
         cache: false,
         contentType: 'multipart/form-data',


         success: function () {
           // clear form and show a success message
           alert("Success!");
           document.getElementById("submit-form").reset();
       location.reload();
         },
         error: function () {
           // show an error message
           alert("UnSuccessfull");
         }});
     }
