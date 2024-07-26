# IoT API Project

This project provides a REST API for managing IoT devices using `aiohttp` and `Peewee`, with `PostgreSQL` as the database backend. The application is containerized using Docker for ease of deployment.

## Running with Docker

To run the project with Docker, follow these steps:

1. **Clone the Repository**

    ```bash
    git clone https://github.com/paashkovaaa/iot_api.git
    ```

2. **Navigate to the Project Directory**

    ```bash
    cd iot_api
    ```

3. **Create PostgreSQL Database and Environment File**

    - Ensure PostgreSQL is set up. Create a `.env` file in the project directory with the following content:

      ```dotenv
      POSTGRES_DB=iot
      POSTGRES_USER=yourusername
      POSTGRES_PASSWORD=yourpassword
      HOST=db
      ```

4. **Build and Run the Docker Containers**

    ```bash
    docker-compose up --build
    ```

5. **Access the API Endpoints**

    The API will be accessible via `http://localhost:8080/`.

## API Endpoints

Below are the available API endpoints for managing IoT devices, users, and locations:

### Device Endpoints

#### Get All Devices

- **Endpoint:** `GET /devices`
- **Description:** Retrieves a list of all devices.
- **Response:** JSON array of devices.

#### Add a Device

- **Endpoint:** `POST /devices`
- **Description:** Adds a new device.
- **Request Body:**

    ```json
    {
        "name": "DeviceName",
        "type": "DeviceType",
        "login": "DeviceLogin",
        "password": "DevicePassword",
        "location_id": 1,
        "api_user_id": 1
    }
    ```

- **Response:** JSON object with the ID of the newly created device.

#### Update a Device

- **Endpoint:** `PUT /devices/{id}`
- **Description:** Updates an existing device.
- **Request Body:**

    ```json
    {
        "name": "UpdatedDeviceName"
    }
    ```

- **Response:** JSON object with status message.

#### Delete a Device

- **Endpoint:** `DELETE /devices/{id}`
- **Description:** Deletes a device by ID.
- **Response:** JSON object with status message.

### User Endpoints

#### Get All Users

- **Endpoint:** `GET /users`
- **Description:** Retrieves a list of all users.

#### Add a User

- **Endpoint:** `POST /users`
- **Description:** Adds a new user.
- **Request Body:**

    ```json
    {
        "username": "user1",
        "email": "user1@example.com",
        "password": "password123"
    }
    ```

#### Update a User

- **Endpoint:** `PUT /users/{id}`
- **Description:** Updates an existing user.
- **Request Body:**

    ```json
    {
        "username": "UpdatedUsername"
    }
    ```

#### Delete a User

- **Endpoint:** `DELETE /users/{id}`
- **Description:** Deletes a user by ID.

### Location Endpoints

#### Get All Locations

- **Endpoint:** `GET /locations`
- **Description:** Retrieves a list of all locations.

#### Add a Location

- **Endpoint:** `POST /locations`
- **Description:** Adds a new location.
- **Request Body:**

    ```json
    {
        "name": "LocationName"
    }
    ```

#### Update a Location

- **Endpoint:** `PUT /locations/{id}`
- **Description:** Updates an existing location.
- **Request Body:**

    ```json
    {
        "name": "UpdatedLocationName"
    }
    ```

#### Delete a Location

- **Endpoint:** `DELETE /locations/{id}`
- **Description:** Deletes a location by ID.

## Testing

To run tests, use the following command:

```bash
pytest tests/
```

## Note

Ensure the environment variable `HOST` is set to `localhost` before running tests. You can configure this in the `.env` file or directly in your testing environment.

## Using Postman

To interact with the API using Postman:

1. **Open Postman** and create a new request.

2. **Set the Request Method** (GET, POST, PUT, DELETE) according to the endpoint you wish to test.

3. **Enter the URL** based on the endpoint you want to interact with:
     - **For GET requests:** 
        - `http://localhost:8080/devices` (Get all devices)
        - `http://localhost:8080/users` (Get all users)
        - `http://localhost:8080/locations` (Get all locations)
    - **For POST, PUT, and DELETE requests:** 
        - Append the relevant ID as needed. For example:
            - `http://localhost:8080/devices/{id}` (Update or delete device with ID)
            - `http://localhost:8080/users/{id}` (Update or delete user with ID)
            - `http://localhost:8080/locations/{id}` (Update or delete location with ID)

4. **Set Headers and Body** as needed:
    - For `POST` and `PUT` requests, provide the request body in JSON format.

5. **Send the Request** and review the response to ensure the API is functioning as expected.
