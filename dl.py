import requests, cPickle

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

fout = open("players.data.pickle", 'w')
cPickle.dump(all, fout)
