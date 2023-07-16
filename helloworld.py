import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--adminEmail', type=str, required=True)
parser.add_argument('--coolVariable', type=str, required=True)
parser.add_argument('--radVariable', type=str, required=True)

args = parser.parse_args()

# print('Email:', args.adminEmail)
# print('coolVariable:', args.coolVariable)
# print('radVariable:', args.radVariable)

adminEmail = args.adminEmail
coolVariable = args.coolVariable
radVariable = args.radVariable

print(f'This is the email: adminEmail')

