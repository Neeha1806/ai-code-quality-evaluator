import unittest
from evaluator import evaluate


class EvaluatorTests(unittest.TestCase):
    def test_valid_code(self):
        self.assertIn("No issues found", evaluate("print('hello')")[0])

    def test_syntax_error(self):
        self.assertIn("Syntax error", evaluate("def broken(:\n pass")[0])

    def test_bare_except(self):
        self.assertTrue(any("bare except" in item for item in evaluate("try:\n pass\nexcept:\n pass")))

    def test_long_line(self):
        self.assertTrue(any("exceeds 88" in item for item in evaluate("# " + "x" * 90)))

    def test_short_line(self):
        self.assertFalse(any("exceeds 88" in item for item in evaluate("x = 1")))

    def test_eval(self):
        self.assertTrue(any("eval()" in item for item in evaluate("result = eval('1+1')")))


if __name__ == "__main__":
    unittest.main()
