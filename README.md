# Pig Latin Translation Microservice
This simple microservice converts text to pig latin. It operates over HTTP, accepting text in the body of a POST request and returning the translation in the body of the response.

## Getting Started
Just run the following command to get up and running. You can change the first 80 in `80:80` if another service is already listening on that port.
```bash
docker run -dp 80:80 sjawhar/piglatin
```

The service will then be listening on port 80 (or whatever you chose). If you visit that page, you should see a friendly welcome message.

## Using the Translator
### URL
`/translate`

### Method 
`POST`

### Request Body Structure
```js
{
    "text": string
}
```
The value of `text` must have length of at least 1.

### Success Response
* **Code:** `200 OK`
* **Content:**
```js
{
    "translation": string
}
```

### Error Response
* **Code:** Varies, `4xx` to `5xx`
* **Content:**
```js
{
    "title": string,
    ["description": string]
}
```
`description` might not be included in some 500 errors

### Sample Call
* **Request**
`POST /translate`
```js
{
    "text": "Please translate this for me, won't you?"
}
```

* **Response**
`HTTP/1.1 200 OK`
```js
{
    "translation": "Easeplay anslatetray isthay orfay emay, on'tway ouyay?"
}
```

## Libraries Used
* [Falcon](https://falconframework.org/)
* [Gunicorn](http://gunicorn.org/)

## TODO and Notes (in no particular order)
* The translator currently has problems with the following:
    * If a word starts with a consonant, the translator cannot tell if that consonant is silent.
        - For example, you might expect "honest" to be translated "honestyay", because it starts with a vowel sound. It is _actually_ translated as "onesthay", as if the "h" were voiced.
    * Words that contain are separated by a slash and no spaces.
        - For example, you might expect "this/that" to be translated "isthay/atthat", as if they were two words. They are _actually_ treated as one word and translated as "is/thatthay".
* Changes I would make to be used in production:
    * App files should be mounted into the container so they can be accessed by CI build agents
    * Use nginx reverse proxy container to serve webservice, instead of directly binding to host. It's easier to change, using ENV variables and Docker Compose.
    * Remove command from Dockerfile, or make more generic to serve as our microservice image for all our Python microservices
* I'm torn between hiding and exposing the piglatin helper functions (e.g. `_split_words()`. Exposing them makes them easier to test, so I went with that.
* The app is currently using Falcon, a REST framework, for RPC calls. It's easy enough to change, since most of `app.py` is boilerplate.
* We could add a `language` parameter to the request body, and have pig latin just be one of the options.
    - Would just require changing a few lines of code in the try block in `PigLatinProcedure.on_post()`, and renaming `piglatin.to_pig_latin()` to something like `translate()`

## Other Notes
If you'd like to mount the project files into the container and poke around with the app while it's running, run:
```bash
docker run -dp 80:80 -v "/path/to/app:/app" sjawhar/piglatin
```

If you'd like to build the Docker image, run the following from the project **root folder**:
```bash
docker build -t sjawhar/piglatin -f ./docker/Dockerfile .
```