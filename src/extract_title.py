from block_markdown import markdown_to_blocks


def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        count = 0
        block_copy = block
        while block_copy.startswith("#"):
            block_copy = block_copy[1:]
            count += 1

        if count == 1:
            return block.strip("# ")
    raise Exception("no h1 header")
