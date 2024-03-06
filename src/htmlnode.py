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
        return new_string

    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props):
        self.tag = tag
        self.value = value
        self.props = props
