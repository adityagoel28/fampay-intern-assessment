# fampay-intern-assessment

# Backend Assignment (Intern) | FamPay
## Assessment Goal:
The goal of this assessment is to create an API that retrieves the most recent videos from YouTube, sorted by their date of publication, based on a specific search term (such as "internships"). The API will respond with paginated results and will continuously query the YouTube API every minute to ensure that the latest videos are always available. The information for each video, including the title, description, publishing date and time, thumbnail URLs, and video and channel IDs, will be stored in a database.
## Video Database
![image](https://user-images.githubusercontent.com/67872867/212305468-6530ad42-03d0-46ed-a5e6-2617a979a311.png)

## Implementation
A Javascript function is created which redirects the page to `/search/` url every 1 minute, which then goes to the `search` function inside `views.py`. Inside the function, we call the YouTube API and fetch the latest video results.
With the help of this method, server calls the YouTube API continuously every 1 minute for fetching the latest videos for the predefined search query. This method helps to update the changes on the webpage in <b>realtime</b> every 1 minute.

Another method has also been created using `job scheduling`. For this APScheduler is used.
Advanced Python Scheduler (APScheduler) is a Python library that lets us schedule our Python code to be executed later, either just once or periodically. We can add new jobs or remove old ones on the fly as we please. For our purpose, we have scheduled our Python code inside `jobs` directory to run periodically every set interval of seconds. For the time being, this method is disabled and 1st method is used.

A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.

## Language & Framework Used
Python (Django), HTML and CSS

## Bonus Points
- Added support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available key.
- Dashboard to view the stored videos with filter option.
![image](https://user-images.githubusercontent.com/67872867/212303720-113b3856-b60d-420a-bdaf-9a4694127910.png)
![image](https://user-images.githubusercontent.com/67872867/212305414-9281a2b1-82d3-42c5-8f2b-524b447e1339.png)
- Django Secret Key and YouTube API has been used as environment variable, therefore they are hidden and <b>secure.</b>
- Added Dockerfile
  - <b> Benfits of Docker</b>
  - Docker has been used to address dependency issues that arise in software development by allowing developers to package their application and its dependencies into a single container. This ensures that the application will always run the same way, regardless of the environment.
  - By packaging the application and its dependencies into a container, we can ensure that the application will always have access to the correct versions of libraries and other dependencies. This eliminates the need to manually manage dependencies and ensures that the application will run consistently across different environments.

## How to run the repo
- Create a python environment. below is the example of creating the environment using `conda` <br>
`conda create -n env_name`
- Clone the repository, and `cd` into it.
- `cd fampay-intern-assessment` and then `cd fampay`
- Install the dependencies with `pip install -r requirements.txt`
- Run the server with `python manage.py runserver` <br>
<b> The development server should be up and running at http://127.0.0.1:8000/</b>
- You can create the superuser with `python manage.py createsuperuser`.

## Building Image using Docker
We can pass multiple environment variables during a Docker build by using the `--build-arg` flag in the docker build command. The syntax for the flag is `--build-arg VAR_NAME=VALUE`. For example, to pass two environment variables named VAR1 and VAR2, you would run the following command:
`docker build --build-arg VAR1=value1 --build-arg VAR2=value2 -t myimage .`

We can also use a file to pass multiple env variables in the following way - <br>
`docker build --build-arg env_file=path/to/your/env/file -t myimage .`

### Filter
Video Duration filter has been added to the website. The video duration options are:
- Any
- Long
- Medium
- Short

Similarly other filter and sorting can be added if necessary.

### - By Aditya Goel
