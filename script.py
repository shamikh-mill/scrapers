import argparse 


ap = argparse.ArgumentParser(description = 'Script to greet and wish happy birthday.')

ap.add_argument("-n", "--name", type=str, default= "Shamikh",
        help= "Name of person to greet. ex: Shamikh")

ap.add_argument("-a", "--age", type=int, default= 19,
        help= "Age of person to greet. ex: 19")

args = vars(ap.parse_args())

print ('Happy ' + str(args['age']) + 'th' + ' Birthday ' + args['name'] + '!')
