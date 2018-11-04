var AWS = require('aws-sdk');
var fs = require('fs');


/*dummy update*/

var response = {
 "isBase64Encoded": false,
 "headers": { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': 'irlo.me'},
 "statusCode": 200,
 "body": "{\"result\": \"Success.\"}"
 };

exports.handler = function (event, context) {
    console.log('Received event:', event);
    upload_s3(event, function (err, data) {
        context.done(err, null);
    });
};

function upload_s3(event, done) {
  // Read in the file, convert it to base64, store to S3
  fs.readFile(event.photoupload, function (err, data) {
  if (err) { throw err; }

  var base64data = new Buffer(data, 'binary');

  var key = "photos/" + event.photoupload

  var s3 = new AWS.S3();
  s3.client.putObject({
    Bucket: 'irlo.me',
    Key: key,
    Body: base64data,
    ACL: 'public-read'
  },function (resp) {
    console.log(arguments);
    console.log('Successfully uploaded package.');
  });

});

}
