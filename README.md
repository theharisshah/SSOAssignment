
in src/database set URI = os.environ.get('MONGODB_URI') to your localhost mongodb uri

![screenshot from 2018-01-04 18-15-17](https://user-images.githubusercontent.com/21083491/34564164-a213af26-f17b-11e7-92c5-c36c37fa07da.png)
![screenshot from 2018-01-04 18-15-09](https://user-images.githubusercontent.com/21083491/34564170-a6d91f6e-f17b-11e7-8b0a-6dad58717d7d.png)

![screenshot from 2018-01-04 13-31-34](https://user-images.githubusercontent.com/21083491/34554700-33a57410-f154-11e7-8607-fd8f16dc1f47.png)
![screenshot from 2018-01-04 13-31-41](https://user-images.githubusercontent.com/21083491/34554713-40f63578-f154-11e7-9b23-a833812f156d.png)
![screenshot from 2018-01-04 13-31-51](https://user-images.githubusercontent.com/21083491/34554716-45be0964-f154-11e7-8a5a-a3009f5bb505.png)
![screenshot from 2018-01-04 13-33-12](https://user-images.githubusercontent.com/21083491/34554722-4c9179ce-f154-11e7-9ce3-403527787ba3.png)
![screenshot from 2018-01-04 13-33-20](https://user-images.githubusercontent.com/21083491/34554726-52533910-f154-11e7-824d-5fcf74ceeb05.png)


# Assignment

Implement single sign-on functionality using any language and platform. The submission must include:

1) A master application that allows for the creation of new accounts and managing existing ones (change password, update profile information etc...)
2) Two sub applications that will require the user to log in using the single sign-on account. The application must reflect the user's profile information, and must update accordingly when it is changed in the master application. 
3) All of the application must remember the user credentials ("remember me") for subsequent logins, and logging out of any one of the application must revoke access across all applications.
4) Well documented codebase with *clear* instructions to build and run the application.

## Bonus:
	1) Use of LDAP / Kerberos / JWT Tokens
	2) Building the mentioned sub applications with some form of functionality and persistent state (like addressBook,
	chatApp etc..., as opposed to a sub application that merely displays user information).
	3) Dockerizing / containerizing the entire solution.
	4) Hosting the solution on the internet so that it's publicly accessible will be awesome.
  
Here are somethings we're watching out for:

1) **Code** A clean and simple to follow codebase with comments.
2) **Content** Documentation will help us understand your story telling ability.

If you're up for the challenge, fork this repository and complete your entire solution there. Feel free to use any stack of your choice, and we're open to partial feature submissions as well. Just see it as an opportunity to know each other technically.

Happy hacking, and have fun!
