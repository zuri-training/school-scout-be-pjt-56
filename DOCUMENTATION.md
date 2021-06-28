# Welcome to School Scout Backend APIs Documentation

## User Registration and Authentication Endpoints

**I. END POINT:** /auth/registration/

> This endpoint is responsible for registering new users.
>
> **Media Type:** *"application/json"*
>
> **Allowed Methods:** "POST"
>
> **Content (Request):**
>
> * username \<string, unique, required>
> * email \<string, unique, required>
> * password1 \<string, required>
> * password2 \<string, required>
> * first_name \<string, required>
> * last_name \<string, required> 
> * **Note:** The password must be atleast 8 characters and not more than 150 characters, can not be entirely numeric and can only contain letters, digits and @/./+/-/_ 
> 
> **Return Type:** *"application/json"*
>
> **Content (Response):**
> * key \<string>

**II. END POINT:** /auth/login/

> This endpoint is responsible for authenticating a user.
>
> **Media Type:** *"application/json"*
>
> **Allowed Methods:** "POST"
>
> **Content (Request):**
>
> * username \<string, optional>
> * email \<string, required>
> * password \<string, required>
> 
> **Return Type:** *"application/json"*
>
> **Content (Response):**
> * key \<string>
