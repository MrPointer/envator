from envator.config.configdict import EnvatorConfigDict
from envator.util.namingcase import NamingCase


class TestConfigDict:
    def test_with_keys_case_lower(self):
        config = EnvatorConfigDict({"FooBar": 42, "BazQux": 69})
        assert config.with_keys_case(NamingCase.LOWER) == {"foobar": 42, "bazqux": 69}

    def test_with_keys_case_upper(self):
        config = EnvatorConfigDict({"FooBar": 42, "BazQux": 69})
        assert config.with_keys_case(NamingCase.UPPER) == {"FOOBAR": 42, "BAZQUX": 69}

    def test_with_keys_case_snake(self):
        config = EnvatorConfigDict({"FooBar": 42, "BazQux": 69})
        assert config.with_keys_case(NamingCase.SNAKE) == {"foo_bar": 42, "baz_qux": 69}

    def test_with_keys_case_kebab(self):
        config = EnvatorConfigDict({"FooBar": 42, "BazQux": 69})
        assert config.with_keys_case(NamingCase.KEBAB) == {"foo-bar": 42, "baz-qux": 69}

    def test_with_keys_case_title(self):
        config = EnvatorConfigDict({"FooBar": 42, "BazQux": 69})
        assert config.with_keys_case(NamingCase.TITLE) == {"Foobar": 42, "Bazqux": 69}

    def test_with_keys_case_camel(self):
        config = EnvatorConfigDict({'foo_bar': 42, 'baz_qux': 69})
        assert config.with_keys_case(NamingCase.CAMEL) == {'fooBar': 42, 'bazQux': 69}

    def test_with_keys_case_pascal(self):
        config = EnvatorConfigDict({'foo_bar': 42, 'baz_qux': 69})
        assert config.with_keys_case(NamingCase.PASCAL) == {'FooBar': 42, 'BazQux': 69}
