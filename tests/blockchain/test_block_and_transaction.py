from .test_case.blockchain import BlockchainTestCase


class TestBlocksAndTransactions(BlockchainTestCase):
    def test_block_creation(self):
        self.create_block()

        latest_block = self.blockchain.last_block

        # The genesis block is create at initialization, so the length should be 2
        assert len(self.blockchain.chain) == 2
        assert latest_block["index"] == 2
        assert latest_block["timestamp"] is not None
        assert latest_block["proof"] == 123
        assert latest_block["previous_hash"] == "abc"

    def test_create_transaction(self):
        self.create_transaction()

        transaction = self.blockchain.current_transactions[-1]

        assert transaction
        assert transaction["sender"] == "a"
        assert transaction["recipient"] == "b"
        assert transaction["amount"] == 1

    def test_block_resets_transactions(self):
        self.create_transaction()

        initial_length = len(self.blockchain.current_transactions)

        self.create_block()

        current_length = len(self.blockchain.current_transactions)

        assert initial_length == 1
        assert current_length == 0

    def test_return_last_block(self):
        self.create_block()

        created_block = self.blockchain.last_block

        assert len(self.blockchain.chain) == 2
        assert created_block is self.blockchain.chain[-1]
