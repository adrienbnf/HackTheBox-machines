# Cap - HackTheBox writeup

## First steps

```
$> nmap 10.10.10.245
```
```
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
80/tcp open  http
```

```
$> ftp 10.10.10.245
```

We try to authenticate as anonymous with no password but we get **"530 Login incorrect"**. So it appears that the anonymous authenctication is not activated on this server. We will, then, need some credentials.

We will now try to analyze the website hosted on port 80.

## Port 80: Security pannel

When we first arrive on the landing page it seems that this website is an admin pannel for the server security.

There is especially one interesting tab that allow us to download a security snapshot as a *.pcap* file. It could be interesting considering that such type of files contains data about packets sent/received in a network.

But, for now the snapshot that I have is completely empty.

//Image de la snapshot

The subdirectory of the snapshot page is **/data/1**. When trying other subdirectories like **/data/2** or **/data/3** I had other snapshots but all of them are empty like the first one.

But when I tried **data/0**... Bingo !

//Image de la snapshot

We now have a snapshot containing some data that we can analyze using WireShark.

## The crucial .pcap snapshot
