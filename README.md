``` cron
10 4 * * * docker run --rm -v /opt/python-count-handson:/opt/python-count-handson irixjp/python-count-handson:latest sh -c "cd /opt/python-count-handson && python count_handson.py"
15 4 * * * cp /opt/python-count-handson/*png /opt/python-count-handson/image_pull_count.pkl.gz /opt/dockerhubinfo/
```
