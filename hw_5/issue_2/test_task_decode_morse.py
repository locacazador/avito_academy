import pytest

from morse import decode


@pytest.mark.parametrize('s,exp', [
    ('.- .- .-', 'AAA'),
    ('...-- ..--- ..---', '322'),
    ('... --- ...', 'SOS'),
    ('-- .- --. .. -.-. -....- ... - .. -.-. -.-', 'MAGIC-STICK'),
    ('-- .- --. .. -.-.      ... - .. -.-. -.-', 'MAGIC STICK')
])
def test_decode_regular(s, exp):
    assert decode(s) == exp
