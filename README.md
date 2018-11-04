# irlome-dev
## IRLOME project development code, Hack the IRL 2-4 Nov 2018

It uses a static hosted website in AWS S3, a simple javascript to submit photos to a folder in the bucket.  
A new file in the bucket triggers an AWS Lambda event that runs the shrink and cluster by color script.
This outputs data that links to mapbox data.  

Still very much a work in progress.

**Requirements:**
Python - matplotlib, PIL.
Javascript - all public web urls in the files already.
AWS implementation requires an AWS account.

## NOT YET SUITABLE FOR USE - STILL VERY MUCH A WORK IN PROGRESS
