# fampay-intern-assessment

# Backend Assignment (Intern) | FamPay
## Assessment Goal:
The goal of this assessment is to create an API that retrieves the most recent videos from YouTube, sorted by their date of publication, based on a specific search term (such as "internships"). The API will respond with paginated results and will continuously query the YouTube API every minute to ensure that the latest videos are always available. The information for each video, including the title, description, publishing date and time, thumbnail URLs, and video and channel IDs, will be stored in a database.
## Video Database
![image](https://user-images.githubusercontent.com/67872867/176224136-0ce8546e-5d23-49a0-9b1d-cf3628a8fc8d.png)

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
![github](https://user-images.githubusercontent.com/67872867/176204848-9e1b4169-eddd-4fda-acdb-b6a677b18663.jpg)
![image](https://user-images.githubusercontent.com/67872867/176204726-35d8acce-4c33-4255-bcbb-6c8cc4e47736.png)
- Django Secret Key and YouTube API has been used as environment variable, therefore they are hidden and <b>secure.</b>
- Added Dockerfile
  - <b> Benfits of Docker</b>
  - Docker has been used to address dependency issues that arise in software development by allowing developers to package their application and its dependencies into a single container. This ensures that the application will always run the same way, regardless of the environment.
  - By packaging the application and its dependencies into a container, we can ensure that the application will always have access to the correct versions of libraries and other dependencies. This eliminates the need to manually manage dependencies and ensures that the application will run consistently across different environments.

## Building Image using Docker
We can pass multiple environment variables during a Docker build by using the `--build-arg` flag in the docker build command. The syntax for the flag is `--build-arg VAR_NAME=VALUE`. For example, to pass two environment variables named VAR1 and VAR2, you would run the following command:
`docker build --build-arg VAR1=value1 --build-arg VAR2=value2 -t myimage .`

We can also use a file to pass multiple env variables in the following way -
`docker build --build-arg env_file=path/to/your/env/file -t myimage .`

### Filter
Video Duration filter has been added to the website. The video duration options are:
- Any
- Long
- Medium
- Short

Similarly other filter and sorting can be added if necessary.

### - By Aditya Goel
