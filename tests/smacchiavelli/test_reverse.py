import sys 
sys.path.append("packages/smacchiavelli/reverse")
import reverse

def test_reverse():
    res = reverse.reverse({})
    assert res["output"] == "reverse"
