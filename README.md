# CHF2IDR

Simple python script that will convert CHF Swiss Francs to IDR Indonesian Rupiah and send the result to a telegram user.

### Prerequisites

* pip

```sh
sudo apt-get install python3-pip -y
```

### Installation


1. Get a free API Key from Telegram @BotFather https://telegram.me/BotFather. Then you can ask the Telegram UserID bot https://telegram.me/myidbot to give you your User ID by sending the command :

```sh
/getid
```

2. Clone the repo

```sh
git clone https://github.com/iyotee/CHF2IDR.git
```

3. Install pip packages

```sh
python3 pip install requests -y
```

```sh
python3 pip install json -y
```


4. Enter your API in `main.py` or `main2.py`

5. Simply run 

```sh
python3 main.py
```

or

```sh
python3 main2.py 
```
for using a different API service (APILAYER.COM)

### Optionnal

you can create a cron task every hour ( 0 * * * * ) 

```sh
crontab -e
```
edit the end of the files by appending :
```sh
0 * * * * python3 CHF2IDR/main.py
```

OR 

```sh
0 * * * * python3 CHF2IDR/main2.py
```

Save and exit with ctrl+x and that's it ! Your bot is now running and sending your message on your Telegram user every hour ! 🎊 
