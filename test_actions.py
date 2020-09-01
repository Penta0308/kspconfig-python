import kspconfig


def test_smoke_test():
    d = open("tests/Penta6A5J.craft")
    f = kspconfig.loadl(d.readlines())
    # pprint(f)
    assert f["ship"] == "Penta6A5J", "Name"
    assert f["PART"][1]["part"] == "bdPilotAI_4294438596", "Part"