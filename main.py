from login import login
from click_sign import sign
from click_questions import questions
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--pd", help="password of iios", required=True)
parser.add_argument("--acc", help="account of iios", required=True)
args = parser.parse_args()

browser = login("https://iios.fun/#", args.pd, args.acc)
sign("https://www.iios.fun/#/points", browser)
questions("https://www.iios.fun/#/points", browser)
