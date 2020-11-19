FROM python:3.8.6-alpine3.12

RUN apk add unixodbc unixodbc-dev curl gcc g++

RUN pip install wheel pyodbc flask

RUN curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/msodbcsql17_17.6.1.1-1_amd64.apk

RUN apk add --allow-untrusted msodbcsql17_17.6.1.1-1_amd64.apk

ADD . .

CMD ["python","OrdersPerMinute.py"]
