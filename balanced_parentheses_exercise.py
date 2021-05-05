import pytest


def are_parentheses_balanced(string):
    raise NotImplementedError()


TEST_CASES = (
    ('Hello world',     True),
    ('(Hello world)',   True),
    ('Hello (world',    False),
    ('Hello world)',    False),
    ('',                True),
    ('()',              True),
    ('((hello))',       True),
    ('((hello) world',  False),
    ('Hello )( world',  False),
    ('(Hello)) world(', False),
    ('(Hello() (world(())))', True)
)


@pytest.mark.parametrize('string,expected', TEST_CASES)
def test_check_parenthesis(string, expected):
    assert are_parentheses_balanced(string) == expected
