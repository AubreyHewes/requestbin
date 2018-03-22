# Your own private RequestBin  
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/AubreyHewes/requestbin/blob/master/LICENSE) 
[![Coverage Status](https://coveralls.io/repos/github/AubreyHewes/requestbin/badge.svg)](https://coveralls.io/github/AubreyHewes/requestbin)
[![wercker status](https://app.wercker.com/status/79acb75d4225b59f966e4d79aac4ef8f/s/custom "wercker status")](https://app.wercker.com/project/byKey/79acb75d4225b59f966e4d79aac4ef8f)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/AubreyHewes/requestbin/pulls)

Originally Created by [Jeff Lindsay](http://progrium.com). Previously publicly hosted as [https://requestb.in](https://github.com/Runscope/requestbin)

#### Inspect HTTP requests. Debug webhooks.

TODO intro

## Looking to self-host?

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

### Deploy your own instance using Heroku
Create a Heroku account if you haven't, then grab the RequestBin source using git:

```shell
git clone git://github.com/AubreyHewes/requestbin.git
```

From the project directory, create a Heroku application:

```shell
heroku create
```

Add Heroku's redis addon:

```shell
heroku addons:add heroku-redis
```

Set an environment variable to indicate production:

```shell
heroku config:set REALM=prod
```

Now just deploy via git:

```shell
git push heroku master
```

It will push to Heroku and give you a URL that your own private RequestBin will be running.

### Deploy your own instance using Dokku

Will use Dokku Dockerfile deployment

```shell
git clone git://github.com/AubreyHewes/requestbin.git`
```

Create a Dokku application:

```shell
dokku apps:create requestbin
dokku config:set DOKKU_PROXY_PORT_MAP="http:80:8000" # fix the port
```

Link in a redis container:

```shell
dokku redis:create requestbin
dokku redis:link requestbin requestbin
```

Set an environment variable to indicate production:

```shell
dokku config:set requestbin REALM=prod
```

Now just deploy via git:

```shell
git push dokku master
```

### Deploy your own instance using Docker

On the server/machine you want to host this, you'll first need a machine with
docker and docker-compose installed, then grab the RequestBin source using git:

```shell
git clone git://github.com/AubreyHewes/requestbin.git
```

Go into the project directory and then build and start the containers

```shell
sudo docker-compose build
sudo docker-compose up -d
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
