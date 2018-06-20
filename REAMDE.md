# Gambit challenge

## Problem description
This is a programming challenge designed by [Gambit](https://github.com/gambit-labs/challenge).

TUF-2000M is an ultrasonic energy meter to which Gambit is providing access through a [live text feed](http://tuftuf.gambitlabs.fi/feed.txt) that shows the time of the reading followed by the first 100 register values.

The task is to choose on of two options:

* Option 1: Convert the register data into human readable format.
* Option 2: Present the data as it is, in a mobile friendly way.

## Solution
This application reads, parses and converts the data, and then presents the data as a web service.

The *Parser* class reads the feed and converts the register data to human readable data like integers, decimals and strings. This data is then presented in a *web.py* application in both tabular format and as a JSON web service.

The application is hosted on Heroku and can be seen at [https://tblomqvi-gambit-challenge.herokuapp.com](https://tblomqvi-gambit-challenge.herokuapp.com).

The JSON API can be accessed at [https://tblomqvi-gambit-challenge.herokuapp.com/dump](https://tblomqvi-gambit-challenge.herokuapp.com/dump) and supports URL query strings. For example [https://tblomqvi-gambit-challenge.herokuapp.com/dump?id=temperatureInlet&id=temperatureOutlet](https://tblomqvi-gambit-challenge.herokuapp.com/dump?id=temperatureInlet&id=temperatureOutlet) returns

```
{
  "temperatureInlet": {
    "Value": 17.786136627197266,
    "Unit": "C"
  },
  "temperatureOutlet": {
    "Value": 20.07769203186035,
    "Unit": "C"
  }
}	
```

The query strings can also be used when viewing data in the tabular format.

