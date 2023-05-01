from stepik_a import stepik_a
import pytest

@pytest.mark.parametrize('num', [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
def test_stepik_a(browser, num):
    link = f"https://stepik.org/lesson/{num}/step/1"
    stepik_a(browser,link)
