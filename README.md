# python2to3-inspector
Inspect behavior for updating Python version from 2.x to 3.x.  
This code works on only Python 2.x.

## 2to3
https://docs.python.org/3/library/2to3.html

### Installation
CentOS

```bash
$ yum install python-tools
```

Ubuntu

```
$ apt-get install 2to3
```

### Usage
Check

```
$ 2to3 PRJ-ROOT/*
```

Convert and create backup files

```
$ 2to3 -w PRJ-ROOT/*
```

Convert without creating backup files

```
$ 2to3 -w --nobackups PRJ-ROOT/*
```

## futurize
http://python-future.org/automatic_conversion.html

### Installation

```
$ pip install future
```

### Usage
Check stage1

```
$ futurize --stage1 PRJ-ROOT/*
```

Check stage2

```
$ futurize --stage2 PRJ-ROOT/*
```

Convert and create backup files

```
$ futurize --stage1 -w PRJ-ROOT/*
```

Convert without creating backup files

```
$ futurize --stage1 -w --nobackups PRJ-ROOT/*
```
