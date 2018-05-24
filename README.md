# LightBerry
An open source home automation platform with Alexa integration

Server exposes a REST API as well as a user dashboard for linking devices. Accounts managed by Auth0. Clients communicate through MQTT.

### Setup
The default client implementations contain device metadata within the `config.py` files. Values to be changed include `deviceId` and `pairingCode`.
These values must be unique across devices, so a UUID should be used for the device ID and a randomly generated, yet easily typed code, should be used for the pairing code.
See the below [Environment Variables](#environment-variables) section for necessary variables to be set.

### Supported Device Types
This list will be updated as more device implementations become supported:
- Switch (on/off)

### Environment Variables
#### Server
The supplied server implementation requires the following variables to defined in a `.env` file within the `server` directory:
```
MQTT_SERVER: server hosting MQTT broker

MQTT_PORT: port on which to connect to MQTT broker

HTTP_PORT: port on which to host client dashboard

EXTERNAL_URL: external URL dashboard site may be accessed at (used for Auth0 authentication)

SECRET: random secret used to authenticate clients to server (will be changed for more secure method)

AUTH0_CLIENT_ID: client ID obtained from Auth0

AUTH0_CLIENT_SECRET: client SECRET obtained from Auth0

AUTH0_API_BASE_URL: base URL of Auth0 API

AUTH0_ACCESS_TOKEN_URL: access token URL of Auth0 API (usually AUTH0_API_BASE_URL+'/oauth/token')

AUTH0_AUTHORIZE_URL: authorize URL of Auth0 API (usually AUTH0_API_BASE_URL+'/authorize')

AUTH0_CALLBACK_URL: callback URL of Auth0 API (usually EXTERNAL_URL+'/callback')

AUTH0_AUDIENCE: user info URL of Auth0 API (usually AUTH0_API_BASE_URL+'/userinfo')
```

#### Client
The supplied client implementations require the following variables to defined in a `.env` file within the associated client's base directory:
```
MQTT_SERVER: server hosting MQTT broker

MQTT_PORT: port on which to connect to MQTT broker

SECRET: random secret used to authenticate clients to server (defined in server environment)
```

For more info, see https://github.com/theskumar/python-dotenv
