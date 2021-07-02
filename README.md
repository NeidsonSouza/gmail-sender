# gmail-sender

Este projeto tem como objetivo fornecer um app Python capaz de enviar email, a partir de uma conta Gmail, de maneira fácil e simples.

## Dependências
    
  * Linux
  * Python 3.7
  * Módulos Python:
      - venv

## Instalação

```console
$ python3 -m venv gmail-app
$ cd gmail-app/
$ . bin/activate
$ pip install --upgrade pip
$ git clone https://neidsonsouza@bitbucket.org/wisereducacao/gmail-sender.git
$ cd gmail-sender/
$ pip install .
```

## Execução

```console
$ export FROM_GMAIL_ACCOUNT=my.account@gmail.com
$ export PASSWORD_GMAIL_ACCOUNT=mYpAsSwOrD
$ echo "my.email@hotmail.com" > data/send_to.txt  # Receiver
$ echo "email.of.my.friend@gmail.com" >> data/send_to.txt  # Receiver
$ python3 gmailsender.py \
  -u $FROM_GMAIL_ACCOUNT \
  -p $PASSWORD_GMAIL_ACCOUNT \
  -r data/send_to.txt \
  -s "Email Subject" \
  -m data/message.txt \
  -a data/attachment.txt
```
```-m``` (```--message```) and ```-a``` (```--attachment```) flag is optional.

## Help

```console
$ python3 gmailsender.py -h
usage: gmailsender.py [-h] -u USERNAME -p PASSWORD -r RECIPIENT -s SUBJECT
                      [-m MESSAGE] [-a ATTACHMENT]

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        Gmail account (sender).
  -p PASSWORD, --password PASSWORD
                        Gmail password (sender).
  -r RECIPIENT, --recipient RECIPIENT
                        Indicate file with list of receiver emails.
  -s SUBJECT, --subject SUBJECT
                        Email subject.
  -m MESSAGE, --message MESSAGE
                        File with the body message.
  -a ATTACHMENT, --attachment ATTACHMENT
                        File to be attached.
```
## Autor

Nome: Neidson Souza

Email: neidson.ds.souza@gmail.com
