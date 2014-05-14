import sys
import os.path


if len(sys.argv)!=3:
    print "error need more arguments <input file> <output file>"
    sys.exit()

fname = sys.argv[1]
fname2 = sys.argv[2]

os.path.isfile(fname)

f = open(fname, 'r')


if os.path.isfile(fname2):
    print "Error output file already exists. Change name or erase file manually.."
    sys.exit()
else:
    f2 = open(fname2, 'w')

lines = f.readlines()

for line in lines:
    good = True
    i = int(line.split(' ', 1)[0])
    text = line.split(' ', 1)[1]
    print "="*40
    print "tweet#", i
    print text
    while (good):
        try:
            num = input("1. Happy     2. Sad   3. Neutral:  ")
            if num == 7:
                a = raw_input("Close? y/n  ")
                print a
                if a == "y":
                    f2.close()
                    print "Please check output file in your text editor"
                    raise SystemExit
            if num == 1 or num == 2 or num == 3:
                good = False
            else:
                print '??????????\n'
        except SystemExit:
            raise SystemExit
        except:
            print '??????????\n'
            pass




    f2.write(str(num)+','+text)