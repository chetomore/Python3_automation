import argparse

parser=argparse.ArgumentParser(description="A simple argparse example")
parser.add_argument("name",help="Yor name")
parser.add_argument("age",type=int,help="Your age")
parser.add_argument("--city",default="Unknown",help="Your city")

args=parser.parse_args()
print(f"Hello {args.name}, you are {args.age} years old and from {args.city}")