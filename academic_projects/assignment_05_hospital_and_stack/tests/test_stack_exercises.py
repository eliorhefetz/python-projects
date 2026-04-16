import unittest
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from stack_exercises import Stack, removeDuplicates, findUnmatch, equalStacks, compressStr, reverseSentence


class TestStackExercises(unittest.TestCase):
    def test_find_unmatch(self):
        self.assertEqual(findUnmatch("(()))"), ")")
        self.assertEqual(findUnmatch("((())"), "(")
        self.assertIsNone(findUnmatch("(())"))

    def test_equal_stacks(self):
        stack1 = Stack()
        stack2 = Stack()

        for value in [1, 2, 3]:
            stack1.push(value)

        for value in [3, 1, 2]:
            stack2.push(value)

        self.assertTrue(equalStacks(stack1, stack2))

    def test_reverse_sentence(self):
        self.assertEqual(reverseSentence("hello world!"), "olleh !dlrow")

    def test_compress_string_current_implementation(self):
        self.assertEqual(compressStr("aabbbcc"), "a2b3c2")
        self.assertEqual(compressStr("abbcbb"), "ab2cb2")


if __name__ == "__main__":
    unittest.main()
