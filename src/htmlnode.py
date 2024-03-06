class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):

        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError('not implemented')

    def props_to_html(self):
        if not self.props:
            return ''
        new_string = ""
        for key, value in self.props.items():
            new_string += f'{key}="{value}" '
        return new_string.strip(' ')

    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if not self.tag:
            return f'{self.value}'
        if not self.props:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        return f'<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>'


class ParentNode(HTMLNode):
    def __init__(self, children, tag=None):
        super().__init__(children=children, tag=tag)

    def to_html(self):
        if not self.tag:
            raise ValueError('No tag found')
        if not self.children:
            raise ValueError('No children found')

        new_string = ''

        for node in self.children:
            new_string += node.to_html()

        return f'<{self.tag}>{new_string}</{self.tag}>'


def text_node_to_html_node(text_node):
    text_type = {
        'text': '',
        'bold': 'b',
        'italic': 'i',
        'code': 'code',
        'link': 'a',
        'image': 'img'
    }

    if text_node.text_type in text_type:
        return LeafNode(text_node.text, text_type[text_node.type])
    raise Exception('Type not found')
