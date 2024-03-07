from textnode import TextNode


def markdown_to_blocks(markdown):
    new_list = markdown.split('\n\n')
    empty_index = []
    for i in range(len(new_list)):
        if new_list[i] == '\n' or new_list[i] == '':
            empty_index.append(i)
        else:
            new_list[i] = new_list[i].strip()
    for index in empty_index:
        new_list.pop(index)

    return new_list


def block_to_block_type(block):
    if block.startswith('#'):
        return 'heading'
    if block.startswith('```') and block.endswith('```'):
        return 'code'
    if block.startswith('>'):
        block_type = 'quote'
        for line in block.split('\n'):
            if not line.strip().startswith('>'):
                block_type = 'paragraph'
        return block_type
    if block.startswith('*') or block.startswith('-'):
        block_type = 'unordered_list'
        for line in block.split('\n'):
            if not line.strip().startswith('*') and not line.startswith('-'):
                block_type = 'paragraph'
        return block_type
    if block.startswith('1.'):
        block_type = 'ordered_list'
        line = block.split('\n')
        for i in range(1, len(line) + 1):
            if not line[i - 1].strip().startswith(f'{i}.'):
                block_type = 'paragraph'
        return block_type
    return 'paragraph'
