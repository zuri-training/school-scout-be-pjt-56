# Welcome to School Scout Backend APIs Documentation

## User Registration and Authentication Endpoints
...

**I. END POINT:** /auth/registration/

This endpoint is responsible for registering new users.
>
> **Media Type:** *"application/json"*
>
> **Allowed Methods:** "POST"
>
> **Content (Request):**
>
> * username
> * email
> * password1
> * password2
> * first_name
> * last_name
> 
> Note: 
> 1. The password must be atleast 8 characters and not more than 150 characters
> 1. It can not be entirely numeric 
> 1. It can only contain letters, digits and @/./+/-/_ 
> 
> **Return Type:** *"application/json"*
>
> **Content (Response):**
> * key

...

**II. END POINT:** /auth/login/

This endpoint is responsible for authenticating a user.
>
> **Media Type:** *"application/json"*
>
> **Allowed Methods:** "POST"
>
> **Content (Request):**
>
> * username \<optional>
> * email
> * password
> 
> **Return Type:** *"application/json"*
>
> **Content (Response):**
> * key
