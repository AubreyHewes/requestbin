[![wercker status](https://app.wercker.com/status/79acb75d4225b59f966e4d79aac4ef8f/s/custom "wercker status")](https://app.wercker.com/project/byKey/79acb75d4225b59f966e4d79aac4ef8f)

Originally Created by [Jeff Lindsay](http://progrium.com)

License
-------
MIT


Looking to self-host?
=====================

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Deploy your own instance using Heroku
Create a Heroku account if you haven't, then grab the RequestBin source using git:

`$ git clone git://github.com/AubreyHewes/requestbin.git`

From the project directory, create a Heroku application:

`$ heroku create`

Add Heroku's redis addon:

`$ heroku addons:add heroku-redis`

Set an environment variable to indicate production:

`$ heroku config:set REALM=prod`

Now just deploy via git:

`$ git push heroku master`

It will push to Heroku and give you a URL that your own private RequestBin will be running.

## Deploy your own instance using Dokku

`$ git clone git://github.com/AubreyHewes/requestbin.git`

Create a Dokku application:

`$ dokku apps:create requestbin`
`$ dokku config:set DOKKU_PROXY_PORT_MAP="http:80:8000"`

Link in a redis container:

`$ dokku redis:create requestbin`
`$ dokku redis:link requestbin requestbin`

Set an environment variable to indicate production:

`$ heroku config:set REALM=prod`

Now just deploy via git:

`$ git push dokku master`

## Deploy your own instance using Docker

On the server/machine you want to host this, you'll first need a machine with
docker and docker-compose installed, then grab the RequestBin source using git:

`$ git clone git://github.com/Runscope/requestbin.git`

Go into the project directory and then build and start the containers

```
$ sudo docker-compose build
$ sudo docker-compose up -d
```

Your own private RequestBin will be running on this server.


Contributors
------------
 * Barry Carlyon <barry@barrycarlyon.co.uk>
 * Jeff Lindsay <progrium@gmail.com>
