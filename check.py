import kspconfig
import sys

if len(sys.argv) == 1:
    print("GIVE ME THE FILE PATH")
    sys.exit(1)

blacklist = ["bahaECMJammer", "AMRAAM.EMP", "BD1x1slopeArmor", "BD2x1slopeArmor", "BD1x1panelArmor", "BD2x1panelArmor", "BD3x1panelArmor", "BD4x1panelArmor"]
armpoint = {"bahaBrowningAnm2" : 0.5, "bahaAim9": 1.0, "bahaAim120": 1.5, "bahaChaffPod": 0.5, "bahaCmPod": 0.5, "bahaGau-8": 2, "bahaHiddenVulcan": 1.0}

armor2 = ["bahaAim9"]

b = open(sys.argv[1], encoding="UTF-8")

ap = 0.0

c = kspconfig.loadl(b.readlines())

err = []

for d in c["PART"]:
    e = '_'.join(d["part"].split("_")[:-1])
    print(e)
    if e in blacklist:
        err.append("Blacklisted Part: " + e)
    f = armpoint.get(e)
    if f is not None:
        ap += f
    g = 0
    for h in d["MODULE"]:
        if h["name"] == "HitpointTracker":
            g = int(h["Armor"])
    i = 10
    if e in armor2:
        i = 2
    if g > i:
        err.append("Armor Thickness is changed: " + e)
if ap > 15.1:
    err.append("Armpoint exceeded: " + str(ap))

if len(err) == 0:
    print("OK")
else:
    for e in err:
          print(e)
    print("Failed")
