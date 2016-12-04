# Rest.

Url API.



 - Registration user:


/api/registration/ method POST


Json data (example):


{
	"username": "test",
	"email": "test@example.com",
	"password": "test"
}


Json responce (example):


{"key": "21ec4ba06a92b609333ee1cb1afa7946", "message": "Registration successful"}





 - Get user profile:


/api/profile/?key=API_KEY metod GET.


Json responce (example):


{"email": "test@example.com", "username": "test", "posts_count": 0}




 - Create post:


/api/post/ method POST


json data (example):


{
	"key": "a7c0938d36b1c7ef4082ca44a0df2924",
	"title": "test1 said first",
	"body": "tes this is a good"
}




 - Get user posts.


/api/post/?key=AIP_KEY method GET


[{"body": "POST_BODY1", "title": "POST_TITLE1"}, {"body": "POST_BODY2", "title": "POST_TITLE2"}]





 - Get user posts with paginator (keyword - page):


/api/post/?key=AIP_KEY&page_number  method GET




 - Get all posts (keyword - all , without parameters):


/api/post/?key=AIP_KEY&all  method GET




 - Search posts (keyword title and body). All arguments must be separated "+":


/api/post/?key=AIP_KEY&all&title=w1+w2&body=w1+w3


Json response (exemple):
[{"body": "w1 w3 anything", "title": "something w1 w2 something"}]
