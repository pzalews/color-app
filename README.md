# color-app

## What is color-app

Color-app is a simple python app that displays "hello-world" html page.

Color-app needs to be configured by environment variables:
    - COLOR1 - this is a font color
    - COLOR2 - this is a bg color

## Simple usage:

```bash
docker run --rm -d -e COLOR1=blue -e COLOR2=darkblue -p 5000:5000 pzalews/color-app
curl localhost:5000
```

