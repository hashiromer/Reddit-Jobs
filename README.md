# Description

Aside from Upwork and Fiver, a lot of jobs/gigs are posted on Reddit as well, some of them tend to be really interesting that you won't find on popular job posting platforms.

I wrote this program to search for jobs from reddit and save them to a database. Additionally, it gives notifications as new jobs are posted. Currently, it is meant to run on personal computer and not on cloud as I didn't find any reason to do so.

# Known Limitations

- As my daily driver is Windows, the program is only tested to work on Windows. Some changes are required to make it work on Linux. Submissions are welcome though if anyone wants to extend it.

- Sometimes regular posts are marked incorrectly as jobs but it was a tradeoff I intentionally made to cover as many subreddits as possible. It is technically possible to remove them but the effort required wasn't worth it in my assessment.

- The UI isn't open source at the moment to query the jobs from database. `FRONTEND_URL` in .env.example refers to the url of UI.

# Setup

- Create a reddit application by registering here https://www.reddit.com/prefs/apps
- Get all the application credentials and save them to .env file, see .env.example to see the format
- Create a Mongo db database and get the MongoURI, save it to .env file , see .env.example to see the format

# Installing dependencies

The project uses poetry as package manager

## Installing Poetry

The project uses poetry as package manager, install it if you don't already have it on your system.

### Windows

```
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

- Create a virtual environment
- Activate virtual environment
- Install all dependencies using `poetry install` within the virtual environment
- Run `poetry run start` start the application
