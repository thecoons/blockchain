import json
import hashlib

from .test_case.blockchain import BlockchainTestCase


class TestHashingAndProofs(BlockchainTestCase):
    def test_hash_is_correct(self):
        self.create_block()

        new_block = self.blockchain.last_block
        new_block_json = json.dumps(
            self.blockchain.last_block, sort_keys=True
        ).encode()
        new_hash = hashlib.sha256(new_block_json).hexdigest()

        assert len(new_hash) == 64
        assert new_hash == self.blockchain.hash(new_block)
