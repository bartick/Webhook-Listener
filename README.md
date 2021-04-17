# Top.gg Server Webhook Listerner
This is a small project I came up with about top.gg server webhook listeners.

There are other better ways of doing this but I tried to make it with easy libraries and without the bot object which you need in top.gg python-sdk. 

It will be better if you use Quart instead of Flask for your project. But I have used flask to make it easier for everyone to understand.


## Get Started
```bash
# Install Requiements File
pip3 install -r requirements.txt
```

#### Create a sqlite3 database
```python
import sqlite3
conn = sqlite3.connect('path\\dabase.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXIST Webhook (Authorization text, Server int, Webhook text)''')

conn.commit()
conn.close()
```



### Put your token in .env
```.env
# Change the name .env-example to .env
DISCORD_AUTH = YOUR_DISCORD_BOT_TOKEN
```

### Run the webserver
```bash
# Run the file using
python wehook.py
```

### Top.gg Server Setup
> Go to [top.gg](https://docs.top.gg/) docs to read how to setup the webhhook url for server. But in sort it is `https://your-website/webhook`


## Conclusion
> This is kinda trial project for me so if you like this project please provide a star and if you found a bug/error in the project and you have fixed it then please create a pull request.