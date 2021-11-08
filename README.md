# Nurture User-Advisor Booking API

This project is based on Django-rest API framework. 

Hosted Base Project URL: **https://herokunurtureapi.herokuapp.com/**

```
Please let me know if you have any problem with consuming API and any error or bug.

sourabhsahu69733@gmail.com
```
## Main library or framwork and 
* Django ()

### Local setup is needed only if using it for furtuhr improvement and developement.
All API's are consumed easily via provided hosted link
To run local: 
* Create a virtual environment (python -m venv env for windows ) and install all dependency in env 
* Run **python manage.py makemigrations** and **python manage.py migrate**
* Start local server **python manage.py runserver**

## Main functions and working flow;
There are three main parts of this application --> User, Admin, Advisor.
Admin will add advisor (name and photourl ) and user can book a appointment with any available advisor.

### File Structure 
app `api` have serializer file using django-rest-framework create json response of fetched data from database (sqlite)

There are total 6 API's, listed below;
--
|**Sr. No.** | **Module** |**API end point** | **Method**  | **Request Body** |  **Response** | **Expectation & working** | **Comments** |
| 1. | Advisor | `/api/v1/user/<int:userId>/advisor/<int:advisorId>` | POST | ```{"bookingTime":"2021-11-12 10:10:10"}``` | `200_OK` or `400_BAD_REQUEST` | It should create a booking of a advisor for a user | will add imporvements in these implementation |
| 2. | Advisor | `/api/v1/user/<int:userId>/advisor/booking` | GET  | NA | List of advisor (name, id, photUrl, bootkingTime, bookingId ) |   | List all advisor booked by a user | ------ |
| 3. |  User | `/api/v1/user/login` | POST | `{"email":"hardik@gmail.com","password":"123456"}` | `{UserId, JWT_Token}` | login user with authorization supported by JWT token | ------ |
| 4. | User | `/api/v1/user/register` | POST | `{"name":"hardik","email":"hardik@gmail.com","password":"123456"}` | `{UserId, JWT_Token}` | register a user with email, name and password |------ |
| 5. | Admin | `/api/v1/admin/<int:userId>/advisor` | GET | NA | A array of all advisor created by admin ```[{id, name, photoUrl}] | List all advisor added by admin  | ------ |
| 6. | Admin | `/api/v1/admin/advisor` | POST | `{name: sourabh, photoUrl: "https://tinyurl.com/y9rxx22w" }` | `200_OK` or `400_BAD_REQUEST` | Register a advsior by admin | ------ |