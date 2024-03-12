
# Youtube Video Aggregator

Welcome to the Youtube Video Aggregator. This project contains an video aggregator which will search videos on youtube for a predefined query and store the results in a database and an API which will show stored results to users. The project is built using Flask and SQLAlchemy as ORM.

## Features

- A separate worker to get data from Youtube API in async manner and store it in database.
- A RESTful API to get data from database.
- Youtube videos will store their title, description, published date, thumbnail and video id.
- A mock server to test the API in case of Youtube API quota exhaustion.


## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd my-project
```

### Using Docker

We can use Docker to run the project. It would make sure all dependencies are installed.

To install Docker, follow steps below according to your operating system:

- [Linux](https://docs.docker.com/desktop/install/linux-install/)
- [Windows](https://docs.docker.com/desktop/install/windows-install/)
- [Mac](https://docs.docker.com/desktop/install/mac-install/)

After Docker is installed, run the project:

```bash
docker-compose down --volumes --remove-orphans && docker-compose up --build
```
This would start the API which will be available at port `8080`.


## Environment Variables

To run this project, you will need to add some environment variables.

If environment variables are not defined, API will use default values which you can figure out by checking code.

Example environment file is present by the name `.env.example` in the `./dev/configs` directory.

## API Reference


### Videos

#### Get videos sorted by published date

_Request_

```http
GET /videos HTTP/1.1
Host: localhost:8080
```

_Response_

```json
{
    "data": [
        {
            "id": 492,
            "title": "Video Title",
            "description": "Video Description",
            "published_at": "2024-03-12T11:48:52",
            "thumbnails": {
                "default": {
                    "url": "https://via.placeholder.com/120x90.png"
                },
                "high": {
                    "url": "https://via.placeholder.com/480x360.png"
                },
                "medium": {
                    "url": "https://via.placeholder.com/320x180.png"
                }
            },
            "created_on": "2024-03-12T11:48:52.753006",
            "updated_on": "2024-03-12T11:48:52.753006"
        }
    ],
    "count": 1,
    "status_code": 200
}
```

- This endpoint will return videos sorted by published date in descending order.
- Query parameters can be used to filter the results. `limit` and `offset` can be used to limit the number of results and to paginate the results.
- Default limit is 10 and default offset is 0.



## Tech Stack

**Server:** Python as Programming Language, Flask as Web Framework, SQLAlchemy as ORM

**Databases:** Postgresql


## TODO

- [ ]  Add documentation for API
- [ ]  Make API more secure
- [ ]  Add tests
- [ ]  Better error handling
- [ ]  Fix bugs if found 

## License

[MIT](https://choosealicense.com/licenses/mit/)

