from .. import kspconfig
import json


def test_smoke_test():
    d = open("Penta6A5J.craft")
    f = kspconfig.loadl(d.readlines())
    print(f)
    assert f["ship"] == "Penta6A5J", "Name"
    assert f["PART"][1]["part"] == "bdPilotAI_4294438596", "Part"
    d.close()
    with open("tests/res3.json", "w") as a:
        json.dump(f, a, indent=4)

test_smoke_test()