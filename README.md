## Extreme Weather Today

Python/Flask web app that displays the extreme weather for the past 24 hours for different continents and regions. It shows the following:

- Maximum Temperature
- Minimum Temperature
- Maximum Precipitation
- Maximum Wind Gust

It consists of the following services:

|Service   | Description  |
|:---|---:|
| Backend  | Periodically reads the latest weather data from Ogimet and exposes a REST API |
| Frontend  | Gets the latest data from the backend and creates the web page  |

Use the app here: App can be used at [weather.costa365.site](https://weather.costa365.site/).

### Run app
#### Development: 
```
docker-compose up backend frontend
```

#### Production: 
```
docker-compose -f docker-compose-prod.yml up
```

### Run unit tests
```
run-tests.sh
```

### Run integration tests
```
docker-compose run integration-tests
```
