import requests, cPickle, shutil, time

all = {}
errorout = open("errors.log", "w")

for i in range(600):
    playerurl = "http://fantasy.premierleague.com/web/api/elements/%s/"
    r = requests.get(playerurl % i)

    if r.status_code != 200: continue

    if i%10 == 0: print i

    try:
        all[i] = r.json()
    except ValueError:
        print "failed parsing player %s" % i
        errorout.write("Failed to parse player %s: %s\n" % (i, r.content))

t = str(time.time()).split(".")[0]
rawfile = "raw/players.%s.pickle" % t
with file(rawfile, 'w') as outfile:
    cPickle.dump(all, outfile)

shutil.copy2(rawfile, "players.data.pickle")
