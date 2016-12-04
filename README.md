# Rest.

Url API.

1. Registration user:

/api/registration/ method POST


Json data (example):


{
	"username": "test",
	"email": "test@example.com",
	"password": "test"
}


Json responce (example):


{"key": "21ec4ba06a92b609333ee1cb1afa7946", "message": "Registration successful"}



2. Get user profile:


/api/profile/?key=<API_KEY> metod GET.


Json responce (example):


{"email": "test@example.com", "username": "test", "posts_count": 0}


3. Create post:


/api/post/ method POST


json data (example):


{
	"key": "a7c0938d36b1c7ef4082ca44a0df2924",
	"title": "test1 said first",
	"body": "tes this is a good"
}

