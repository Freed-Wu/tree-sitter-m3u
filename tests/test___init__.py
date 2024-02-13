r"""Test __init__.py."""

import os

from tree_sitter_hlsplaylist import parser


class Test:
    r"""Test."""

    @staticmethod
    def test_parser() -> None:
        r"""Test parser.

        :rtype: None
        """
        with open(
            os.path.join(os.path.dirname(__file__), "zho.hlsplaylist"), "rb"
        ) as f:
            text = f.read()
        tree = parser.parse(text)
        assert len(tree.root_node.children)
