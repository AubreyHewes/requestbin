[![wercker status](https://app.wercker.com/status/79acb75d4225b59f966e4d79aac4ef8f/s/custom "wercker status")](https://app.wercker.com/project/byKey/79acb75d4225b59f966e4d79aac4ef8f)

# Your own private RequestBin

https://github.com/Runscope/requestbin

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

Will use Dokku Dockerfile deployment

`$ git clone git://github.com/AubreyHewes/requestbin.git`

Create a Dokku application:

`$ dokku apps:create requestbin && dokku config:set DOKKU_PROXY_PORT_MAP="http:80:8000"`

Link in a redis container:

`$ dokku redis:create requestbin && dokku redis:link requestbin requestbin`

Set an environment variable to indicate production:

`$ dokku config:set requestbin REALM=prod`

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

## Configuration

You can configure the runtime via environment variables

| Key | Description |
| --- | --- |
| SESSION_SECRET_KEY | Set to a unique value; **default is untrusted; so set this in production** |
| BIN_TTL | The TTL of a bin. Set to an int value in hours; default `48` |
| MAX_REQUESTS | A bin will keep the last `MAX_REQUESTS` requests made. Set to an int value; default `20` |
| MAX_RAW_SIZE | Set to an int value in bytes: default `10240` |
| MAX_JSON_TO_PRETTYPARSE_IN_BYTES | Set to an int value in bytes: default `307200` |
| BUGSNAG_KEY | Set your [BugSnag](https://www.bugsnag.com) key |
| REDIS_URL | Set your REDIS_URL |
| ENABLE_CORS | Enable CORS |
| CORS_ORIGINS | Set CORS origins; default `*` if `ENABLE_CORS` |
| ROOT_URL | Set your ROOT_URL without PORT (superfluous; not used anywhere) |
| PORT | Set listening port; default `8000` (Fixed at `8000` in docker/dokku) |
| DEBUG | Display some debug output; default `False` in `prod` and `True` in `local` |

Contributors
------------
 * Barry Carlyon <barry@barrycarlyon.co.uk>
 * Jeff Lindsay <progrium@gmail.com>
 * https://github.com/AubreyHewes/requestbin/graphs/contributors
