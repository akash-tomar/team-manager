# Team Members Management

This is a RESTful API for team member management.

## Details: 

It supports addition, deletion, editing and viewing of team members. It is an API which can be used by a mobile as well as a web developer.

It has been implemented using Django web framework. 


## Documentation:

It supports four end points:

### Add [/addmember/]

#### Add a team member [POST]

You can add a team member using this action. It takes a JSON
object containing team member details.

+ Request 
    
    + Body

	        {
	            "first_name":"aakash",
	            "last_name":"tomar",
	            "email":"something@something.something",
	            "phone":"7291818864",
	            "role":"regular"
	        }
    
    + Headers

            Content-Type : application/json   

+ Response 200 (application/json)

    + Body

	      	{
	            "id":"124",
	            "first_name":"aakash",
	            "last_name":"tomar",
	            "email":"something@something.something",
	            "phone":"7291818864",
	            "role":"regular"
	        }

### Delete [/deletemember/]

#### Delete a team member [DELETE]

You may delete a team member using this action. It takes a JSON object containing the product name.

+ Request 
    
    + Body

	        {
	            "id":"124"
	        }
    
    + Headers

            Content-Type : application/json   

+ Response 200 (application/json)

    + Body

	      	{
	            
	        }

### Update [/update/]

#### Update team member details [POST]

You may update team member details using this action. Also, you can only add the fields that need to be updated. It takes a JSON object containing the product name.

+ Request 
    
    + Body

	        {
	            "id":"124",
	            "first_name":"akash",
	            "email":"akash.tomar217@gmail.com"
	        }
    
    + Headers

            Content-Type : application/json   

+ Response 200 (application/json)

    + Body

	      	{
	         	"id":"124",
         	 	"first_name":"akash",	
         	 	"last_name":"tomar",
         	 	"phone":"7291818864",
         	 	"role":"regular"
	            "email":"akash.tomar217@gmail.com"
	        }


### View [/getmembers/]

#### View all team member details [GET]

You may view all team member details using this action. It takes a JSON object containing the product name.

+ Request 
    
    + Headers

            Content-Type : application/json   

+ Response 200 (application/json)

    + Body

	      	{
	      		"data": [
	      					{
	      						"first_name": "akash", 
	      						"last_name": "tomar", 
	      						"role": "regular", 
	      						"email": "akash.tomar217@gmail.com", 
	      						"id": 2
	      					}, 

	      					{
	      						"first_name": "kamayani", 
	      						"last_name": "tewari", 
	      						"role": "admin", 
	      						"email": "blah@blah.com", 
	      						"id": 3
	      					}
	      				]
			}
