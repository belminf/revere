import os
import revere
import revere.database
import unittest
import tempfile


class UserResourcesTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, self.db_fn = tempfile.mkstemp()

        revere.app.config['DATABASE_URL'] = 'sqlite:///{}'.format(self.db_fn)
        revere.app.config['TESTING'] = True

        with revere.app.app_context():
            revere.database.init_db()

    def test_dummy(self):
        self.assertEqual(True, True)

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(self.db_fn)


if __name__ == '__main__':
    unittest.main()
