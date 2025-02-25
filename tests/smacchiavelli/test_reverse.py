import sys 
sys.path.append("packages/smacchiavelli/reverse")
import reverse

def test_reverse():
    res = reverse.reverse({"input" : "ciao"})
    assert res["output"] == "oaic"
