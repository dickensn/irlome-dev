var bucketName = 'irlo.me';
var bucketRegion = 'us-east-1';

AWS.config.update({
  region: bucketRegion
})
var s3 = new AWS.S3({
  apiVersion: '2006-03-01',
  params: {Bucket: bucketName}
});

function clickHandler() {
  alert("something");
}

function get_file_extension(filename){
  return filename.split('.').pop();
}

function addPhoto() {
  var files = document.getElementById('photoupload').files;
  if (!files.length) {
    return alert('Please choose a file to upload first.');
  }
  var file = files[0];
  var fileName = file.name;

/*  s3.upload({
    Key: photoKey,
    Body: file,
    ACL: 'public-read'
  }, function(err, data) {
    if (err) {
      return alert('There was an error uploading your photo: ', err.message, photoKey);
    }
    alert('Successfully uploaded photo.');
//    viewAlbum(albumName);
// add submit to API instead?
});*/

  var date = new Date();
  var timestamp = date.getTime();

  var extension = get_file_extension(fileName)

  var photoKey = "/photos/" + timestamp + "." + extension


  var params = {
  Body: file,
  Bucket: bucketName,
  Key: photoKey
 };
 //putObject
 s3.putObject(params, function(err, data) {
   if (err) console.log(err, err.stack); // an error occurred
   else     console.log(data);           // successful response
 });

 document.getElementById("submit").innerHTML="<div class=\"w3-cell w3-container\"> \
   <h3>Thanks</h3> \
   <p>Thank you for uploading a photo.</p> \
 </div> \
</div>";
 document.getElementById("form").innerHTML="  <div class=\"w3-cell w3-container\"> \
     <p>To see the data we have, please visit the map.</p> \
   </div>";
 }

 var upload_image = function(url,form,id) {
    var field = $(form).find('input[name=photo]');
    var file = field[0].files[0];
    var original_name = field.val();
    var extension = original_name.substr((original_name.lastIndexOf('.')));
    var filename = id + extension;

    var fd = new FormData();
    fd.append('key', filename);
    fd.append('acl', 'bucket-owner-full-control');
    fd.append('Content-Type', file.type);
    fd.append("file",file);

    return $.ajax({
        type : 'POST',
        url : url,
        data : fd,
        processData: false,  // tell jQuery not to convert to form data
        contentType: false  // tell jQuery not to set contentType
    });
};
