import sys
from test import support, list_tests

class ListTest(list_tests.CommonTest):

    type2test = list

    def test_basic(self):
        self.assertEqual(self.type2test([]), [])
        l0_3 = [0, 1, 2, 3]
        l0_3_bis = self.type2test(l0_3)
        self.assertEqual(l0_3, l0_3_bis)
        self.assertTrue(l0_3 is not l0_3_bis)
        self.assertEqual(self.type2test(()), [])
        self.assertEqual(self.type2test((0, 1, 2, 3)), [0, 1, 2, 3])
        self.assertEqual(self.type2test(''), [])
        self.assertEqual(self.type2test('spam'), ['s', 'p', 'a', 'm'])

        #FIXME: too brutal for us ATM.
        if not support.is_jython:
            if sys.maxsize == 0x7fffffff:
                # This test can currently only work on 32-bit machines.
                # XXX If/when PySequence_Length() returns a ssize_t, it should be
                # XXX re-enabled.
                # Verify clearing of bug #556025.
                # This assumes that the max data size (sys.maxint) == max
                # address size this also assumes that the address size is at
                # least 4 bytes with 8 byte addresses, the bug is not well
                # tested
                #
                # Note: This test is expected to SEGV under Cygwin 1.3.12 or
                # earlier due to a newlib bug.  See the following mailing list
                # thread for the details:

                #     http://sources.redhat.com/ml/newlib/2002/msg00369.html
                self.assertRaises(MemoryError, list, range(sys.maxsize // 2))

        # This code used to segfault in Py2.4a3
        x = []
        x.extend(-y for y in x)
        self.assertEqual(x, [])

    def test_truth(self):
        super(ListTest, self).test_truth()
        self.assertTrue(not self.type2test([]))
        self.assertTrue(self.type2test([42]))

    def test_identity(self):
        self.assertTrue([] is not [])
        self.assertTrue(self.type2test([]) is not self.type2test([]))

    def test_len(self):
        super(ListTest, self).test_len()
        self.assertEqual(len(self.type2test([])), 0)
        self.assertEqual(len(self.type2test([0])), 1)
        self.assertEqual(len(self.type2test([0, 1, 2])), 3)

    def test_overflow(self):
        lst = self.type2test([4, 5, 6, 7])
        n = int((sys.maxsize*2+2) // len(lst))
        def mul(a, b): return a * b
        def imul(a, b): a *= b
        self.assertRaises((MemoryError, OverflowError), mul, lst, n)
        self.assertRaises((MemoryError, OverflowError), imul, lst, n)

def test_main(verbose=None):
    support.run_unittest(ListTest)

    # verify reference counting
    import sys
    if verbose and hasattr(sys, "gettotalrefcount"):
        import gc
        counts = [None] * 5
        for i in range(len(counts)):
            support.run_unittest(ListTest)
            gc.collect()
            counts[i] = sys.gettotalrefcount()
        print(counts)


if __name__ == "__main__":
    test_main(verbose=True)
