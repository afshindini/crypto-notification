# Create Crypto Notification to Your Telegram
In this project, we simply try to get data from a crypto API and use a webhook and IFTTT (If this, then that!) to send a notification to a telegram account.

## Crypto API
There are several APIs for crypto curreny among which we selected [coinapi](https://www.coinapi.io/market-data-api). You need to create a free acount and get you `API KEY` for receiving the crypto information. By creating an account you can easily get your own API key.

## Webhook
A webhook is an HTTP request, triggered by an event in a source system and sent to a destination system, often with a payload of data. Webhooks are automated, in other words they are automatically sent out when their event is fired in the source system. This provides a way for one system (the source) to "speak" (HTTP request) to another system (the destination) when an event occurs, and share information (request payload) about the event that occurred.

Simply put, webhooks are used to communicate the occurrence of an event in one system to another system, and they often share data about the event. Let's say you subscribe to a streaming service. The streaming service wants to send you an email at the beginning of each month when it charges your credit card. The streaming service can subscribe to the banking service (the source) to send a webhook when a credit card is charged (event trigger) to their emailing service (the destination). When the event is processed, it will send you a notification each time your card is charged. The banking system webhooks will include information about the charge (event data), which the emailing service uses to construct a suitable message for you, the customer.

## Zapier as IFTTT
IFTTT aka "If this then that!" is a web service that bridges the gap between different apps and devices. An IFTTT applet is composed of two parts: a trigger and an action. In our case, the trigger will be a webhook service provided by IFTTT. Our Python app will make an HTTP request to the webhook URL which will trigger an action. IFTTT offers a multitude of actions like sending an email, updating a Google Spreadsheet and even calling your phone. 
We use the free [Zapier](https://zapier.com/app/home) IFTTT to send message to our telegram account.

To do so, you need to create a free account in Zapier(https://zapier.com/app/home) after which you would be able to create an applet. In teh trigger part of applet you should select a webhook to "Catch Hook". You will need the final URL of the created webhook in the code. For the action part, you choose the "Telegram Message" and connect to your telegram account by following the instruction. After connecting to your telegram account, in the related "configuration" section you need choose your `chatID` which is the ID of the channel/bot/saved_message in your telegram. `Text format` can be selected as `Plain Text`. In the message section, you can specify the format of the message you want to send. In this project, we wanted to send the message as `Latest crypto prices: {{Value3}}:  {{Value1}} {{Value2}}` where we will define values for `Value1/2/3` in our python script.

## Run Locally
To run the code locally, clone this respository and run `python main.py` command. It will load the `config.yml` file and create messages based on the related information. You should modify it based on your need.

## Run as a Container
I wrote a simple Dockerfile to make it possible to run this service as a container.
To do so, create the docker image by running `docker build -t crypto_notification:latest .` and then run the container by `docker run crypto_notification:latest --show_conf`.

