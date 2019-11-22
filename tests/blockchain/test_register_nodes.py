from .test_case.blockchain import BlockchainTestCase
from model import Blockchain


class TestRegisterNodes(BlockchainTestCase):
    def test_valid_nodes(self):
        blockchain = Blockchain()

        blockchain.register_node("http://192.168.0.1:5000")

        self.assertIn("192.168.0.1:5000", blockchain.nodes)

    def test_malformed_nodes(self):
        blockchain = Blockchain()

        with self.assertRaises(ValueError):
            blockchain.register_node("http//192.168.0.1:5000")

    def test_idempotency(self):
        blockchain = Blockchain()

        blockchain.register_node("http://192.168.0.1:5000")
        blockchain.register_node("http://192.168.0.1:5000")

        assert len(blockchain.nodes) == 1
