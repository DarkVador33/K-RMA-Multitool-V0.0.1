import os
import time
import discord
import requests
import sys
from pystyle import Center
from pystyle import Write, Colors, Colorate
from colorama import Fore
from colorama import Style
import urllib.request

os.system("title K-RMA l Multitool V0.0.1")

def joiner():
  print()
  link = Write.Input("[Discord Invite Code]>",
                     Colors.blue_to_purple,
                     interval=0.0025)
  if len(link) > 6:
    link = link[19:]
  apilink = "https://discordapp.com/api/v6/invite/" + str(link)
  with open('tokens.txt', 'r') as handle:
    tokens = handle.readlines()
    for x in tokens:
      token = x.rstrip()
      headers = {'Authorization': token}
      requests.post(apilink, headers=headers)
    print()
    Write.Print("> All valid tokens have been invited!",
                Colors.blue_to_purple,
                interval=0.0025)


def checker():
  with open('tokens.txt', 'r') as handle:
    tokens = handle.readlines()
    for x in tokens:
      token = x.rstrip()
  headers = {'Authorization': token}
  src = requests.get('https://discordapp.com/api/v6/auth/login',
                     headers=headers)
  try:
    if src.status_code == 200:
      Write.Print("> Valid!", Colors.green, interval=0.0025)
    else:
      Write.Print("> Inavlid!", Colors.red, interval=0.0025)
  except Exception:
    print("ERROR")


def spammer():
  spam_option = input("CAPTCHA! Please enter 1 to verify you: ")

  if "1" in spam_option:
    with open('tokens.txt', 'r') as handle:
      tokens = handle.readlines()
      for x in tokens:
        token = x.rstrip()
        headers = {'Authorization': token}

    channel_id = input("Channel ID: ")
    number_of_spam = input("Number of Spams: ")
    spam_delay = input("Delay (Seconds): ")
    message_content = input("Message Content: ")
    content = message_content

    payload = {"content": f"{content}"}

    os.system("cls")
    print(f"{Fore.LIGHTBLUE_EX}Press Ctrl + C to Stop\n")
    for zero in range(int(number_of_spam)):
      try:
        requests.post(
          f"https://discord.com/api/v9/channels/{channel_id}/messages",
          headers=headers,
          data=payload)
        print(
          f"{Fore.GREEN}Message Sent to {channel_id}!\nContent: {content}\n{Style.RESET_ALL}"
        )
      except:
        print(f"{Fore.RED}Something went wrong :/{Style.RESET_ALL}")
        break

      time.sleep(int(float(spam_delay)))
    print(f"{Fore.WHITE}Operation Done!{Style.RESET_ALL}")
  elif "2" in spam_option:
    headers = {"authorization": f"{authorization}"}
    channel_id = input("Channel ID: ")
    spam_delay = input("Delay (Seconds): ")
    message_content = input("Message Content: ")
    content = message_content

    payload = {"content": f"{content}"}

    os.system("cls")
    print(f"{Fore.LIGHTBLUE_EX}SPAMMING!\n")
    num1 = 0
    while num1 <= 10:
      try:
        requests.post(
          f"https://discord.com/api/v9/channels/{channel_id}/messages",
          headers=headers,
          data=payload)
        print(
          f"{Fore.GREEN}Message Sent to {channel_id}!\nContent: {content}\n{Style.RESET_ALL}"
        )
      except:
        print(f"{Fore.RED}Something went wrong :/{Style.RESET_ALL}")
        break

      time.sleep(int(float(spam_delay)))
  else:
    print(f"{Fore.RED}\nInvalid Option :/{Style.RESET_ALL}")


def tkcreator():
  print()
  Write.Print(
    "> Github Source: https://github.com/imvast/Discord-Account-Creator",
    Colors.blue_to_purple,
    interval=0.0025)
  print()
  Write.Print("> Coming soon...", Colors.blue_to_purple, interval=0.0025)


def threadspam():
  os.system("python nopermnuker.py")


def vcspam():
  Write.Print("Coming soon", Colors.blue_to_purple, interval=0.0025)


def pxgen():
  req = urllib.request.Request("http://free-proxy-list.net/")
  req.add_header(
    "User-Agent",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1")
  sourcecode = urllib.request.urlopen(req)
  part = str(sourcecode.read())
  part = part.split("<tbody>")
  part = part[1].split("</tbody>")
  part = part[0].split("<tr><td>")
  proxylist = ""
  for proxy in part:
    proxy = proxy.split("</td><td>")
    try:
      proxylist = proxylist + proxy[0] + ":" + proxy[1] + "\n"
    except:
      pass
  out_file = open("proxy.txt", "w")
  out_file.write(proxylist)
  out_file.close()
  Write.Print("", Colors.blue_to_purple, interval=0.0025)

def credits():
  print()
  Write.Print("""Design: Snoyxo#2277
  Code: Dark Vador#2277
  Token Creator: imvast
  VC Spammer: Nekzy#9999
  Discord: https://dsc.gg/k-rma
  Github: https://github.com/DarkVador33""", Colors.blue_to_purple, interval=0.0025)

print()
print(
  Center.XCenter(
    Colorate.Horizontal(
      Colors.blue_to_purple, """
        ██   ██     ██████  ███    ███  █████  v0.0.1
        ██  ██      ██   ██ ████  ████ ██   ██ 
        █████   ███ ██████  ██ ████ ██ ███████
        ██  ██      ██   ██ ██  ██  ██ ██   ██
        ██   ██     ██   ██ ██      ██ ██   ██           

 All credits to: Dark Vador#2277 & Snoyxo#2491
 Discord: https://dsc.gg/k-rma
 Github: https://github.com/DarkVador33

 ╔══════════════════════════════════════════════════╗
 ║                                                  ║
 ║  1.Joiner          5.No perms nuker              ║
 ║                                                  ║
 ║  2.Checker         6.VC Spammer                  ║
 ║                                                  ║
 ║  3.Spammer         7.Proxy Generator             ║
 ║                                                  ║
 ║  4.Token Creator   8.Credits                     ║
 ║                                                  ║
 ╚══════════════════════════════════════════════════╝

""", 1)))
print()
choice = Write.Input("[?]> ", Colors.blue_to_purple, interval=0.0025)
if choice == "1":
  joiner()
if choice == "2":
  checker()
if choice == "3":
  spammer()
if choice == "4":
  tkcreator()
if choice == "5":
  threadspam()
if choice == "6":
  vcspam()
if choice == "7":
  pxgen()
if choice == "8":
  credits()
else:
  exit()
