from twitter_ads_v2.utils import CustomDecorators


def test_decorator_deprecated():
    import warnings

    class TestClass(object):
        @classmethod
        @CustomDecorators.deprecated('deprecated API')
        def test(self):
            pass

    with warnings.catch_warnings(record=True) as log:
        TestClass.test()
        assert len(log) == 1
        assert issubclass(log[-1].category, DeprecationWarning)
        assert "TestClass.test" in str(log[-1].message)
        assert "deprecated API" in str(log[-1].message)
