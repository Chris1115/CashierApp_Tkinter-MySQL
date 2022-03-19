import unittest
import backend

class test_syntax(unittest.TestCase, backend.backend):

    def test_select(self):
        self.assertEqual(self.select("SELECT * FROM product where id = 1")[0][0], 1)

    def test_insert(self):
        self.assertTrue(self.action("INSERT INTO product VALUES (21, 'Kwetiau Pangsit Jamur', 10, 15000)"))

    def test_edit(self):
        self.assertTrue(self.action("UPDATE product SET id=21, name='Kwetiau Pangsit Jamur', stock='9', price='18000' WHERE id=21"))

    def test_delete(self):
        self.assertTrue(self.action("DELETE FROM product WHERE id=21"))

    def test_getRowCounts(self):
        self.assertEqual(self.getRowCounts()[0][0], 20)

if __name__ == '__main__':
    unittest.main()