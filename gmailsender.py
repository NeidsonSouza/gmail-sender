

import os
from argparse import ArgumentParser
from gmail import main
from pathlib import Path

def get_args():
    parser = ArgumentParser()
    # gmailsender -u USER -p PSWD -r recipients.txt -m message.txt -a file.pdf
    parser.add_argument("-u", "--username", required=True, help="Gmail account (sender).")
    parser.add_argument("-p", "--password", required=True, help="Gmail password (sender).")
    parser.add_argument("-r", "--recipient", required=True, help="Indicate file with list of receiver emails.")
    parser.add_argument("-s", "--subject", required=True, help="Email subject.")
    parser.add_argument("-m", "--message", help="File with body message.")
    parser.add_argument("-a", "--attachment", help="File to be attached.")
    return parser.parse_args()

def set_envs(args):
    recipient_path = Path(os.getcwd()) / args.recipient
    if args.message != None:
        message_path = Path(os.getcwd()) / args.message
    if args.attachment != None:
        attachment_path = Path(os.getcwd()) / args.attachment
    
    os.environ["USERNAME"] = args.username
    os.environ["PASSWORD"] = args.password
    os.environ["RECIPIENT"] = str(recipient_path)
    os.environ["SUBJECT"] = args.subject
    if args.message != None:
        os.environ["MESSAGE"] = str(message_path)
    if args.attachment != None:
        os.environ["ATTACHMENT"] = str(attachment_path)

if __name__ == "__main__":
    args = get_args()
    set_envs(args)
    main()
