# appu

appu is a command line chef that brings you tasty food

## Demo
![](https://imgur.com/3AHOkmJ)

## Features

- Written in Python
- Uses the Zomato API, so works in 23 countries.
- Works on Linux, Windows and Mac.

## Installation


### From Source

```bash
$ git clone https://github.com/souravyuvrajj/appu
$ cd appu/
$ python setup.py install
```

## Usage

### Search for a restaurant

```bash
$ appu search Good Chinese Food
```

### Get surprised by something random in your budget

```bash
$ appu surprise
```

### Get restaurants that support a specific cuisine

```bash
$ appu cuisine Indian
```

Or to get a list of cuisines

```bash
$ appu cuisine list
```

### Get a list of restaurants in your budget.

```bash
$ appu budget 500
```

### Get details of a particular restaurant by id

```bash
$ appu restaurant 310543
```

### Get reviews of a restaruant by id

```bash
$ appu reviews 310543
```

### Reconfigure appu

```bash
$ appu configure
```

### Help

```bash
$ appu --help
```
